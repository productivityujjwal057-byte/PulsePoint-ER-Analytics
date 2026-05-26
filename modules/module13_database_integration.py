import pandas as pd
import sqlite3

# ==============================
# DATABASE CONNECTION
# ==============================

conn = sqlite3.connect("database/hospital_er.db")

print("Hospital ER Database Connected")

# ==============================
# LOAD DATASET
# ==============================

df = pd.read_csv("data/er_data.csv")

# ==============================
# STORE DATA
# ==============================

df.to_sql("er_visits", conn, if_exists="replace", index=False)

print("ER Dataset Stored Successfully")

# ==============================
# VERIFY DATA
# ==============================

query = "SELECT * FROM er_visits LIMIT 10"

result = pd.read_sql(query, conn)

print("\nFIRST 10 RECORDS FROM DATABASE")

print(result)

# ==============================
# TOTAL RECORDS
# ==============================

count_query = "SELECT COUNT(*) as total_patients FROM er_visits"

count_result = pd.read_sql(count_query, conn)

print("\nTOTAL PATIENT RECORDS")

print(count_result)

# Close Database
conn.close()

print("\nDATABASE INTEGRATION COMPLETED")
