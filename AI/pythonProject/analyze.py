from ultralytics import YOLO
import os
import cv2


def analyze_latest_image(input_dir: str, output_path: str):
    # Lade das trainierte Modell
    model = YOLO('best.pt')  # oder 'last.pt'

    # Finde das zuletzt hinzugefügte Bild im Eingabeverzeichnis
    jpeg_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpeg', '.jpg'))]
    if jpeg_files:
        latest_file = max(jpeg_files, key=lambda f: os.path.getctime(os.path.join(input_dir, f)))
        img_path = os.path.join(input_dir, latest_file)

        # Vorhersage mit YOLO
        print(f"Trying to analyze picture from {img_path}")
        results = model.predict(img_path)

    # Lade das Originalbild mit OpenCV
    img = cv2.imread(img_path)
    img_height, img_width, _ = img.shape

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        class_id = int(box.cls)
        class_name = results[0].names[class_id]
        print(class_name)

        # Dynamische Skalierung von Textgröße und Linienstärke
        scale_factor = max(img_width, img_height) / 1000
        font_scale = max(1, scale_factor * 1.5)
        thickness = max(2, int(scale_factor * 3))

        # Zeichne die Bounding Box auf das Bild
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness)

        # Schreibe den Klassennamen auf das Bild
        text_size = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
        text_x, text_y = x1, max(y1 - 10, text_size[1] + 10)
        cv2.rectangle(img, (text_x, text_y - text_size[1] - 5), (text_x + text_size[0] + 5, text_y + 5), (0, 255, 0),
                      -1)
        cv2.putText(img, class_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness,
                    cv2.LINE_AA)

    # Speicher das Bild mit Bounding Boxes und stelle sicher, dass nur ein Bild im Ausgabeordner existiert
    labeled_img_path = os.path.join(output_dir, "labeled_latest.jpg")
    cv2.imwrite(labeled_img_path, img)
