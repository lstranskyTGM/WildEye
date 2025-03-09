from ultralytics import YOLO

# Lade das Modell
model = YOLO('yolov8n.pt')  # 'n' steht für Nano. Alternativen: yolov8s.pt, yolov8m.pt, etc.

# Trainiere das Modell
model.train(
    data='data.yaml',  # Pfad zur data.yaml
    epochs=60,         # Anzahl der Epochen
    imgsz=640,         # Bildgröße
    batch=8,          # Batch-Größe
    workers=0          # Anzahl der Threads
)

# Optional: Validiere das Modell
metrics = model.val()
print(metrics)

# Optional: Modelle speichern oder weiterverwenden
model.save("best_model.pt")
