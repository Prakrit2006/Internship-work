import pandas as pd
import matplotlib.pyplot as plt


#Reading from CSV file and fixing null values
data=pd.read_csv('netflix_titles_duration_minutes.csv')
movies = data[data['type'] == 'Movie']
movies['duration'].describe()
data[['director', 'cast', 'country']] = data[['director', 'cast', 'country']].fillna('Unknown')
data['duration'] = data['duration'].fillna(data['duration'].median())


#Line graph for frequency of titles added per year
data['date_added'] = pd.to_datetime(data['date_added'].str.strip(), errors='coerce')
data['year_added'] = data['date_added'].dt.year
titles_per_year = data['year_added'].value_counts().sort_index()
titles_per_year.plot(kind='line', marker='o')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.title('Netflix Titles Added Per Year')
plt.show()


# Bar graph of movies vs shows
data['type'].value_counts().plot(kind='bar')
plt.xlabel('Type')
plt.ylabel('Number of Titles')
plt.title('No. of movies vs shows')
plt.show()



#Histogram of Duration
plt.hist(data['duration'].dropna(),bins=20)
plt.xlabel('Duration')
plt.ylabel('Number of Titles')
plt.title('Histogram of Duration')
plt.show()



#Top rating bar graph
data['rating'].value_counts().head(11).plot(kind='bar')
plt.title('Top Rating')
plt.show()


#Release year distribution
plt.hist(data['release_year'].dropna(),bins=20)
plt.xlabel('Release Date')
plt.ylabel('Number of Titles')
plt.title('Histogram of Release Date')
plt.show()



#Pie chart of movies vs shows
plt.pie(data['type'].value_counts(),labels=data['type'].unique())
plt.title('Piechart of Type of media on netflix')
plt.show()

#Scatter chart of rating vs release year
rating_map={
            rating:index
            for index,rating in enumerate(sorted(data['rating'].dropna().unique()))}
data['encoded_Rating']=data['rating'].map(rating_map)
plt.scatter(data['release_year'],data['encoded_Rating'])
plt.title("Release Year vs Encoded Rating")
plt.xlabel("Release Year")
plt.ylabel("Encoded Rating")
plt.yticks(list(rating_map.values()), list(rating_map.keys()))
plt.show()

#Heatmap
df=pd.read_csv("All_Pokemon.csv")
plt.figure(figsize=(10,10))
numeric_cols = ['HP', 'Att', 'Def', 'Spa', 'Spd', 'Spe', 'BST', 'Height', 'Weight']
corr = df[numeric_cols].corr()
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation')
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap of Pokémon Stats")
plt.tight_layout()
plt.show()

#Pie chart of legendary distribution
legendary_count = df['Legendary'].value_counts()
plt.pie(
    legendary_count,
    labels=['Non-Legendary', 'Legendary'],
    shadow=True)
plt.title("Distribution of Legendary and Non-Legendary Pokémon")
plt.show()

#Primary type Bar graph
type_count = df['Type 1'].value_counts(ascending=True)
plt.barh(type_count.index, type_count.values)
plt.title("Number of Pokémon by Primary Type")
plt.xlabel("Primary Type")
plt.ylabel("Number of Pokémon")
plt.show()
