ETL Pipeline for Sales Data Processing
Project Overview
This project is an ETL (Extract, Transform, Load) pipeline that processes sales data from two different regions, applies business rules, and loads the cleaned data into an SQLite database.

Additionally, SQL queries and Python functions are provided for data validation.

📂 Project Structure
graphql
Copy
Edit
├── etl_pipeline/  
│   ├── extract.py        # Extracts data from CSV files  
│   ├── transform.py      # Transforms data (applies business rules)  
│   ├── load.py           # Loads transformed data into SQLite  
│   ├── validate.py       # Validates data using SQL queries  
│   ├── config.py         # Database configuration  
├── data/                 # Folder containing CSV files  
│   ├── order_region_a.csv  
│   ├── order_region_b.csv  
├── main.py               # Runs the ETL pipeline  
├── README.md             # Documentation  
├── requirements.txt      # Python dependencies  
🚀 How to Run the Project Locally
Follow these steps to run the project on your local machine:

1️⃣ Clone the Repository
bash
Copy
Edit
git clone <repository_url>
cd <repository_name>
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate the environment:

Windows:
bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure Database
The database is set up in config.py:

python
Copy
Edit
DATABASE_PATH = "sales_data.db"
5️⃣ Place CSV Files
Ensure the CSV files (order_region_a.csv and order_region_b.csv) are placed inside the /data/ folder.

6️⃣ Run the ETL Pipeline

python main.py
----------------------------------------
Extract data from CSV files
Transform data by applying business rules
Load data into the SQLite database
Validate the data using SQL queries
------------------------------------------

🔍 Validation Queries
After running the pipeline, we can manually validate data by executing SQL queries.
--------------------------------------------------------------------------------------------
Count total records
---------------SELECT COUNT(*) FROM sales_data;
Total sales amount by region
----------------SELECT Region, SUM(TotalSales) FROM sales_data GROUP BY Region;
Average sales per transaction
----------------SELECT AVG(TotalSales) FROM sales_data;
Check for duplicate OrderId values
---------------------SELECT OrderId, COUNT(*) FROM sales_data GROUP BY OrderId HAVING COUNT(*) > 1;
📜 Business Rules Applied
Combine data from both CSV files into a single table.
Calculate total_sales as QuantityOrdered * ItemPrice.
Add a region column to identify the data source (A or B).
Remove duplicate OrderId values to ensure data integrity.
Calculate net_sale as total_sales - PromotionDiscount.
Exclude invalid records where net_sale is negative or zero.
