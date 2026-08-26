import pandas as pd

df = pd.read_csv('zomato.csv', encoding='latin-1')

# Find restaurant names that appear more than once (chains)
chain_counts = df['Restaurant Name'].value_counts()
chains = chain_counts[chain_counts > 1]
print("Top 10 Restaurant Chains (by number of outlets):")
print(chains.head(10))

# Average rating and votes for top restaurant chains
top_chain_names = chains.head(10).index
chain_data = df[df['Restaurant Name'].isin(top_chain_names)]

chain_stats = chain_data.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',
    'Votes': 'sum'
}).sort_values('Aggregate rating', ascending=False)

print("\nRating & Votes for Top 10 Chains:")
print(chain_stats)
