import pandas as pd

parquet_file_path = 'parquet/file/path'
df = pd.read_parquet(parquet_file_path)

# Save DataFrame to a CSV file
csv_output_path = 'location/to/store/CSV'
df.to_csv(csv_output_path, index=False)