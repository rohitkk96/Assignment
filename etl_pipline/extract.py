import pandas as pd
import os
from etl_pipline.config import CSV_FOLDER_PATH

def extract_data():
    # Read CSV files from 'data' folder
    region_a_file = os.path.join(CSV_FOLDER_PATH, "order_region_a.csv")
    region_b_file = os.path.join(CSV_FOLDER_PATH, "order_region_b.csv")

    df_region_a = pd.read_csv(region_a_file)
    df_region_b = pd.read_csv(region_b_file)

    # Add region identifier
    df_region_a["Region"] = "A"
    df_region_b["Region"] = "B"

    # Combine both datasets
    df_combined = pd.concat([df_region_a, df_region_b], ignore_index=True)
    
    print("✅ Data Extracted Successfully!")
    return df_combined

