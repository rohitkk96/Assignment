import sqlite3
from etl_pipline.config import DATABASE_PATH

def count_total_records():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sales_data")
    total_records = cursor.fetchone()[0]
    conn.close()
    print(f"✅ Total number of records: {total_records}")
    return total_records

def total_sales_by_region():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT Region, SUM(TotalSales) FROM sales_data GROUP BY Region")
    results = cursor.fetchall()
    conn.close()
    
    print("✅ Total Sales by Region:")
    for row in results:
        print(f"Region: {row[0]}, Total Sales: {row[1]}")
    return results

def avg_sales_per_transaction():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(TotalSales) FROM sales_data")
    avg_sales = cursor.fetchone()[0]
    conn.close()
    print(f"✅ Average Sales per Transaction: {avg_sales}")
    return avg_sales

def check_duplicate_order_ids():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT OrderId, COUNT(*) FROM sales_data GROUP BY OrderId HAVING COUNT(*) > 1")
    duplicates = cursor.fetchall()
    conn.close()
    
    if duplicates:
        print("⚠️ Duplicate Order IDs Found:")
        for row in duplicates:
            print(f"OrderId: {row[0]}, Count: {row[1]}")
    else:
        print("✅ No duplicate Order IDs found.")
    return duplicates

def run_validations():
    print("\n🔍 Running Data Validations...")
    count_total_records()
    total_sales_by_region()
    avg_sales_per_transaction()
    check_duplicate_order_ids()

if __name__ == "__main__":
    run_validations()
