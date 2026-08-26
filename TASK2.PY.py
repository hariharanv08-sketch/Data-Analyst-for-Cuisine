import pandas as pd

df = pd.read_csv('zomato.csv', encoding='latin-1')

# Top 10 most common cuisine combinations
top_combos = df['Cuisines'].value_counts().head(10)
print("Top 10 Cuisine Combinations:")
print(top_combos)
# Average rating for each cuisine combination
combo_ratings = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nTop 10 Cuisine Combinations by Average Rating:")
print(combo_ratings.head(10))
