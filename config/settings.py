"""
Configuration settings for the NEX AI project.
This file can store non-sensitive configurations or provide defaults.
Sensitive information like API keys should be handled via environment variables.
"""

# Example API endpoints
CRYPTO_API_BASE_URL = "https://api.examplecryptoexchange.com"
BLOCKCHAIN_EXPLORER_API_URL = "https://api.exampleblockchainexplorer.com"

# Data fetching settings
DEFAULT_FETCH_LIMIT = 1000
DEFAULT_TIME_INTERVAL = "1h" # 1 hour

# Signal generation parameters
DEFAULT_SHORT_SMA_WINDOW = 10
DEFAULT_LONG_SMA_WINDOW = 30

# Model training parameters
MODEL_EPOCHS = 50
MODEL_BATCH_SIZE = 32
