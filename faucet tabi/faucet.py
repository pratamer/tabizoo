import requests
import time
import random

# Load proxies from a text file
def load_proxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Proxy configuration
proxies_list = load_proxies('proxy.txt')

# Headers
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://faucet.testnet.tabichain.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://faucet.testnet.tabichain.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# Data payload
data = {
    "address": "0x5xxxx"
}

# URL
url = 'https://faucet-api.testnet.tabichain.com/api/faucet'

# Infinite loop to continuously make requests
while True:
    try:
        # Get a random proxy
        proxy = random.choice(proxies_list)
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        response = requests.post(url, headers=headers, json=data, proxies=proxies)
        response_json = response.json()
        if response_json.get("success"):
            print("You Got 0.1 TABI")
        else:
            print(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Wait for a while before making the next request
    time.sleep(1)  # Adjust the sleep time as needed