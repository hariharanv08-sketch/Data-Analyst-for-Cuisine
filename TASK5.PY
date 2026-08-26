import pandas as pd

df = pd.read_csv('zomato.csv', encoding='latin-1')

# Restaurant with highest votes
highest_votes = df.loc[df['Votes'].idxmax(), ['Restaurant Name', 'Votes', 'Aggregate rating']]
print("Restaurant with Highest Votes:")
print(highest_votes)

# Restaurant with lowest votes
lowest_votes = df.loc[df['Votes'].idxmin(), ['Restaurant Name', 'Votes', 'Aggregate rating']]
print("\nRestaurant with Lowest Votes:")
print(lowest_votes)

# Correlation between votes and rating
correlation = df['Votes'].corr(df['Aggregate rating'])
print(f"\nCorrelation between Votes and Rating: {correlation:.3f}")
