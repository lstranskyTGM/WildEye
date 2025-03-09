
from pathlib import Path
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

from training_v1.CreatDataset import CustomDataset
from training_v1.Model_v4 import ConvNet


class Trainer:
    def __init__(self, model, dataset, epochs=60, save_interval=1, save_dir="Model4"):
        self.model = model
        self.dataset = dataset
        self.epochs = epochs
        self.save_interval = save_interval
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
        self.dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

    def train(self):
        for epoch in range(1, self.epochs + 1):
            running_loss = 0.0
            for images, labels in self.dataloader:
                self.optimizer.zero_grad()
                outputs = self.model(images)
                loss = self.criterion(outputs, labels.long())
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()

            print(f"Epoch {epoch}/{self.epochs}, Loss: {running_loss / len(self.dataloader):.4f}")

            if epoch % self.save_interval == 0:
                torch.save(self.model.state_dict(), self.save_dir / f"model_epoch_{epoch}.pth")
                print(f"Model nach {epoch} Epochen gespeichert.")


# Nutzung
if __name__ == "__main__":
    model = ConvNet(num_classes=4)  # Beispiel mit 6 Klassen
    dataset = CustomDataset(
        data_dir="training_v2/train",
        transform=transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor()
        ]),
        target_classes=["Bear", "goat", "WildBoar", "Deer"]
    )
    trainer = Trainer(model, dataset)
    trainer.train()