import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Ambulance Analytics
avg_ambulance = df["ambulance_time"].mean()

max_ambulance = df["ambulance_time"].max()

print("Average Ambulance Response Time:", round(avg_ambulance,2))

print("Maximum Ambulance Response Time:", max_ambulance)

# Department Wise Ambulance Time
ambulance_department = df.groupby("department")["ambulance_time"].mean()

# Chart
ambulance_department.plot(kind="bar")

plt.title("Ambulance Response Analytics")

plt.xlabel("Department")

plt.ylabel("Response Time")

plt.xticks(rotation=45)

plt.show()