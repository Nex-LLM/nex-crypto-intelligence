import requests
import time
import datetime

"""
Module for data ingestion and initial processing.
This would include functions to:
- Fetch current token pair data from Dexscreener.
- Handle API rate limits and errors.
"""

def fetch_token_pair_data(chain_id: str, token_address: str) -> dict | None:
    """
    Fetches current token pair data from the Dexscreener API.

    Args:
        chain_id (str): The blockchain ID (e.g., 'solana', 'ethereum').
        token_address (str): The address of the base token.

    Returns:
        dict | None: A dictionary containing the token pair data, or None if fetching fails.
    """
    print(f"Fetching token pair data for chain '{chain_id}' and token '{token_address}' from Dexscreener API...")
    url = f"https://api.dexscreener.com/tokens/v1/{chain_id}/{token_address}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json() # This 'data' variable is now a list, e.g., [{...}]

        # The API returns a list of pair dictionaries.
        # We expect the first item in this list to be the pair data we want.
        if not isinstance(data, list) or not data:
            print(f"API response is not a list or is empty for {token_address} on {chain_id}.")
            return None

        pair_info = data[0] # Get the first dictionary from the list

        # Now, check if this dictionary contains the 'pairs' key, or if it's the pair itself
        # Based on your example, the list directly contains the pair dictionary, not a 'pairs' key within it.
        # So, we directly use pair_info.
        if not pair_info:
            print(f"No pair data found in the first item of the response for {token_address} on {chain_id}.")
            return None

        print(f"Successfully fetched data for pair: {pair_info.get('baseToken', {}).get('symbol')} / {pair_info.get('quoteToken', {}).get('symbol')}")
        return pair_info # Return the pair dictionary

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred during the request: {req_err}")
    except ValueError as json_err:
        print(f"Error decoding JSON response: {json_err}")
        print(f"Response content: {response.text}")
    except IndexError:
        print(f"API response list was empty for {token_address} on {chain_id}.")
    return None

def process_raw_data(raw_data: dict) -> dict:
    """
    Performs initial cleaning and structuring of raw data.
    (Placeholder implementation)
    """
    print("Processing raw data...")
    return raw_data # For now, just return as is
