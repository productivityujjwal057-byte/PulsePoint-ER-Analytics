import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# ==============================
# KPI CALCULATIONS
# ==============================

avg_wait = df["wait_time"].mean()

max_wait = df["wait_time"].max()

avg_ambulance = df["ambulance_time"].mean()

critical_patients = len(df[df["severity"] == "Critical"])

total_patients = len(df)

print("\n========== ER KPI DASHBOARD ==========")

print(f"Total Patients: {total_patients}")

print(f"Average Wait Time: {round(avg_wait,2)} mins")

print(f"Maximum Wait Time: {max_wait} mins")

print(f"Average Ambulance Time: {round(avg_ambulance,2)} mins")

print(f"Critical Patients: {critical_patients}")

# ==============================
# WAIT TIME CHART
# ==============================

department_wait = df.groupby("department")["wait_time"].mean()

department_wait.plot(kind="bar")

plt.title("Department Wise Wait Time")

plt.xlabel("Department")

plt.ylabel("Average Wait Time")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ==============================
# SEVERITY DISTRIBUTION
# ==============================

severity_count = df["severity"].value_counts()

severity_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Patient Severity Distribution")

plt.ylabel("")

plt.show()