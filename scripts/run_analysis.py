"""
A standalone script to run a basic crypto intelligence analysis.
This script demonstrates how to use the modules within the 'nex_ai' package.
"""

import sys
import os

# Get the absolute path of the directory containing this script (scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the project root directory (one level up from scripts/)
project_root = os.path.join(script_dir, os.pardir)
# Add the 'src' directory to Python's path
sys.path.insert(0, os.path.join(project_root, 'src'))

from nex_ai.data_ingestion import fetch_token_pair_data
from nex_ai.signal_generation import generate_trading_signals
from nex_ai.models import train_price_prediction_model, predict_next_price
from nex_ai.utils import load_config

if __name__ == "__main__":
    print("--- NEX: Decentralized Crypto Intelligence Analysis Script ---")

    # 1. Load configuration (if any)
    # config = load_config("config/settings.py") # Uncomment if you create a settings.py

    # 2. Fetch Data from Dexscreener
    # Using the example from your provided JSON
    chain_id = "solana"
    token_address = "8NCievmJCg2d9Vc2TWgz2HkE6ANeSX7kwvdq5AL7pump" # BUNKER token address

    pair_data = fetch_token_pair_data(chain_id, token_address)

    if not pair_data:
        print("Could not fetch token pair data. Exiting analysis.")
        exit()

    current_price_usd = float(pair_data.get('priceUsd', '0'))
    price_change_h24 = pair_data.get('priceChange', {}).get('h24', 0.0)

    print(f"\nCurrent Price (USD) for {pair_data['baseToken']['symbol']}: {current_price_usd:.8f}")
    print(f"24-hour Price Change: {price_change_h24:.2f}%")

    # --- Using 'real' data from the response for signal generation ---
    # The Dexscreener API provides a snapshot, not a historical series.
    # To use the `generate_trading_signals` function, which requires a list of prices,
    # we will infer an approximate price 24 hours ago based on the current price
    # and the 24-hour price change, then simulate a linear progression of prices.
    # This allows us to demonstrate the signal generation with data derived from the API.

    if price_change_h24 != -100: # Avoid division by zero if price dropped to 0
        # Calculate the price 24 hours ago
        # current_price = original_price * (1 + price_change_percentage / 100)
        # original_price = current_price / (1 + price_change_percentage / 100)
        price_24h_ago = current_price_usd / (1 + price_change_h24 / 100)
    else:
        price_24h_ago = 0.0 # If it dropped 100%, assume it was 0 or very close

    num_simulated_points = 24 # One point per hour for the last 24 hours
    simulated_prices = []
    for i in range(num_simulated_points):
        # Linear interpolation between price_24h_ago and current_price_usd
        interpolated_price = price_24h_ago + (current_price_usd - price_24h_ago) * (i / (num_simulated_points - 1))
        simulated_prices.append(interpolated_price)

    print(f"\nSimulated Historical Prices (derived from 24h change, {num_simulated_points} points):")
    print([f"{p:.8f}" for p in simulated_prices]) # Format for cleaner output

    # 3. Generate Signals
    # Adjust window sizes based on the number of simulated points
    short_term_window = 8  # e.g., 8-hour SMA
    long_term_window = 16 # e.g., 16-hour SMA
    signals = generate_trading_signals(simulated_prices, short_term_window, long_term_window)

    print(f"\nGenerated Signals (Short SMA: {short_term_window}, Long SMA: {long_term_window}):")
    for i, signal in enumerate(signals):
        if signal:
            print(f"Point {i+1} (Simulated Price: {simulated_prices[i]:.8f}): {signal}")

    # 4. Train and use a model for price prediction
    print("\n--- Training Price Prediction Model ---")
    look_back_window = 5 # Use the last 5 prices to predict the next
    trained_model = train_price_prediction_model(simulated_prices, look_back=look_back_window)

    if trained_model:
        # Get the latest prices to make a prediction for the very next point
        latest_prices_for_prediction = simulated_prices[-look_back_window:]
        if len(latest_prices_for_prediction) == look_back_window:
            next_price_prediction = predict_next_price(trained_model, latest_prices_for_prediction)
            if next_price_prediction is not None:
                print(f"\nPredicted next price based on last {look_back_window} points: {next_price_prediction:.8f}")
            else:
                print("Could not make a prediction for the next price.")
        else:
            print(f"Not enough simulated data points ({len(simulated_prices)}) to form a prediction input of size {look_back_window}.")
    else:
        print("Model could not be trained due to insufficient data.")

    print("\n--- Analysis Complete ---")
