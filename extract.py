import requests
from datetime import datetime

# iTunes Search API - 100% free, no API key needed
SEARCH_TERM = "hindi"  # change to any genre, artist, or language
LIMIT = 50

def extract_tracks():
    url = "https://itunes.apple.com/search"
    params = {
        "term": SEARCH_TERM,
        "media": "music",
        "entity": "song",
        "country": "IN",
        "limit": LIMIT
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["results"]

if __name__ == "__main__":
    tracks = extract_tracks()
    print(f"Extracted {len(tracks)} tracks")
    print("First track:", tracks[0]["trackName"])
    print("Artist      :", tracks[0]["artistName"])
    print("Genre       :", tracks[0]["primaryGenreName"])
    print("Price       :", tracks[0]["trackPrice"])
