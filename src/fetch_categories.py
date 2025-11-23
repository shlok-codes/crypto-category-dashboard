import os
import requests
import pandas as pd
from datetime import date

# 🔑 ENTER YOUR API KEY HERE
COINGECKO_API_KEY = "CG-VMU73FATgEZ45F5A8ZaNL9LN"

BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_categories():
    url = f"{BASE_URL}/coins/categories"
    headers = {
        "x-cg-demo-api-key": COINGECKO_API_KEY
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data)
    df["snapshot_date"] = date.today()
    return df

def main():
    df = fetch_categories()

    columns_to_keep = [
        "snapshot_date",
        "id",
        "name",
        "market_cap",
        "market_cap_change_24h",
        "volume_24h"
    ]

    columns_to_keep = [c for c in columns_to_keep if c in df.columns]
    df = df[columns_to_keep]

    os.makedirs("../data", exist_ok=True)
    output_path = "../data/crypto_categories_snapshot.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved CSV to {output_path}")

if __name__ == "__main__":
    main()
