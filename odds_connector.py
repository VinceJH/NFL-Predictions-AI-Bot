#Later, connect to TheOddsAPI (replace with real API key). (STUB)


# odds_connector.py
import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your TheOddsAPI key
BASE_URL = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds"

def get_live_odds():
    """
    Fetch live odds from TheOddsAPI.
    """
    params = {
        "apiKey": API_KEY,
        "regions": "us",
        "markets": "spreads",
        "oddsFormat": "american"
    }
    resp = requests.get(BASE_URL, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("⚠️ Error fetching odds:", resp.text)
        return []
