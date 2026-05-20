import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Convert Time
df["arrival_time"] = pd.to_datetime(df["arrival_time"], format="%H:%M")

# Extract Hour
df["hour"] = df["arrival_time"].dt.hour

# Peak Traffic
peak_hour = df.groupby("hour").size()

print("Peak Traffic Analysis")
print(peak_hour)

busy_hour = peak_hour.idxmax()

print("\nBusiest Hour:", busy_hour)

# Chart
peak_hour.plot(kind="line", marker="o")

plt.title("ER Peak Traffic Hours")

plt.xlabel("Hour")

plt.ylabel("Number of Patients")

plt.grid(True)

plt.show()