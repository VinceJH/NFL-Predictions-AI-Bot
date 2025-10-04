# **🏈 NFL Predictive Betting AI Bot (Still a work in Progress)**
An end-to-end sports analytics project that predicts NFL game outcomes and highlights value betting opportunities using machine learning, live odds APIs, and injury/news data.
**Disclaimer: This project is for educational purposes only**

Built with Python, PyTorch, and external data connectors (TheOddsAPI, news feeds), the bot analyzes each matchup and provides:

- Predicted winner

- Betting line recommendations (spread, moneyline)

- Evidence-backed reasoning (injuries, trends, odds movement)

# **Features**

Data Engineering

- Historical NFL game data ingestion (spreads, outcomes, performance metrics).

- Injury tracking across multiple weeks.

- Live odds fetching via TheOddsAPI
 (DraftKings, FanDuel, etc.).

Machine Learning

- Custom PyTorch neural network (NFLBettingModel) for win probability prediction.

- Training pipeline with accuracy tracking, saved checkpoints, and configurable features.

- Extendable feature set: spreads, team performance stats, injuries, trends, etc.

Betting Insights

- Model outputs predictions like:

     Week 4: Ravens -2.5 is a strong value play vs Browns (Injuries: Browns missing key OL, Ravens healthy, public money overinflated on Browns).

- Shows odds source, confidence score, and explainability report.

Modular Codebase

- data_loader.py – Loads & preprocesses datasets.

- model.py – PyTorch neural network & helpers.

- trainer.py – Training loop & evaluation.

- predictor.py – Generates predictions with reasoning.

- odds_api.py – Odds connector (TheOddsAPI).

- injury_tracker.py – Multi-week injury tracker.

- main.py – Entry point for generating weekly predictions.

# **Tech Stack**
- Language: Python 3.10+

- ML Framework: PyTorch

- Data: CSV historical games + live API feeds

- APIs: TheOddsAPI (for sportsbook odds), optional news scrapers

- Environment: VS Code / macOS / virtualenv

⚡ Example Usage
Train the model
python3 src/trainer.py  

Generate weekly predictions
python3 main.py

Sample Output:

Week 4 Prediction:
✅ Pick: Ravens -2.5 (DraftKings)
- Injuries: Browns missing LT + CB, Ravens healthy
- Historical trend: Ravens 7-1 ATS last 8 vs Browns
- Odds movement: Public money heavy on Browns, line inflated
Confidence: 73%

# **Future Improvements**
- Add advanced stats (EPA/play, DVOA, etc.)

- Improve NLP-driven news & injury parsing

- Integrate bet-tracking module for bankroll management

- Deploy as a web dashboard or Telegram bot
