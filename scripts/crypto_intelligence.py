def calculate_sma(prices, window):
  """
  Calculates the Simple Moving Average (SMA) for a given list of prices.

  Args:
      prices (list): A list of numerical prices.
      window (int): The number of periods to include in the moving average.

  Returns:
      list: A list of SMA values. The first (window - 1) values will be None.
  """
  sma_values = []
  for i in range(len(prices)):
      if i < window - 1:
          sma_values.append(None)  # Not enough data for the first few points
      else:
          # Calculate the sum of prices within the current window
          current_window_sum = sum(prices[i - window + 1 : i + 1])
          sma_values.append(current_window_sum / window)
  return sma_values

def generate_trading_signals(prices, short_window=10, long_window=30):
  """
  Generates basic buy/sell signals based on Simple Moving Average (SMA) crossovers.

  A 'buy' signal is generated when the short-term SMA crosses above the long-term SMA.
  A 'sell' signal is generated when the short-term SMA crosses below the long-term SMA.

  Args:
      prices (list): A list of historical cryptocurrency prices.
      short_window (int): The window size for the short-term SMA.
      long_window (int): The window size for the long-term SMA.

  Returns:
      list: A list of signals ('BUY', 'SELL', or None) corresponding to each price point.
  """
  if len(prices) < long_window:
      print("Not enough data to calculate long-term moving average.")
      return [None] * len(prices)

  short_sma = calculate_sma(prices, short_window)
  long_sma = calculate_sma(prices, long_window)

  signals = [None] * len(prices)

  for i in range(1, len(prices)):
      if short_sma[i] is not None and long_sma[i] is not None:
          # Check for crossover
          if short_sma[i-1] is not None and long_sma[i-1] is not None:
              # Buy signal: short SMA crosses above long SMA
              if short_sma[i] > long_sma[i] and short_sma[i-1] <= long_sma[i-1]:
                  signals[i] = 'BUY'
              # Sell signal: short SMA crosses below long SMA
              elif short_sma[i] < long_sma[i] and short_sma[i-1] >= long_sma[i-1]:
                  signals[i] = 'SELL'
  return signals

if __name__ == "__main__":
  # --- Mock Cryptocurrency Price Data ---
  # In a real application, you would fetch this data from a crypto exchange API.
  mock_crypto_prices = [
      100, 102, 105, 103, 108, 110, 109, 112, 115, 113,
      118, 120, 122, 125, 123, 128, 130, 129, 132, 135,
      133, 130, 128, 125, 122, 120, 118, 115, 112, 110,
      108, 105, 103, 100, 98, 95, 93, 90, 88, 85,
      87, 89, 92, 95, 98, 100, 103, 105, 108, 110,
      112, 115, 118, 120, 122, 125, 128, 130, 132, 135
  ]

  print("--- NEX: Decentralized Crypto Intelligence (Basic Signal Generation) ---")
  print(f"Mock Crypto Prices ({len(mock_crypto_prices)} data points):")
  print(mock_crypto_prices)
  print("\nCalculating trading signals...")

  # Define short and long window periods for SMAs
  short_term_window = 10
  long_term_window = 30

  # Generate signals
  signals = generate_trading_signals(mock_crypto_prices, short_term_window, long_term_window)

  print(f"\nGenerated Signals (Short SMA: {short_term_window}, Long SMA: {long_term_window}):")
  for i, signal in enumerate(signals):
      if signal:
          print(f"Day {i+1} (Price: {mock_crypto_prices[i]}): {signal}")

  print("\n--- End of Analysis ---")
  print("Note: In a real system, these signals would be fed into a trading bot or a dashboard.")
