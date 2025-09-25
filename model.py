# model.py
import torch
import torch.nn as nn

class NFLBettingModel(nn.Module):
    def __init__(self, input_dim):
        super(NFLBettingModel, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.layers(x)


def load_model(model_path, input_dim):
    model = NFLBettingModel(input_dim)
    try:
        model.load_state_dict(torch.load(model_path))
        model.eval()
        print(f"✅ Loaded trained model from {model_path}")
    except FileNotFoundError:
        print(f"⚠️ No pretrained model at {model_path}, using untrained model.")
    return model
