import pandas as pd
from datetime import datetime

def transform(raw_tracks):
    records = []

    for track in raw_tracks:
        records.append({
            "track_name"   : track.get("trackName", "Unknown"),
            "artist"       : track.get("artistName", "Unknown"),
            "album"        : track.get("collectionName", "Unknown"),
            "genre"        : track.get("primaryGenreName", "Unknown"),
            "duration_min" : round(track.get("trackTimeMillis", 0) / 60000, 2),
            "price"        : track.get("trackPrice", 0.0),
            "release_year" : track.get("releaseDate", "2000-01-01")[:4],
            "country"      : track.get("country", "Unknown"),
            "fetched_at"   : datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    df = pd.DataFrame(records)

    # Clean the data
    df = df.dropna()
    df = df.drop_duplicates(subset=["track_name", "artist"])
    df = df[df["duration_min"] > 0]
    df = df[df["track_name"] != "Unknown"]

    return df

if __name__ == "__main__":
    from extract import extract_tracks
    raw = extract_tracks()
    df = transform(raw)
    print(f"Clean rows : {len(df)}")
    print(f"Columns    : {list(df.columns)}")
    print("\nSample data:")
    print(df[["track_name", "artist", "genre", "duration_min"]].head())