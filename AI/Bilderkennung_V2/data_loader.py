import os

from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import torch
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

        for label, folder_name in enumerate(['fuchs', 'reh']):
            folder_path = os.path.join(root_dir, folder_name)
            for img_file in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img_file)
                if img_file.endswith('.jpg'):
                    self.images.append(img_path)
                    self.labels.append(label)

            #img = self.transform(img)
    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = self.images[idx]
        img = Image.open(img_path).convert('RGB')
        if self.transform:
            label = self.labels[idx]
        return img, label


def get_dataloaders(root_dir, batch_size=8):
    dataset = SymbolDataset(root_dir, transform=transform)

    # Indizes für die Klassen
    h_indices = [i for i, label in enumerate(dataset.labels) if label == 0][:30]
    nine_indices = [i for i, label in enumerate(dataset.labels) if label == 1][:30]

    train_indices = h_indices[:20] + nine_indices[:20]
    test_indices = h_indices[20:] + nine_indices[20:]

    # Subsets und DataLoader
    train_dataset = torch.utils.data.Subset(dataset, train_indices)
    test_dataset = torch.utils.data.Subset(dataset, test_indices)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    print(f"Anzahl Trainingsbilder: {len(train_dataset)}")
    print(f"Anzahl Testbilder: {len(test_dataset)}")

    return train_loader, test_loader
