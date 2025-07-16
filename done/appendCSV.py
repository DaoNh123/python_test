# import pandas as pd
#
# # Dữ liệu cần thêm
# data = {
#     'name': ['nam', 'Elite'],
#     'branch':['BU', 'BA'],
#     'year':[4, 3],
#     'cgpa': [8.8, 9.0]
# }
# df = pd.DataFrame(data)
#
# # Append vào file data.csv
# df.to_csv('university_records.csv', mode='a', header=False, index=False)

import pandas as pd
import os

file_path = 'data.csv'

df = pd.DataFrame({
    'Name': ['Charlie'],
    'Age': [35]
})

# Ghi header nếu file chưa tồn tại
df.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)