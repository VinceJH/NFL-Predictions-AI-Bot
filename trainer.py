# Training loop for historical data.

# trainer.py (updated for real dataset)
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from model import NFLBettingModel

def load_training_data(path="data/training_data.csv"):
    df = pd.read_csv(path)
    X = df.drop(columns=["label"]).values
    y = df["label"].values

    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32).unsqueeze(1)

    input_dim = X_tensor.shape[1]
    return X_tensor, y_tensor, input_dim

def train_model(X, y, input_dim, save_path="models/nfl_model.pt", epochs=500, lr=0.01):
    model = NFLBettingModel(input_dim)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.BCELoss()

    for epoch in range(epochs):
        optimizer.zero_grad()
        preds = model(X)
        loss = loss_fn(preds, y)
        loss.backward()
        optimizer.step()

        if epoch % 100 == 0:
            acc = ((preds > 0.5).float() == y).float().mean().item()
            print(f"Epoch {epoch} | Loss: {loss.item():.4f} | Acc: {acc:.2f}")

    torch.save(model.state_dict(), save_path)
    print(f"✅ Training complete, model saved to {save_path}")
    return model

if __name__ == "__main__":
    X, y, input_dim = load_training_data()
    train_model(X, y, input_dim)


