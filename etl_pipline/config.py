import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Project root
DATABASE_PATH = os.path.join(BASE_DIR, "..", "sales_data.db")  # SQLite database file
CSV_FOLDER_PATH = os.path.join(BASE_DIR, "..", "data")  # CSV files location
