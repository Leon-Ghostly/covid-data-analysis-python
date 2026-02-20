import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("\nFirst rows:")
print(df.head())

# Data cleaning
df = df.drop_duplicates()
df = df.dropna(subset=["Country_Region", "Confirmed"])

# Dataset info
print("\nDataset info:")
print(df.info())

# Statistics
print("\nStatistical summary:")
print(df.describe())

# Top 10 countries by confirmed cases
print("\nTop 10 countries by confirmed cases:")
top_countries = (
    df.groupby("Country_Region")["Confirmed"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_countries)

# Export cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nAnalysis completed.")
