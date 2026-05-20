import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# Triage Function
def triage(severity):
    if severity == "Critical":
        return "Red"
    elif severity == "High":
        return "Yellow"
    else:
        return "Green"

# Create Triage Category
df["triage_category"] = df["severity"].apply(triage)

# Count Categories
triage_count = df["triage_category"].value_counts()

print("Triage Monitoring")
print(triage_count)

# Pie Chart
triage_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Triage Category Distribution")

plt.ylabel("")

plt.show()