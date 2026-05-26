import pandas as pd
import sqlite3

print("\n========== FINAL ER ANALYTICS PROJECT ==========")

# ==============================
# LOAD DATA
# ==============================

df = pd.read_csv("data/er_data.csv")

print("\nDataset Loaded Successfully")

# ==============================
# DATABASE CONNECTION
# ==============================

conn = sqlite3.connect("database/hospital_er.db")

df.to_sql("er_visits", conn, if_exists="replace", index=False)

print("Database Connected Successfully")

# ==============================
# KPI CALCULATIONS
# ==============================

avg_wait = df["wait_time"].mean()

avg_ambulance = df["ambulance_time"].mean()

critical_cases = len(df[df["severity"] == "Critical"])

total_patients = len(df)

print("\n========== FINAL KPIs ==========")

print(f"Total Patients: {total_patients}")

print(f"Average Wait Time: {round(avg_wait,2)} mins")

print(f"Average Ambulance Response Time: {round(avg_ambulance,2)} mins")

print(f"Critical Patients: {critical_cases}")

# ==============================
# FORECASTING
# ==============================

df["arrival_time"] = pd.to_datetime(df["arrival_time"], format="%H:%M")

df["hour"] = df["arrival_time"].dt.hour

peak_hour = df.groupby("hour").size()

predicted_hour = peak_hour.idxmax()

print(f"\nPredicted Peak Traffic Hour: {predicted_hour}:00")

# ==============================
# SQL REPORT
# ==============================

query = """
SELECT department,
AVG(wait_time) as avg_wait
FROM er_visits
GROUP BY department
"""

report = pd.read_sql(query, conn)

print("\nDepartment Wise Wait Time Report")

print(report)

# ==============================
# FINAL STATUS
# ==============================

print("\nEmergency Room Analytics Dashboard Completed Successfully")

conn.close()
