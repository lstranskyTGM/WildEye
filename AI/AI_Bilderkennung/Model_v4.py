
import torch.nn as nn
import torch.nn.functional as F

class ConvNet(nn.Module):
    def __init__(self, num_classes):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(64 * 128 * 128, 128)  # Angenommen, Input-Bilder sind 128x128
        self.dropout = nn.Dropout(0.2)  # Dropout nach Flatten
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.flatten(x)
        x = self.dropout(F.relu(self.fc1(x)))  # Dropout nach Fully-Connected
        x = self.fc2(x)  # Kein Softmax hier!
        return x