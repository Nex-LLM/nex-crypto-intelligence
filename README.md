
# NEX: Decentralized Crypto Intelligence

![enter image description here](https://olive-chemical-haddock-701.mypinata.cloud/ipfs/bafybeihvlxl57innrcqwo43s7sf2sgsluorazbgrpcfwyvzziib5mx4tfa)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%200.24%2B-orange?logo=scikit-learn&logoColor=white)
![Product Hunt](https://img.shields.io/badge/Product%20Hunt-%23DA552F?logo=producthunt&logoColor=white)

## Project Overview

  

NEX is an AI-powered platform designed to provide decentralized crypto intelligence. It aims to analyze various data sources, including real-time market data from public APIs, on-chain metrics, and potentially social sentiment, to generate actionable insights and signals for the cryptocurrency market. This project serves as the foundational codebase for building sophisticated analytical tools and potentially automated strategies.

  

## Features

  

*  **Data Ingestion:** Fetches real-time token pair data from the Dexscreener API.

*  **Signal Generation:** Algorithms for identifying potential trading opportunities or market trends using simulated historical price data derived from API snapshots.

*  **Machine Learning Models:** Framework for developing and deploying predictive or classification models for price forecasting.

*  **Modular Design:** A clear separation of concerns for easy development and maintenance.

  

## Project Structure

  

```

nex-ai-project/

├── README.md
├── requirements.txt
├── setup.py
├── src/
│ └── nex_ai/
│ ├── __init__.py
│ ├── data_ingestion.py
│ ├── signal_generation.py
│ ├── models.py
│ └── utils.py
├── scripts/
│ ├── crypto_intelligence.py
│ └── run_analysis.py
├── tests/
│ ├── __init__.py
│ └── test_signal_generation.py
└── config/
└── settings.py

```

  

### Directory Breakdown:

  

*  **`README.md`**: This file. Provides an overview of the project, setup instructions, and usage.

*  **`requirements.txt`**: Lists all Python dependencies required to run the project (e.g., `requests`, `scikit-learn`).

*  **`setup.py`**: Configuration file for installing the `nex_ai` package in editable mode, crucial for local development.

*  **`src/`**: Contains the core source code of the NEX AI application.

*  **`nex_ai/`**: The main Python package for the project.

*  **`__init__.py`**: Makes `nex_ai` a Python package.

*  **`data_ingestion.py`**: Handles fetching current token pair data from the Dexscreener API and initial processing.

*  **`signal_generation.py`**: Contains the logic for generating trading signals (e.g., moving average crossovers) using a simulated historical price series.

*  **`models.py`**: Houses definitions and training/inference logic for machine learning models (e.g., linear regression for price prediction).

*  **`utils.py`**: A collection of utility functions and helper classes used across the project.

*  **`scripts/`**: Contains standalone executable scripts for various tasks.

*  **`crypto_intelligence.py`**: The initial script for basic signal generation.

*  **`run_analysis.py`**: A script to demonstrate how to fetch data, generate signals, and train/predict with a model using the `nex_ai` package. Includes `sys.path` modification for easier execution.

*  **`tests/`**: Contains unit and integration tests for the codebase to ensure reliability.

*  **`config/`**: Stores configuration files (e.g., API keys, database connection strings, model parameters).

*  **`settings.py`**: Example configuration file.

  

## Installation and Setup

  

1.  **Clone the repository:**
```
    bash
    git clone <your-repository-url>
    cd nex-ai-project
```



  

2.  **Create a virtual environment (recommended):**
```
    bash
    python3 -m venv venv
    source venv/bin/activate # On Windows: `venv\Scripts\activate`
```

3.  **Install dependencies:**
```
    bash
    pip install -r requirements.txt
    pip install -e . # Install your project in editable mode
```
  

4.  **Configure environment variables (if applicable):**
```
    For sensitive information like API keys, create a `.env` file in the root directory (or set system-wide environment variables).
```

# Example .env content

DEXSCREENER_API_KEY=your_api_key_here # (Currently not required by Dexscreener public API)

## Usage

  

To run a basic crypto intelligence analysis using live data from Dexscreener:
```
    bash
    python scripts/run_analysis.py
```
  

This script will:

* Fetch current price and change data for a specified token (e.g., BUNKER on Solana) from Dexscreener.

* Infer a simulated 24-hour historical price series based on the current price and 24-hour price change.

* Generate basic trading signals (buy/sell) using moving average crossovers on this simulated data.

* Train a simple linear regression model to predict the next price based on the simulated history.

  

Refer to the individual script files in `scripts/` and modules in `src/nex_ai/` for more specific usage examples and functionalities.

  

## Contributing

  

Contributions are welcome! Please refer to the `CONTRIBUTING.md` (if available) for guidelines on how to contribute to this project.

  

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
- [Website](https://nex-chain.tech)
- [Twitter](https://x.com/use_nex)