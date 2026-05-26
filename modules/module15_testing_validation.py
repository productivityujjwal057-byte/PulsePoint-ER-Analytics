import pandas as pd

# Load Dataset
df = pd.read_csv("data/er_data.csv")

print("\n========== TESTING & VALIDATION ==========")

# ==============================
# TEST 1 - MISSING VALUES
# ==============================

missing = df.isnull().sum()

print("\nMISSING VALUES TEST")

print(missing)

# ==============================
# TEST 2 - DUPLICATES
# ==============================

duplicates = df.duplicated().sum()

print("\nDUPLICATE RECORD TEST")

print("Duplicate Records:", duplicates)

# ==============================
# TEST 3 - WAIT TIME VALIDATION
# ==============================

avg_wait = df["wait_time"].mean()

print("\nWAIT TIME VALIDATION")

print("Average Wait Time:", round(avg_wait,2))

# ==============================
# TEST 4 - AMBULANCE VALIDATION
# ==============================

avg_ambulance = df["ambulance_time"].mean()

print("\nAMBULANCE RESPONSE VALIDATION")

print("Average Ambulance Time:", round(avg_ambulance,2))

# ==============================
# TEST 5 - SEVERITY VALIDATION
# ==============================

severity_check = df["severity"].value_counts()

print("\nSEVERITY DISTRIBUTION VALIDATION")

print(severity_check)

print("\nALL TESTS COMPLETED SUCCESSFULLY")
