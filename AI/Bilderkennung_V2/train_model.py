import torch
import torch.nn as nn
import torch.optim as optim
from data_loader import get_dataloaders
from model_define import CNNModel
from torchviz import make_dot
# CNN-Modell-Klasse

# Trainingsfunktion
def train_model(model, optimizer, loader, criterion, epochs=5, save_path="model.pth"):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for inputs, labels in loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {running_loss / len(loader)}')
    torch.save(model.state_dict(), save_path)
    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    train_loader, _ = get_dataloaders(root_dir=".", batch_size=8)
    model = CNNModel()

    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # Trainiere das Modell und speichere es
    train_model(model, optimizer, train_loader, criterion, epochs=50, save_path="cnn_model.pth")
    make_dot(output, params=dict(model.named_parameters())).render("model_topology", format="png")
