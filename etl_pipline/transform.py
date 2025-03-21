import pandas as pd
import json

def transform_data(df):
    # Calculate total_sales
    df["TotalSales"] = df["QuantityOrdered"] * df["ItemPrice"]

    # Convert PromotionDiscount from JSON string to float
    df["PromotionDiscount"] = df["PromotionDiscount"].apply(lambda x: float(json.loads(x)["Amount"]))

    # Calculate net_sale
    df["NetSale"] = df["TotalSales"] - df["PromotionDiscount"]

    # Remove duplicates based on OrderId
    df = df.drop_duplicates(subset=["OrderId"])

    # Remove rows where NetSale is negative or zero
    df = df[df["NetSale"] > 0]

    print("✅ Data Transformed Successfully!")
    return df
