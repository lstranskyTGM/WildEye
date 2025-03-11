from ultralytics import YOLO
import os
import cv2
import torch
import torchvision.transforms as transforms
from PIL import Image
from Model_v4 import ConvNet


def analyze_latest_image(input_dir: str, output_path: str):
    object_detector = YOLO('best.pt')
    num_classes = 4
    classification_model = ConvNet(num_classes)
    classification_model.load_state_dict(torch.load('model_epoch_32.pth', map_location=torch.device('cpu')))
    classification_model.eval()

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    class_labels = ["Bear", "Goat", "WildBoar", "Deer"]

    jpeg_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpeg', '.jpg', '.png'))]
    if not jpeg_files:
        return {'title': None, 'tags': [], 'filename': None}

    latest_file = max(jpeg_files, key=lambda f: os.path.getctime(os.path.join(input_dir, f)))
    img_path = os.path.join(input_dir, latest_file)
    print(f"Trying to analyze picture from {img_path}")

    detection_results = object_detector.predict(img_path)
    img = cv2.imread(img_path)
    img_height, img_width, _ = img.shape

    detected_tags = set()

    for box in detection_results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        class_id = int(box.cls)
        detected_class = (detection_results[0].names[class_id])

        cropped_img = img[y1:y2, x1:x2]
        cropped_pil = Image.fromarray(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
        input_tensor = transform(cropped_pil).unsqueeze(0)

        with torch.no_grad():
            outputs = classification_model(input_tensor)
            probs = torch.softmax(outputs, dim=1)
            confidence, pred_idx = torch.max(probs, 1)
            predicted_class = class_labels[pred_idx.item()]

        print(f"Objekt: {detected_class} -> Klassifikation: {predicted_class} ({confidence.item():.4f})")
        detected_tags.add(predicted_class)
        if confidence.item() != 1:
            predicted_class = detected_class
        label_text = f"{predicted_class} ({confidence.item():.2f})"
        scale_factor = max(img_width, img_height) / 1000
        font_scale = max(1, scale_factor * 1.5)
        thickness = max(2, int(scale_factor * 3))

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness)
        text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
        text_x, text_y = x1, max(y1 - 10, text_size[1] + 10)
        cv2.rectangle(img, (text_x, text_y - text_size[1] - 5), (text_x + text_size[0] + 5, text_y + 5), (0, 255, 0),
                      -1)
        cv2.putText(img, label_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness,
                    cv2.LINE_AA)

    filename = "output.jpg"
    labeled_img_path = os.path.join(output_path, filename)
    cv2.imwrite(labeled_img_path, img)

    detected_tags = list(detected_tags)
    title = f"new {detected_tags[0]}" if detected_tags else None
    tag = detected_tags[0] if detected_tags else None

    return {'title': title, 'tags': tag, 'filename': filename}
