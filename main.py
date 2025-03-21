from etl_pipline.extract import extract_data
from etl_pipline.transform import transform_data
from etl_pipline.load_data import load_data
from etl_pipline.validate import run_validations

def run_pipeline():
    # Step 1: Extract Data
    df = extract_data()

    # Step 2: Transform Data
    transformed_df = transform_data(df)

    # Step 3: Load Data
    load_data(transformed_df)

    # Step 4: Validate Data
    run_validations()

if __name__ == "__main__":
    run_pipeline()
