# import pyarrow.parquet as pa
#
# if __name__ == '__main__':
#     table = pa.read_table('weather.2016.parquet')
#     print(table.shape)  # (194697, 15)
#     df = table.to_pandas()
#
#     print(df.head().T)


# Example 2:
# import pandas as pd
#
# df = pd.read_parquet('weather.2016.parquet')
# print(df.head().T)

# import pandas as pd
#
# df = pd.read_parquet('weather.2016.parquet', filters=[('Country', '=', 'ENGLAND')])
# # df = pd.read_parquet('weather.2016.parquet')
# print(df.head().T)
#
# grouped = df.groupby(['Country']).mean(numeric_only=True)
# # Taking tanspose so the printing dataset will easy.
# print(grouped.T)

# import pandas as pd
#
# df = pd.read_parquet('weather.2016.parquet',
#                      filters=[('Country', '=', 'ENGLAND'),
#                               ('WindSpeed','<', 7)])
# # Taking tanspose so the printing dataset will easy.
# print(df.head().T)