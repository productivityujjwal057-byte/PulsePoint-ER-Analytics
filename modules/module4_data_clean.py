import pandas as pd

# Load Dataset
df = pd.read_csv("data/er_data.csv")

print("FIRST 5 RECORDS")
print(df.head())

# Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Arrival Time
df["arrival_time"] = pd.to_datetime(df["arrival_time"], format="%H:%M")

# Extract Hour
df["hour"] = df["arrival_time"].dt.hour

print("\nDATASET SHAPE")
print(df.shape)

print("\nDATA CLEANING COMPLETED")