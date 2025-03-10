import requests
import json
from web3 import Web3

# Load your blockchain explorer API key
from config import ETHERSCAN_API_KEY

ETHERSCAN_URL = "https://api.etherscan.io/api"

# Connect to Ethereum blockchain
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Function to fetch whale transactions
def get_whale_transactions(token_address):
    params = {
        "module": "account",
        "action": "tokentx",
        "contractaddress": token_address,
        "page": 1,
        "offset": 10,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }
    response = requests.get(ETHERSCAN_URL, params=params)
    data = response.json()

    if data["status"] == "1":
        transactions = data["result"]
        for tx in transactions:
            print(f"Whale Alert 🚨: {tx['from']} → {tx['to']} | {int(tx['value']) / 10**18} tokens")
    else:
        print("No transactions found.")

# Example usage
TOKEN_ADDRESS = "0xD533a949740bb3306d119CC777fa900bA034cd52"  # CRV Token Example
get_whale_transactions(TOKEN_ADDRESS)
