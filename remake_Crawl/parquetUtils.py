import pandas as pd
import pyarrow.dataset as ds
import pyarrow as pa
import pyarrow.parquet as pq
import time
import os

# def dict_to_parquet_file (dict_data, target_parquet_path):
#     df = pd.DataFrame(dict_data)
#     df.to_parquet(target_parquet_path, engine="pyarrow", index=False)
#
# def read_parquet_file (target_parquet_path):
#     df_loaded = pd.read_parquet(target_parquet_path, engine="pyarrow")
#     print(df_loaded)


def append_parquet_batch(data_dict, out_dir='parquet_data'):
    """
    Ghi một batch dữ liệu dạng columnar hoặc rowar vào dataset Parquet theo format part-{timestamp}-{i:03d}.parquet
    """

    # Tạo thư mục nếu chưa có
    os.makedirs(out_dir, exist_ok=True)

    # Tạo DataFrame
    df = pd.DataFrame(data_dict)

    # Convert sang Arrow Table
    table = pa.Table.from_pandas(df)

    # Tạo timestamp để phân biệt batch
    timestamp = int(time.time() * 1000)
    filename_template = f"part-{timestamp}-{{i}}.parquet"

    # Ghi dữ liệu vào thư mục Parquet (append kiểu phân vùng file)
    pq.write_to_dataset(
        table,
        root_path=out_dir,
        basename_template=filename_template
    )

    # Đổi tên file `{i}` thành `{i:03d}`
    for fname in os.listdir(out_dir):
        if fname.startswith(f"part-{timestamp}-") and fname.endswith(".parquet"):
            i_str = fname.split('-')[-1].replace('.parquet', '')
            try:
                i_int = int(i_str)
                new_name = f"part-{timestamp}-{i_int:03d}.parquet"
                os.rename(os.path.join(out_dir, fname), os.path.join(out_dir, new_name))
            except ValueError:
                continue

    print(f"[✅] Ghi {len(df)} bản ghi vào {out_dir}/ với prefix: part-{timestamp}-...")

def read_parquet_batch(out_dir='parquet_data'):
    # Tạo dataset từ thư mục
    dataset = ds.dataset("parquet_data", format="parquet")

    # Convert toàn bộ thành DataFrame
    table = dataset.to_table()
    df = table.to_pandas().sort_values("updated_at").drop_duplicates("title", keep='last')

    print(f"Đọc {len(df)} bản ghi")
    print(df.head(10).T)
