# model_define.py

import torch.nn as nn
import torch

import torch.nn as nn
import torch

import torch.nn as nn
import torch


class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()

        # Weniger Convolutional Layer und weniger Filter
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3)  # Reduzierte Anzahl der Filter
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3)  # Reduzierte Anzahl der Filter

        # Berechne die Flatten-Größe basierend auf der neuen Bildgröße (64x64)
        self.flatten_size = 32 * 16 * 16  # Korrekte Größe nach zwei Pooling-Schichten

        # Kleinere Fully Connected Layer
        self.fc1 = nn.Linear(self.flatten_size, 128)  # Kleinere Anzahl von Neuronen
        self.fc2 = nn.Linear(128, 64)  # Kleinere Anzahl von Neuronen
        self.fc3 = nn.Linear(64, 2)  # 2 Ausgänge für 2 Klassen

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # Erste Convolution + Pooling
        x = self.pool(torch.relu(self.conv2(x)))  # Zweite Convolution + Pooling
        x = x.view(-1, self.flatten_size)  # Flatten für Fully Connected Layer
        x = torch.relu(self.fc1(x))  # Erste Fully Connected Schicht
        x = torch.relu(self.fc2(x))  # Zweite Fully Connected Schicht
        x = self.fc3(x)  # Ausgabe (2 Klassen)
        return x
