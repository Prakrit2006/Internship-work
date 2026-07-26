import pandas as pd
#Reading from a CSV file
data=pd.read_csv("Iris.csv",index_col="Id")
print(data)
#Print first 10 rows
print(data.head(10))
#Dataset info
print(data.info())
#Select column
print(data["Species"])
#To print the whole column instead of truncated
print(data["Species"].to_string())
#Filter rows
print("Filtering data according to petal length")
min_petal_length=float(input("Enter the minimum petal length: "))
max_petal_length=float(input("Enter the maximum petal length: "))
print(data[(data["PetalLengthCm"]>min_petal_length) & (data["PetalLengthCm"]<=max_petal_length)])