import pandas as pd

df = pd.read_csv("data/er_data.csv")

print(df.head())

avg_wait = df["wait_time"].mean()

print("Average Wait Time:", avg_wait)