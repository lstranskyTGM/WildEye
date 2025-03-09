import os
import shutil
import random
from pathlib import Path
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

class CustomDataset(Dataset):
    def __init__(self, data_dir: str, transform=None, target_classes=None):
        self.data_dir = Path(data_dir)
        self.transform = transform

        # Liste der gewünschten Klassen zum Filtern
        self.target_classes = target_classes if target_classes else ["Bear", "goat", "WildBoar", "Deer"]

        # Labels nur für die gewünschten Klassen erstellen
        self.label_map = {category: i for i, category in enumerate(self.target_classes)}

        # Nur Bildpfade aufnehmen, deren Klassen in der Ziel-Liste enthalten sind
        self.image_paths = [
            img for img in self.data_dir.glob("**/*.jpg")
            if img.parent.name in self.target_classes
        ]

        random.shuffle(self.image_paths)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.label_map[img_path.parent.name]
        image = Image.open(img_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label



if __name__ == "__main__":
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])
    dataset = CustomDataset("training_v1/train", transform=transform)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    print(f"Dataset Größe: {len(dataset)} Bilder")