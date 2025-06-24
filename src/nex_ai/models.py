"""
Module for defining, training, and evaluating machine learning models.
This could include:
- Price prediction models (e.g., LSTM, Transformer).
- Anomaly detection models.
- Classification models for market regimes.
"""
from sklearn.linear_model import LinearRegression
import numpy as np

def create_dataset(prices: list, look_back: int = 1) -> tuple[np.ndarray, np.ndarray]:
    """
    Transforms a time series of prices into a dataset suitable for supervised learning.
    Each sample (X) will be a sequence of 'look_back' previous prices,
    and the target (y) will be the next price in the sequence.

    Args:
        prices (list): A list of numerical prices.
        look_back (int): The number of previous time steps to use as input features.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple containing X (features) and y (targets).
    """
    X, y = [], []
    for i in range(len(prices) - look_back):
        feature_set = prices[i:(i + look_back)]
        target = prices[i + look_back]
        X.append(feature_set)
        y.append(target)
    return np.array(X), np.array(y)

def train_price_prediction_model(prices: list, look_back: int = 5):
    """
    Trains a simple linear regression model for price prediction.

    Args:
        prices (list): A list of historical prices.
        look_back (int): The number of previous prices to use as features for prediction.

    Returns:
        sklearn.linear_model.LinearRegression: The trained linear regression model.
    """
    print(f"Preparing data for model training with look_back={look_back}...")
    X, y = create_dataset(prices, look_back)

    if len(X) == 0:
        print("Not enough data to create a dataset for training. Need more prices than look_back.")
        return None

    print(f"Training linear regression model with {len(X)} samples...")
    model = LinearRegression()
    model.fit(X, y)
    print("Model training complete.")
    return model

def predict_next_price(model, latest_prices: list) -> float | None:
    """
    Uses the trained model to predict the next price.

    Args:
        model (sklearn.linear_model.LinearRegression): The trained model.
        latest_prices (list): A list of the most recent prices,
                              matching the 'look_back' window used during training.

    Returns:
        float | None: The predicted next price, or None if prediction is not possible.
    """
    if model is None:
        print("Model is not trained. Cannot make prediction.")
        return None
    if len(latest_prices) != model.n_features_in_:
        print(f"Error: 'latest_prices' length ({len(latest_prices)}) must match model's expected features ({model.n_features_in_}).")
        return None

    # Reshape for prediction (model expects 2D array: [[feature1, feature2, ...]])
    input_features = np.array(latest_prices).reshape(1, -1)
    prediction = model.predict(input_features)[0]
    return prediction
