import os
import requests

URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
RAW_FILE = os.path.join(RAW_DIR, "nbaallelo.csv")


def download():
    os.makedirs(RAW_DIR, exist_ok=True)
    response = requests.get(URL, timeout=30)
    response.raise_for_status()
    with open(RAW_FILE, "wb") as f:
        f.write(response.content)
    print(f"Fichier telecharge : {RAW_FILE} ({len(response.content)} octets)")


if __name__ == "__main__":
    download()
