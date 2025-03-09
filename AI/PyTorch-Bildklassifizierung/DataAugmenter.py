
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import cv2
import numpy as np

class DataAugmenter:
    def __init__(self, train_dir: str):
        self.train_dir = Path(train_dir)
        self.categories = [d.name for d in self.train_dir.iterdir() if d.is_dir()]
        self.valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

    def augment_data(self):
        for category in self.categories:
            image_paths = [p for p in (self.train_dir / category).iterdir() if p.suffix.lower() in self.valid_extensions]
            for img_path in image_paths:
                self._augment_image(img_path)

    def _augment_image(self, img_path):
        try:
            img = Image.open(img_path)
            img_cv = cv2.imread(str(img_path))

            # Gespiegelte Version
            flipped = ImageOps.mirror(img)
            flipped.save(img_path.parent / f"flipped_{img_path.name}")

            # Drehungen
            rotated_90 = img.rotate(90)
            rotated_90.save(img_path.parent / f"rotated90_{img_path.name}")

            rotated_180 = img.rotate(180)
            rotated_180.save(img_path.parent / f"rotated180_{img_path.name}")

            rotated_270 = img.rotate(270)
            rotated_270.save(img_path.parent / f"rotated270_{img_path.name}")

            # Kontrast erhöhen
            enhancer = ImageEnhance.Contrast(img)
            contrast = enhancer.enhance(1.5)
            contrast.save(img_path.parent / f"contrast_{img_path.name}")

            # Helligkeit verringern
            enhancer = ImageEnhance.Brightness(img)
            darker = enhancer.enhance(0.7)
            darker.save(img_path.parent / f"darker_{img_path.name}")

            # Rauschen hinzufügen
            if img_cv is not None:
                noisy = self._add_noise(img_cv)
                cv2.imwrite(str(img_path.parent / f"noisy_{img_path.stem}.jpg"), noisy)

            # Schwarz-Weiß-Version
            if img_cv is not None and len(img_cv.shape) == 3:
                gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(str(img_path.parent / f"gray_{img_path.stem}.jpg"), gray)

        except Exception as e:
            print(f"Fehler bei {img_path}: {e}")

    def _add_noise(self, img):
        """ Fügt zufälliges Gaußsches Rauschen zum Bild hinzu """
        row, col, ch = img.shape
        mean = 0
        sigma = 15
        gauss = np.random.normal(mean, sigma, (row, col, ch)).astype('uint8')
        noisy = cv2.add(img, gauss)
        return noisy


if __name__ == "__main__":
    augmenter = DataAugmenter("training_v2/train")
    augmenter.augment_data()

