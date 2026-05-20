import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Convert Time
df["arrival_time"] = pd.to_datetime(df["arrival_time"], format="%H:%M")

# Extract Hour
df["hour"] = df["arrival_time"].dt.hour

# Hourly Patient Count
hourly_patients = df.groupby("hour").size()

# Forecast
predicted_hour = hourly_patients.idxmax()

predicted_patients = hourly_patients.max()

print("Predicted Peak Hour:", predicted_hour)

print("Expected Patients:", predicted_patients)

# Forecast Chart
hourly_patients.plot(kind="line", marker="o")

plt.title("Patient Surge Forecast")

plt.xlabel("Hour")

plt.ylabel("Patient Count")

plt.grid(True)

plt.show()