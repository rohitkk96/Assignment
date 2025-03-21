import sqlite3
from etl_pipline.config import DATABASE_PATH

def load_data(df):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        OrderId TEXT PRIMARY KEY,
        OrderItemId TEXT,
        QuantityOrdered INTEGER,
        ItemPrice REAL,
        PromotionDiscount REAL,
        TotalSales REAL,
        NetSale REAL,
        Region TEXT
    )
    """)

    # Insert data
    df.to_sql("sales_data", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()
    print("✅ Data Loaded into Database Successfully!")
