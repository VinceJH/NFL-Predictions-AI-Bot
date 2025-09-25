# Feature builder + odds conversion + bet decision.

# utils.py
import numpy as np

def build_features(game, metrics):
    home = metrics.get(game["home_team"], {})
    away = metrics.get(game["away_team"], {})

    home_epa = home.get("epa_per_play", 0.0)
    away_epa = away.get("epa_per_play", 0.0)
    home_success = home.get("success_rate", 0.0)
    away_success = away.get("success_rate", 0.0)
    spread = float(game.get("spread", 0))

    features = np.array([
        home_epa, home_success,
        away_epa, away_success,
        spread
    ], dtype=np.float32)

    return features


def calculate_market_probs(odds):
    if odds < 0:
        prob = -odds / (-odds + 100)
    else:
        prob = 100 / (odds + 100)
    return prob


def decide_bets(game, model_prob, market_prob, threshold=0.05):
    edge = model_prob - market_prob
    bet = None
    if edge > threshold:
        bet = "BET Home"
    elif edge < -threshold:
        bet = "BET Away"

    return {
        "game": f"{game['away_team']} @ {game['home_team']}",
        "spread": game["spread"],
        "model_prob": round(model_prob, 3),
        "market_prob": round(market_prob, 3),
        "edge": round(edge, 3),
        "recommendation": bet or "No Bet"
    }
