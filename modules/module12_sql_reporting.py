import pandas as pd
import sqlite3

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Create Database Connection
conn = sqlite3.connect("database/hospital_er.db")

# Store Dataset into SQL Table
df.to_sql("er_visits", conn, if_exists="replace", index=False)

print("Database Connected Successfully")

# ==============================
# SQL QUERY 1
# Average Wait Time By Department
# ==============================

query1 = """
SELECT department,
AVG(wait_time) AS average_wait_time
FROM er_visits
GROUP BY department
"""

result1 = pd.read_sql(query1, conn)

print("\nAVERAGE WAIT TIME REPORT")
print(result1)

# ==============================
# SQL QUERY 2
# Critical Cases Count
# ==============================

query2 = """
SELECT severity,
COUNT(*) AS total_cases
FROM er_visits
GROUP BY severity
"""

result2 = pd.read_sql(query2, conn)

print("\nSEVERITY REPORT")
print(result2)

# ==============================
# SQL QUERY 3
# Ambulance Analytics
# ==============================

query3 = """
SELECT department,
AVG(ambulance_time) AS avg_response_time
FROM er_visits
GROUP BY department
"""

result3 = pd.read_sql(query3, conn)

print("\nAMBULANCE RESPONSE REPORT")
print(result3)

# Close Connection
conn.close()

print("\nSQL REPORTING COMPLETED")
