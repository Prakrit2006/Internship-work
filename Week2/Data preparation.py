import pandas as pd

Data=pd.read_csv("netflix_titles_duration_minutes.csv")

# #Detecting null values
print(Data.isnull().sum())
# Fill missing values
Data['director']=Data['director'].fillna("Director not known")
Data[['date_added','rating']]=Data[['date_added','rating']].fillna("N/A")
Data['duration'] = Data['duration'].fillna(0)
print("After fillna\n",Data.isnull().sum())
#Rename Columns
Data=Data.rename(columns={"title":"Title"})
#Removing Duplicates
Data= Data.drop_duplicates(subset=['Title'])
#Converting Data types
Data=Data.astype({'duration':float})
