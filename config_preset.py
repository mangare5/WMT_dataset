import pandas as pd

# parquet = '/home/mag/PycharmProjects/WMT_dataset/dataset/parquet'
#
# for f in parquet:
parquet_file_path = '/home/mag/PycharmProjects/WMT_dataset/dataset/parquet/validation/0000.parquet'
df = pd.read_parquet(parquet_file_path)

# Save DataFrame to a CSV file
csv_output_path = '/home/mag/PycharmProjects/WMT_dataset/dataset/wmt19_fr-de_validation.csv'
df.to_csv(csv_output_path, index=False)
