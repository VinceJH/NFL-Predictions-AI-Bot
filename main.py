# Entry point for predictions + orchestrating the pipeline.


# main.py
import torch
import numpy as np
from model import load_model
from utils import build_features, calculate_market_probs, decide_bets

# Example hardcoded game + metrics (in production these come from APIs)
upcoming_games = [
    {"home_team": "Ravens", "away_team": "Bengals", "spread": -2.5, "odds": -110}
]

team_metrics = {
    "Ravens": {"epa_per_play": 0.15, "success_rate": 0.48},
    "Bengals": {"epa_per_play": 0.05, "success_rate": 0.45}
}

if __name__ == "__main__":
    input_dim = 5  # features: home_epa, home_success, away_epa, away_success, spread
    model = load_model("models/nfl_model.pt", input_dim)

    for game in upcoming_games:
        features = build_features(game, team_metrics)
        features_tensor = torch.tensor(features).unsqueeze(0)  # shape [1, input_dim]

        model_prob = model(features_tensor).item()
        market_prob = calculate_market_probs(game["odds"])

        recommendation = decide_bets(game, model_prob, market_prob)
        print("\n📊 Recommendation:")
        for k, v in recommendation.items():
            print(f"{k}: {v}")