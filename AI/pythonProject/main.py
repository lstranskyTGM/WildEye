from flask import Flask, request, jsonify, send_file
from ultralytics import YOLO
import cv2
import numpy as np
import os

app = Flask(__name__)
model = YOLO('best.pt')  # YOLO Modell laden


def process_image(image):
    # Bild speichern und analysieren
    img_array = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img_height, img_width, _ = img.shape

    results = model.predict(img)
    detected_classes = []

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        class_id = int(box.cls)
        class_name = results[0].names[class_id]
        detected_classes.append(class_name)

        # Dynamische Skalierung von Textgröße und Linienstärke
        scale_factor = max(img_width, img_height) / 1000
        font_scale = max(1, scale_factor * 1.5)
        thickness = max(2, int(scale_factor * 3))

        # Zeichne Bounding Box
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness)
        text_size = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
        text_x, text_y = x1, max(y1 - 10, text_size[1] + 10)
        cv2.rectangle(img, (text_x, text_y - text_size[1] - 5), (text_x + text_size[0] + 5, text_y + 5), (0, 255, 0),
                      -1)
        cv2.putText(img, class_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness,
                    cv2.LINE_AA)

    return img, detected_classes


@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    processed_img, detected_classes = process_image(image)
    output_path = 'output.jpg'
    cv2.imwrite(output_path, processed_img)

    return send_file(output_path, mimetype='image/jpeg', as_attachment=True), 200, {'Detected-Classes': ', '.join(detected_classes)}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

