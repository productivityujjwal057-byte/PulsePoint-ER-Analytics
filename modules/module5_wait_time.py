import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Analytics
avg_wait = df["wait_time"].mean()

max_wait = df["wait_time"].max()

min_wait = df["wait_time"].min()

print("Average Wait Time:", round(avg_wait,2))
print("Maximum Wait Time:", max_wait)
print("Minimum Wait Time:", min_wait)

# Department Wise Wait Time
department_wait = df.groupby("department")["wait_time"].mean()

print("\nDepartment Wise Wait Time")
print(department_wait)

# Chart
department_wait.plot(kind="bar")

plt.title("Department Wise Average Wait Time")

plt.xlabel("Department")

plt.ylabel("Average Wait Time")

plt.xticks(rotation=45)

plt.show()