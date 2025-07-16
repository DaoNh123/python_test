import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import time
import os

# Dữ liệu mới (vd: batch mới đến hằng ngày)
df_new = pd.DataFrame({
    'name': ['Alice2'],
    'age': [32],
    'city': ['Hanoi']
})

# Convert sang Arrow Table
table = pa.Table.from_pandas(df_new)

# Create timestamp for name
timestamp = int(time.time() * 1000)  # ms
filename = f"part-{timestamp}-{{i}}.parquet"

# Append bằng cách ghi thêm file mới vào thư mục dataset
pq.write_to_dataset(
    table,
    root_path='parquet_data',
    basename_template=filename
)

# 🔃 Rename file để format {i} = 3 chữ số
for fname in os.listdir('parquet_data'):
    if fname.startswith(f"part-{timestamp}-") and fname.endswith(".parquet"):
        # Tách số i
        i_str = fname.split('-')[-1].replace('.parquet', '')
        i_int = int(i_str)
        new_name = f"part-{timestamp}-{i_int:03d}.parquet"
        os.rename(f"parquet_data/{fname}", f"parquet_data/{new_name}")

#  Read all file parquet từ "parquet_data
if __name__ == '__main__':
    dataset = pq.ParquetDataset('parquet_data')
    table = dataset.read()
    df_all = table.to_pandas()
    print(df_all)