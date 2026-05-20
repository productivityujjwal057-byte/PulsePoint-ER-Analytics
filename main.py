import pandas as pd

# Load dataset
df = pd.read_csv("data/er_data.csv")

# Show first rows
print("FIRST 5 RECORDS")
print(df.head())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert arrival time into datetime
df["arrival_time"] = pd.to_datetime(df["arrival_time"], format="%H:%M")

# Extract hour
df["hour"] = df["arrival_time"].dt.hour

# Dataset shape
print("\nDATASET SIZE")
print(df.shape)

print("\nDATA CLEANING COMPLETED")




print("\nWAIT TIME ANALYTICS")

avg_wait = df["wait_time"].mean()
max_wait = df["wait_time"].max()
min_wait = df["wait_time"].min()

print("Average Wait Time:", round(avg_wait, 2))
print("Maximum Wait Time:", max_wait)
print("Minimum Wait Time:", min_wait)

# Department-wise wait time
department_wait = df.groupby("department")["wait_time"].mean()

print("\nDEPARTMENT WISE WAIT TIME")
print(department_wait)




import matplotlib.pyplot as plt

department_wait.plot(kind="bar")

plt.title("Department Wise Average Wait Time")
plt.xlabel("Department")
plt.ylabel("Average Wait Time")

plt.xticks(rotation=45)

plt.show()




# MODULE 6 - PEAK TRAFFIC ANALYSIS

print("\nPEAK TRAFFIC ANALYSIS")

peak_hour = df.groupby("hour").size()

print(peak_hour)

busy_hour = peak_hour.idxmax()

print("\nBUSIEST HOUR:", busy_hour)


peak_hour.plot(kind="line", marker="o")

plt.title("ER Peak Traffic Hours")
plt.xlabel("Hour")
plt.ylabel("Number of Patients")

plt.grid(True)

plt.show()