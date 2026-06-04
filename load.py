import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    url = (
        f"postgresql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )
    return create_engine(url)

def load(df):
    engine = get_engine()
    df.to_sql(
        "itunes_tracks",
        engine,
        if_exists="append",
        index=False
    )
    print(f"Successfully loaded {len(df)} rows into itunes_tracks table")

if __name__ == "__main__":
    from extract import extract_tracks
    from transform import transform
    raw = extract_tracks()
    df = transform(raw)
    load(df)