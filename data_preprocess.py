#preprocessing script to extra data from the spreadsheet containing the past data info

# data_preprocess.py
import pandas as pd

def create_training_data(input_csv="data/spreadspoke_scores.csv",
                         output_csv="data/training_data.csv"):
    df = pd.read_csv(input_csv)

    # Drop rows without spreads
    df = df.dropna(subset=["spread_favorite", "score_home", "score_away"])

    rows = []
    for _, row in df.iterrows():
        home = row["team_home"]
        away = row["team_away"]
        home_score = row["score_home"]
        away_score = row["score_away"]

        # Spread: negative if home favored, positive if away favored
        spread = float(row["spread_favorite"])
        if row["team_favorite_id"] == home:
            spread = -spread  # home favored
        else:
            spread = spread  # away favored

        # Label: 1 if home won, else 0
        label = 1 if home_score > away_score else 0

        # Here we’re only using spread as a feature for now.
        # Later you can merge with EPA, success rate, injuries.
        rows.append([spread, label])

    out_df = pd.DataFrame(rows, columns=["spread", "label"])
    out_df.to_csv(output_csv, index=False)
    print(f"✅ Training dataset saved to {output_csv} with {len(out_df)} rows.")

if __name__ == "__main__":
    create_training_data()
