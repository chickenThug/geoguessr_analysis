import pandas as pd
from duel_round import DuelRound
from argparse import ArgumentParser
from tqdm import tqdm

tqdm.pandas() 

def process_row(row):
    # Create a DuelRound instance from the row
    duel_round = DuelRound(
        round_number=row['round_number'],
        duel_id=row['duel_id'],
        timestamp=row['timestamp'],
        oliver_guess=row['oliver_guess'],
        viggo_guess=row['viggo_guess'],
        us_score=row['us_score'],
        best_opponent_guess=row['best_opponent_guess'],
        opponent_score=row['opponent_score'],
        country_code=row['country_code'],
        round_location=row['round_location'],
        state=row['state']
    )

    # Return a new DataFrame row with both original and new columns
    new_data = {
        'oliver_country': duel_round.oliver_country,
        'viggo_country': duel_round.viggo_country,
        'opponent_country': duel_round.opponent_country,
        'round_country': duel_round.round_country,
        'oliver_state': duel_round.oliver_state,
        'viggo_state': duel_round.viggo_state,
        'opponent_state': duel_round.opponent_state,
        'round_state': duel_round.round_state,
        'country_match': duel_round.country_match
    }
    return pd.Series({**row, **new_data})


def process_csv(input_file, output_file):
    # Read the input CSV into a DataFrame
    df = pd.read_csv(input_file)
    
    # Apply the process_row function to each row
    processed_df = df.progress_apply(process_row, axis=1)
    
    # Write the processed DataFrame to a new CSV file
    processed_df.to_csv(output_file, index=False)

def main():
    parser = ArgumentParser(description='Process a CSV file with DuelRound data.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file.')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file.')

    args = parser.parse_args()

    process_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()