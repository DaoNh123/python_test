import pandas as pd

# Tạo một DataFrame ví dụ
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Hanoi', 'Saigon', 'Danang']
})

# Ghi ra file Parquet
df.to_parquet('data.parquet', engine='pyarrow', index=False)

# Read parquet we've just written
df_loaded = pd.read_parquet('data.parquet', engine='pyarrow')
print(df_loaded)