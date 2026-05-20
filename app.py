import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/er_data.csv")

# Convert time
df["arrival_time"] = pd.to_datetime(df["arrival_time"], format="%H:%M")
df["hour"] = df["arrival_time"].dt.hour

st.title("Emergency Room Analytics Dashboard")

# Dataset
st.subheader("ER Dataset")
st.write(df)

# KPIs
avg_wait = df["wait_time"].mean()
max_wait = df["wait_time"].max()

st.metric("Average Wait Time", round(avg_wait,2))
st.metric("Maximum Wait Time", max_wait)

# Department Wait Analysis
department_wait = df.groupby("department")["wait_time"].mean()

fig1, ax1 = plt.subplots()

department_wait.plot(kind="bar", ax=ax1)

plt.xticks(rotation=45)

st.subheader("Department Wise Wait Time")

st.pyplot(fig1)

# Peak Traffic
peak_hour = df.groupby("hour").size()

fig2, ax2 = plt.subplots()

peak_hour.plot(kind="line", marker="o", ax=ax2)

st.subheader("Peak Traffic Hours")

st.pyplot(fig2)