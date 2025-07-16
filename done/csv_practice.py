# import csv

# data = [
#     # ['Name', 'Branch', 'Year', 'CGPA'],
#     # ['Nikhil', 'COE', 2, 9.0],
#     # ['Sanchit', 'COE', 2, 9.1],
#     # ['Aditya', 'IT', 2, 9.3],
#     # ['Sagar', 'SE', 1, 9.5],
#     ['Prateek', 'MCE', 3, 7.8],
#     ['Sahil', 'EP', 2, 9.1]
# ]
#
# with open('students.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE,
#                         delimiter='|', quotechar='"', escapechar='\\')
#     writer.writerows(data)


# Read .csv File
# import csv
# from student import Student
#
#
# if __name__ == '__main__':
    # filename = "university_records.csv"
    #
    # data = []
    # with open(filename, mode='r') as csvfile:
    #     csvFile = csv.reader(csvfile)
    #     for line in csvFile:
    #         data.append(line)
    #
    # print(data)
    # students = []
    # list_dict = [];
    # for line in data[1:]:
    #     list_dict.append(dict(zip(data[0], line)))
    #     students.append(Student(line[0], line[1], line[2], line[3]))
    #
    # for student in students:
    #     print(student)

    # for dict in list_dict:
    #     print(dict)

    # filename = "university_records.csv"
    #
    # with open(filename, mode='r') as csvfile:
    #     csvFile = csv.DictReader(csvfile)
    #     for line in csvFile:
    #         print(line)


# import pandas
# csvFile = pandas.read_csv('university_records.csv', index_col=0)
# print(csvFile)

# import pandas as pd
#
# # Sample data stored in a multi-line string
# data = """totalbill_tip, sex:smoker, day_time, size
# 16.99, 1.01:Female|No, Sun, Dinner, 2
# 10.34, 1.66, Male, No|Sun:Dinner, 3
# 21.01:3.5_Male, No:Sun, Dinner, 3
# 23.68, 3.31, Male|No, Sun_Dinner, 2
# 24.59:3.61, Female_No, Sun, Dinner, 4
# 25.29, 4.71|Male, No:Sun, Dinner, 4"""
#
# # Save the data to a CSV file
# with open("sample.csv", "w") as file:
#     file.write(data)
# print(data)

# import pandas as pd
#
# df = pd.read_csv('sample.csv', nrows=3)
# print(df)

# df = pd.read_csv('sample.csv',
#                  sep='[:, |_]',  # Define the delimiters
#                  engine='python')  # Use Python engine for regex separators
# print(df)
# import pandas as pd
#
# df= pd.read_csv("sample.csv")
# print("Previous Dataset: ")
# print(df)
# # using skiprows
# df = pd.read_csv("sample.csv", skiprows = [4,5])
# print("Dataset After skipping rows: ")
# print(df)

import pandas as pd
from datetime import datetime
df = pd.read_csv("people.csv", parse_dates=["Date of birth"])

# Ngày hiện tại
today = pd.Timestamp(datetime.today().date())

# Tính tuổi
df["Age"] = df["Date of birth"].apply(
    lambda dob: today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
)

# In kết quả
print(df)

data = df.to_dict(orient="records")

for item in data:
    print(item)

names = df["Name"].tolist()  # ["Alice", "Bob"]
print(names)

oldest = df.loc[df["Age"].idxmax()]
print(oldest["Name"], oldest["Age"])  # VD: Bob 39