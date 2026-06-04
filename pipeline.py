import schedule
import time
from datetime import datetime
from extract import extract_tracks
from transform import transform
from load import load

def run_pipeline():
    print("="*50)
    print(f"Pipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)

    # Step 1 - Extract
    print("\n[1/3] Extracting tracks from iTunes API...")
    raw = extract_tracks()
    print(f"      Done — {len(raw)} raw tracks fetched")

    # Step 2 - Transform
    print("\n[2/3] Transforming data with Pandas...")
    df = transform(raw)
    print(f"      Done — {len(df)} clean rows ready")

    # Step 3 - Load
    print("\n[3/3] Loading data into itunes_db...")
    load(df)

    print("\n" + "="*50)
    print(f"Pipeline complete at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)

# Run once immediately
run_pipeline()

# Then schedule to run every day at 8am
schedule.every().day.at("08:00").do(run_pipeline)
print("\nScheduler running... pipeline will auto-run daily at 8:00 AM")
print("Press Ctrl+C to stop\n")

while True:
    schedule.run_pending()
    time.sleep(60)