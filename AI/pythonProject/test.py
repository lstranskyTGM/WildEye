from ultralytics import YOLO
import os
import cv2

# Lade das trainierte Modell
model = YOLO('best.pt')  # oder 'last.pt'

# Erstelle den Ausgabeordner für Bilder mit Bounding Boxes
output_dir = "labeled"
os.makedirs(output_dir, exist_ok=True)

# Verarbeite alle Bilder im Ordner "img"
for file in os.listdir('img'):
    if file.endswith('.jpeg') or file.endswith('.jpg'):
        img_path = os.path.join('img', file)

        # Vorhersage mit YOLO
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
            cv2.rectangle(img, (text_x, text_y - text_size[1] - 5), (text_x + text_size[0] + 5, text_y + 5),(0, 255, 0), -1)
            cv2.putText(img, class_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)

        # Speicher das Bild mit Bounding Boxes
        labeled_img_path = os.path.join(output_dir, f"labeled_{file}")
        cv2.imwrite(labeled_img_path, img)