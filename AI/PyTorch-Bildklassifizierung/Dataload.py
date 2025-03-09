import os
import shutil
import random
from pathlib import Path


class Dataload:
    def __init__(self, data_dir: str, output_dir: str, split_ratio: float = 0.9):
        self.data_dir = Path("../" + data_dir)
        self.output_dir = Path(output_dir)
        self.split_ratio = split_ratio
        self.train_dir = self.output_dir / "train"
        self.test_dir = self.output_dir / "test"
        self.categories = [d.name for d in self.data_dir.iterdir() if d.is_dir()]

    def prepare_data(self):
        # Erstelle Zielverzeichnisse
        for category in self.categories:
            (self.train_dir / category).mkdir(parents=True, exist_ok=True)
            (self.test_dir / category).mkdir(parents=True, exist_ok=True)

        # Verarbeite jede Kategorie
        for category in self.categories:
            image_paths = list((self.data_dir / category).glob("*.jpg"))  # Anpassung an Bildformate möglich
            random.shuffle(image_paths)

            split_idx = int(len(image_paths) * self.split_ratio)
            train_images = image_paths[:split_idx]
            test_images = image_paths[split_idx:]

            # Kopiere Bilder
            self._copy_images(train_images, self.train_dir / category)
            self._copy_images(test_images, self.test_dir / category)

            print(f"Kategorie {category}: {len(train_images)} Trainingsbilder, {len(test_images)} Testbilder")

    def _copy_images(self, images, target_dir):
        for img_path in images:
            shutil.copy(img_path, target_dir)


# Nutzung
if __name__ == "__main__":
    data_preparer = Dataload("categorized_objects", "training_v2")
    data_preparer.prepare_data()
