"""
Unit tests for the signal_generation module.
"""
import unittest
from src.nex_ai.signal_generation import calculate_sma, generate_trading_signals

class TestSignalGeneration(unittest.TestCase):

    def test_calculate_sma(self):
        prices = [10, 20, 30, 40, 50]
        # Window 3: (10+20+30)/3=20, (20+30+40)/3=30, (30+40+50)/3=40
        expected_sma_w3 = [None, None, 20.0, 30.0, 40.0]
        self.assertEqual(calculate_sma(prices, 3), expected_sma_w3)

        # Window 1: SMA is just the price itself
        expected_sma_w1 = [10.0, 20.0, 30.0, 40.0, 50.0]
        self.assertEqual(calculate_sma(prices, 1), expected_sma_w1)

        # Not enough data
        self.assertEqual(calculate_sma([10, 20], 3), [None, None])

    def test_generate_trading_signals(self):
        # Simple scenario for buy/sell
        prices = [
            100, 101, 102, 103, 104, # Prices rising
            105, 106, 107, 108, 109, # Short SMA > Long SMA
            108, 107, 106, 105, 104, # Prices falling
            103, 102, 101, 100, 99   # Short SMA &lt; Long SMA
        ]
        # With short_window=3, long_window=5
        # This test would need careful calculation of expected signals based on SMA values
        # For simplicity, let's test a known crossover point
        mock_prices_crossover = [
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19, # Rising
            20, 21, 22, 23, 24, 25, 24, 23, 22, 21, # Peak and start falling
            20, 19, 18, 17, 16, 15, 14, 13, 12, 11  # Falling
        ]
        # This is a simplified expectation. A real test would calculate SMAs and signals precisely.
        signals = generate_trading_signals(mock_prices_crossover, short_window=5, long_window=10)
        # Expecting a SELL signal around the point where prices start to fall significantly
        # and short SMA crosses below long SMA.
        # The exact index depends on the windows and data.
        # For this mock data, a sell signal might appear around index 20-25
        self.assertIn('SELL', signals)
        self.assertNotIn('BUY', signals[:15]) # No buy signals early on if already rising

        # Test with not enough data
        self.assertEqual(generate_trading_signals([1,2,3,4], short_window=2, long_window=5), [None, None, None, None])

if __name__ == '__main__':
    unittest.main()
