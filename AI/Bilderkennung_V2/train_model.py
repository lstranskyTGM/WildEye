import torch
import torch.nn as nn
import torch.optim as optim
from data_loader import get_dataloaders
from model_define import CNNModel
from torchviz import make_dot

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


def visualize_model_with_weights(model, example_input, output_path="model_topology_with_weights"):
    model.eval()  # Switch to evaluation mode
    with torch.no_grad():
        output = model(example_input)  # Generate example output

    # Visualize the model with Torchviz, including weights
    dot = make_dot(output, params=dict(model.named_parameters()))
    dot.render(output_path, format="png")
    print(f"Model topology with weights saved to {output_path}.png")

if __name__ == "__main__":
    # Retrain the model
    train_loader, _ = get_dataloaders(root_dir=".", batch_size=8)
    model = CNNModel()

    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # Train and save the model
    train_model(model, optimizer, train_loader, criterion, epochs=5, save_path="cnn_model.pth")

    print("Model retrained and saved to cnn_model.pth")

    # Visualize the model with weights
    example_input = torch.randn(1, 3, 64, 64)  # Adjusted input size to match training data
    visualize_model_with_weights(model, example_input, output_path="cnn_model_topology_with_weights")