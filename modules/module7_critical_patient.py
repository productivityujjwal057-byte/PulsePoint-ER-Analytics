import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Critical Patients
critical_cases = df[df["severity"] == "Critical"]

print("Total Critical Patients:", len(critical_cases))

# Department Wise Critical Cases
critical_department = critical_cases.groupby("department").size()

print("\nCritical Cases By Department")
print(critical_department)

# Chart
critical_department.plot(kind="bar")

plt.title("Critical Patient Trend Analysis")

plt.xlabel("Department")

plt.ylabel("Critical Patients")

plt.xticks(rotation=45)

plt.show()