# iTunes ETL Pipeline 

An end-to-end ETL (Extract, Transform, Load) data pipeline that automatically fetches music data from the iTunes API, cleans it using Pandas, and stores it in a PostgreSQL database — scheduled to run daily.

---

##  Architecture
iTunes API → extract.py → transform.py → load.py → PostgreSQL (itunes_db) → pipeline.py (orchestrator + scheduler)


---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data cleaning & transformation |
| iTunes Search API | Free music data source |
| PostgreSQL | Data storage |
| SQLAlchemy | Database connection |
| Schedule | Daily automation |
| Git & GitHub | Version control |

---

##  Project Structure
itunes-etl-pipeline/
│
├── extract.py        → Fetches raw track data from iTunes API
├── transform.py      → Cleans and structures data using Pandas
├── load.py           → Loads clean data into PostgreSQL
├── pipeline.py       → Orchestrates all steps + daily scheduler
├── .env.example      → Template for environment variables
├── requirements.txt  → All Python dependencies
└── README.md         → Project documentation

---

## 🔄 What the Pipeline Does

1. **Extract** — Calls iTunes Search API and fetches 50 tracks (Bollywood/Hindi music, India market)
2. **Transform** — Cleans raw JSON data:
   - Removes null values
   - Drops duplicate tracks
   - Converts duration from milliseconds to minutes
   - Adds timestamp of when data was fetched
3. **Load** — Pushes 49 clean rows into PostgreSQL `itunes_tracks` table
4. **Schedule** — Runs automatically every day at 8:00 AM

---

## 🚀 How to Run

**1. Clone the repository**
git clone https://github.com/Pankajkm13/itunes-etl-pipeline.git
cd itunes-etl-pipeline

**2. Create virtual environment**
python -m venv venv
venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Setup environment variables**
cp .env.example .env
Fill in your PostgreSQL credentials in .env

**5. Run the pipeline**
python pipeline.py

---

## 🔧 Setup Requirements

- Python 3.10+
- PostgreSQL 15+
- iTunes API (free, no API key needed)

---

## 👨‍💻 Author
**Pankaj Kumar**  
[LinkedIn](https://Linkedin.com/in/Pankajkm13) | [GitHub](https://github.com/Pankajkm13)