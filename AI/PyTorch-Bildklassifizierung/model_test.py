
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

from training_v1.CreatDataset import CustomDataset
from training_v1.Model_v4 import ConvNet


def count_training_images(train_dir):
    train_dir = Path(train_dir)
    category_counts = {category.name: len(list(category.glob("*.jpg"))) for category in train_dir.iterdir() if
                       category.is_dir()}

    for category, count in category_counts.items():
        print(f"{category}: {count} Bilder")

    return category_counts

class Tester:
    def __init__(self, model_dir, dataset):
        self.model_dir = Path(model_dir)
        self.dataset = dataset
        self.dataloader = DataLoader(dataset, batch_size=32, shuffle=False)
        self.models = sorted(self.model_dir.glob("*.pth"))
        self.label_map = dataset.label_map
        self.num_classes = len(self.label_map)

    def test_models(self):
        results = {}
        for model_path in self.models:
            model = ConvNet(num_classes=self.num_classes)
            model.load_state_dict(torch.load(model_path))
            model.eval()

            correct = 0
            total = 0
            class_correct = np.zeros(self.num_classes)
            class_total = np.zeros(self.num_classes)

            with torch.no_grad():
                for images, labels in self.dataloader:
                    outputs = model(images)
                    _, predicted = torch.max(outputs, 1)

                    total += labels.size(0)
                    correct += (predicted == labels).sum().item()

                    for i in range(len(labels)):
                        label = labels[i].item()
                        class_total[label] += 1
                        if predicted[i].item() == label:
                            class_correct[label] += 1

            accuracy = correct / total
            class_accuracies = {label: class_correct[idx] / class_total[idx] if class_total[idx] > 0 else 0.0 for
                                label, idx in self.label_map.items()}

            results[model_path.name] = (accuracy, class_accuracies)
            print(f"Modell {model_path.name}: Gesamtgenauigkeit {accuracy:.4f}")
            for class_name, acc in class_accuracies.items():
                print(f"  - {class_name}: {acc:.4f}")

        best_model = max(results, key=lambda k: results[k][0])
        print(f"Bestes Modell: {best_model} mit Gesamtgenauigkeit {results[best_model][0]:.4f}")



if __name__ == "__main__":
    count_training_images("training_v2/train")
    dataset = CustomDataset("training_v1/test", transform=transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ]))
    tester = Tester("Model4", dataset)
    tester.test_models()