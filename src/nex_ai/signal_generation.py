"""
Module for generating trading signals and insights.
This includes various technical analysis indicators and custom algorithms.
"""

def calculate_sma(prices: list, window: int) -> list:
  """
  Calculates the Simple Moving Average (SMA) for a given list of prices.
  """
  sma_values = []
  for i in range(len(prices)):
      if i < window - 1: # Corrected from &lt;
          sma_values.append(None)
      else:
          current_window_sum = sum(prices[i - window + 1 : i + 1])
          sma_values.append(current_window_sum / window)
  return sma_values

def generate_trading_signals(prices: list, short_window: int = 10, long_window: int = 30) -> list:
  """
  Generates basic buy/sell signals based on Simple Moving Average (SMA) crossovers.
  """
  if len(prices) < long_window: # Corrected from &lt;
      print("Not enough data to calculate long-term moving average.")
      return [None] * len(prices)

  short_sma = calculate_sma(prices, short_window)
  long_sma = calculate_sma(prices, long_window)

  signals = [None] * len(prices)

  for i in range(1, len(prices)):
      if short_sma[i] is not None and long_sma[i] is not None:
          if short_sma[i-1] is not None and long_sma[i-1] is not None:
              if short_sma[i] > long_sma[i] and short_sma[i-1] <= long_sma[i-1]: # Corrected from &lt;=
                  signals[i] = 'BUY'
              elif short_sma[i] < long_sma[i] and short_sma[i-1] >= long_sma[i-1]: # Corrected from &lt; and >=
                  signals[i] = 'SELL'
  return signals

# You can add more signal generation functions here, e.g.,
# def calculate_rsi(prices: list, period: int = 14) -> list:
#     """Calculates the Relative Strength Index (RSI)."""
#     pass
