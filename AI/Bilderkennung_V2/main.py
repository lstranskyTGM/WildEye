import imshow
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torch import classes
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split, Dataset
import numpy as np
import os
from PIL import Image


# Transformationspipeline (Bildgrößenanpassung und Normalisierung)
transform = transforms.Compose([
    transforms.Resize((150, 150)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Dataset-Klasse für das Symbol "H" und "9"
class SymbolDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        self.labels = []

        # Lade die Bilder aus den Ordnern "H" und "9"
        for label, folder_name in enumerate(['H', '9']):
            folder_path = os.path.join(root_dir, folder_name)
            for img_file in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img_file)
                self.images.append(img_path)
                self.labels.append(label)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = self.images[idx]
        img = Image.open(img_path).convert('RGB')
        if self.transform:
            img = self.transform(img)
        label = self.labels[idx]
        return img, label

# Lade den Datensatz
dataset = SymbolDataset('.', transform=transform)

# Berechne, wie viele Bilder pro Klasse vorhanden sind
num_h_images = sum(1 for label in dataset.labels if label == 0)
num_9_images = sum(1 for label in dataset.labels if label == 1)

# Überprüfe, ob es mindestens 30 Bilder pro Symbol gibt
assert num_h_images >= 30 and num_9_images >= 30, "Es müssen mindestens 30 Bilder pro Symbol (H und 9) vorhanden sein."

# Manuelle Aufteilung: Erst die ersten 30 "H" Symbole, dann die ersten 30 "9" Symbole
h_indices = [i for i, label in enumerate(dataset.labels) if label == 0][:30]  # 30 "H"
nine_indices = [i for i, label in enumerate(dataset.labels) if label == 1][:30]  # 30 "9"

# Aufteilen in Trainings- und Testsets (je 20 Trainings- und 10 Testdaten pro Klasse)
train_indices = h_indices[:20] + nine_indices[:20]  # 20 "H" + 20 "9" für Training
test_indices = h_indices[20:] + nine_indices[20:]   # 10 "H" + 10 "9" für Test


# Verwende Subset für die Train- und Test-Datensätze
train_dataset = torch.utils.data.Subset(dataset, train_indices)
test_dataset = torch.utils.data.Subset(dataset, test_indices)
#Trainings Daten aber h und 9 sind seperiert
train_dataset_h = torch.utils.data.Subset(dataset, h_indices[:20])
train_dataset_9 = torch.utils.data.Subset(dataset, nine_indices[:20])

# DataLoader für Training und Test: Die Daten werden in Tensoren gespeichert
train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False)
train_loader_h = DataLoader(train_dataset_h, batch_size=8, shuffle=False)
train_loader_9 = DataLoader(train_dataset_9, batch_size=8, shuffle=False)

# Prüfen der Anzahl der Bilder in den Datensätzen
print(f"Anzahl Trainingsbilder: {len(train_dataset)}")
print(f"Anzahl Testbilder: {len(test_dataset)}")
print(f"Anzahl Testbilder: {len(train_loader_h)}")
print(f"Anzahl Testbilder: {len(train_loader_9)}")


# Beispiel, um sicherzustellen, dass die Labels als Text zurückgegeben werden
for img, label in train_loader:
    print(label)  # Dies gibt "H" oder "9" für die entsprechenden Bilder zurück


# Klasse die, die Struktur der ersten 2 Models vorgibt
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        # Eingabe hat 3 Kanäle (z.B. RGB-Bild), Ausgabe hat 32 Kanäle
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        # Reduziert die räumlichen Dimensionen um den Faktor 2x2, was die Rechenlast senkt
        self.pool = nn.MaxPool2d(2, 2)
        # Nimmt die 32-Kanal-Eingabe von der vorherigen Schicht und gibt 64 Kanäle aus
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        # Diese Schicht nimmt die Ausgabe der vorherigen Convolution- und Pooling-Schichten,
        # die in ein eindimensionales Array umgeformt wurde (flattend).
        # Die Eingangsgröße beträgt 64 * 36 * 36 (64 Merkmalskarten, jede 36x36 Pixel).
        self.fc1 = nn.Linear(64 * 36 * 36, 128)
        # Diese Schicht reduziert die Dimension von 128 auf 2, um die Klassifikation durchzuführen.
        self.fc2 = nn.Linear(128, 2)  # 2 Klassen (symbol_1 und symbol_2)

    def forward(self, x):
        # Wendet die erste Convolution-Schicht (conv1) auf die Eingabe x an, gefolgt von der
        # ReLU-Aktivierungsfunktion, um negative Werte zu eliminieren und nicht-lineare
        x = self.pool(torch.relu(self.conv1(x)))
        # Macht genau das selbe um auf den zweiten Convolution-Schichten (conv2)
        x = self.pool(torch.relu(self.conv2(x)))
        # Formatiert die Ausgabe der Convolution-Schichten in ein eindimensionales Array,
        # damit sie in die voll verbundenen Schichten eingegeben werden kann.
        x = x.view(-1, 64 * 36 * 36)
        # Wendet die erste voll verbundene Schicht (fc1) auf die flachgedrückte Eingabe an
        x = torch.relu(self.fc1(x))
        # Wendet die zweite voll verbundene Schicht (fc2) an, die die endgültigen Ausgaben
        x = self.fc2(x)
        return x

# Die genauen Kommentare erspare ich mir hier: Sie sind sehr ähnlich zu den im Model davor
class CNNModel1(nn.Module):
    def __init__(self):
        super(CNNModel1, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(128, 2)  # Platzhalter, wird in forward angepasst
        self.fc2 = nn.Linear(128, 2)  # 2 Klassen (symbol_1 und symbol_2)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = self.pool(torch.relu(self.conv2(x)))

        # Dynamisches Flattening
        x = x.view(x.size(0), -1)  # Flatten

        # Dynamische Größe für fc1 berechnen
        if not hasattr(self, "fc1") or self.fc1.in_features != x.size(1):
            self.fc1 = nn.Linear(x.size(1), 128).to(x.device)

        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Die genauen Kommentare erspare ich mir hier: Sie sind sehr ähnlich zu den im Model davor
class CNNModel2(nn.Module):
    def __init__(self):
        super(CNNModel2, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=3)
        self.conv4 = nn.Conv2d(32, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(128, 2)  # Platzhalter, wird dynamisch angepasst
        self.fc2 = nn.Linear(128, 2)  # 2 Klassen (symbol_1 und symbol_2)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = self.pool(torch.relu(self.conv4(x)))
        x = self.pool(torch.relu(self.conv2(x)))

        # Dynamisches Flattening
        x = x.view(x.size(0), -1)  # Flatten

        # Dynamische Größe für fc1 berechnen
        if not hasattr(self, "fc1") or self.fc1.in_features != x.size(1):
            self.fc1 = nn.Linear(x.size(1), 128).to(x.device)

        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Erzeuge das Modell und definiere den Loss und Optimizer
model1 = CNNModel()
criterion = nn.CrossEntropyLoss()
optimizer1 = optim.Adam(model1.parameters(), lr=0.001)

model2 = CNNModel()
optimizer2 = optim.Adam(model2.parameters(), lr=0.001)

model3 = CNNModel1()
optimizer3 = optim.Adam(model3.parameters(), lr=0.001)

model4 = CNNModel2()
optimizer4 = optim.Adam(model4.parameters(), lr=0.001)

# In dieser Methode werden die Modelle trainiert
def train_model(modelv, optimizerv, loader, epochs=5):
    modelv.train()  # Setzt das Modell in den Trainingsmodus
    for epoch in range(epochs):  # Iteriert über die Anzahl der Epochen
        running_loss = 0.0  # Initialisiert den Verlust für die aktuelle Epoche
        for inputs, labels in loader:  # Durchläuft die Daten im Loader
            optimizerv.zero_grad()  # Setzt die Gradienten des Optimierers zurück
            outputs = modelv(inputs)  # Führt die Vorwärtsdurchlauf durch das Modell aus
            loss = criterion(outputs, labels)  # Berechnet den Verlust
            loss.backward()  # Berechnet die Gradienten durch Backpropagation
            optimizerv.step()  # Aktualisiert die Modellparameter
            running_loss += loss.item()  # Summiert den Verlust zur laufenden Summe
            print(f'Epoch [{epoch + 1}/{epochs}], Loss: {running_loss / len(loader)}')

# Trainiere das Modell für H
train_model(model1, optimizer1, train_loader)
train_model(model2, optimizer2, train_loader_h)
train_model(model2, optimizer2, train_loader_9)
train_model(model3, optimizer3, train_loader)
train_model(model4, optimizer4, train_loader)

# Teste das Modell
def test_model(loader, model1):
    model1.eval()  # Schaltet den Evaluationsmodus an
    correct = 0
    total = 0
    with torch.no_grad():  # Deaktiviert die Gradientenberechnung für die Evaluierung
        for inputs, labels in loader:  # Iteriert durch die Daten im Loader
            outputs = model1(inputs)  # Führt den Vorwärtsdurchlauf durch das Modell aus
            _, predicted = torch.max(outputs, 1)  # Bestimmt die Klasse mit der höchsten Wahrscheinlichkeit
            total += labels.size(0)
            correct += (predicted == labels).sum().item()  # Zählt die richtigen Vorhersagen
    print(f'Test Accuracy: {100 * correct / total:.2f}%')

# Teste das Modell auf H und 9
test_model(test_loader,model1)
test_model(test_loader,model2)
test_model(test_loader,model3)
test_model(test_loader,model4)

# Bedeutung der Begriffe:
#
#neuronales Netzwerk:
#
#



