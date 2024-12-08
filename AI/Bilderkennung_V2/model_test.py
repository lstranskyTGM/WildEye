import torch
from model_define import CNNModel  # Importiere das Modell, das du definiert hast
from data_loader import get_dataloaders


# Testfunktion
def test_model(model_path, test_loader):
    # Modell instanziieren
    model = CNNModel()

    # Lade die gespeicherten Modellgewichte
    checkpoint = torch.load(model_path, weights_only=True)  # Nur die Gewichte laden
    model.load_state_dict(checkpoint)  # Gewichte in das Modell laden

    # Setze das Modell in den Evaluationsmodus
    model.eval()

    # Initialisiere Variablen zur Berechnung der Genauigkeit
    correct = 0
    total = 0

    with torch.no_grad():  # Kein Gradientenberechnung während der Evaluation
        for inputs, labels in test_loader:
            # Führe Vorhersagen durch
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)  # Wähle die Klasse mit der höchsten Wahrscheinlichkeit

            # Berechne die Anzahl der korrekten Vorhersagen
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    # Berechne die Genauigkeit
    accuracy = 100 * correct / total
    print(f'Accuracy of the model on the test images: {accuracy:.2f}%')


if __name__ == "__main__":
    # Lade die Test-Daten
    _, test_loader = get_dataloaders(root_dir=".", batch_size=8)

    # Definiere den Pfad zum gespeicherten Modell
    model_path = "cnn_model.pth"

    # Teste das Modell
    test_model(model_path, test_loader)
