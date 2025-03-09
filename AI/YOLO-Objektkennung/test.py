from ultralytics import YOLO

# Lade das trainierte Modell aus train7
model = YOLO('runs/detect/train7/weights/best.pt')  # oder 'last.pt'

# Validiere das Modell auf dem Testdatensatz
#metrics = model.val()

# Zeige die Metriken an
#print(metrics)
results = model.predict('elfant.jpg', save=True)

# Optional: Zeige die Ergebnisse an
print(results)

for box in results[0].boxes:
    print(results[0].names[int(box.cls)])
