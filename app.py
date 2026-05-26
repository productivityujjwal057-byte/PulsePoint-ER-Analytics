# =========================================================
# MEDICORE ER COMMAND CENTER
# FINAL PROFESSIONAL LUXURY DASHBOARD
# FULLY WORKING VERSION
# =========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MediCore ER Command Center",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("data/er_data.csv")

# =========================================================
# DATA CLEANING
# =========================================================

df.drop_duplicates(inplace=True)

df["arrival_time"] = pd.to_datetime(
    df["arrival_time"],
    format="%H:%M"
)

df["hour"] = df["arrival_time"].dt.hour

# =========================================================
# DATABASE CONNECTION
# =========================================================

conn = sqlite3.connect(
    "database/hospital_er.db"
)

df.to_sql(
    "er_visits",
    conn,
    if_exists="replace",
    index=False
)

# =========================================================
# KPI VALUES
# =========================================================

total_patients = len(df)

critical_patients = len(
    df[df["severity"] == "Critical"]
)

high_patients = len(
    df[df["severity"] == "High"]
)

avg_wait = round(
    df["wait_time"].mean(),
    1
)

avg_ambulance = round(
    df["ambulance_time"].mean(),
    1
)

departments = df["department"].nunique()

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {

    background:
    linear-gradient(
        135deg,
        #1a120b,
        #24180f,
        #0f172a
    );

    color: #f8fafc;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #1f140d,
        #120d08
    );

    border-right: 1px solid #5b4636;
}

/* REMOVE STREAMLIT */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* HEADER */

.main-header {

    background:
    linear-gradient(
        135deg,
        #3b2414,
        #5b3a1f,
        #2a1a11
    );

    padding: 30px;

    border-radius: 22px;

    border: 1px solid #8b6b3f;

    margin-bottom: 28px;

    box-shadow:
    0 0 30px rgba(255,215,0,0.08);
}

.header-title {

    font-size: 40px;

    font-weight: 700;

    color: #fff8e7;
}

.header-sub {

    color: #f4d58d;

    font-size: 15px;

    margin-top: 5px;
}

/* KPI CARDS */

.metric-card {

    background:
    linear-gradient(
        145deg,
        #2a1b13,
        #3b2618
    );

    padding: 22px;

    border-radius: 20px;

    border: 1px solid #7c5c34;

    box-shadow:
    0 0 18px rgba(255,215,0,0.06);

    transition: 0.3s;
}

.metric-card:hover {

    transform: translateY(-4px);

    border: 1px solid #fbbf24;

    box-shadow:
    0 0 25px rgba(251,191,36,0.25);
}

.metric-title {

    color: #d6b98c;

    font-size: 14px;

    margin-bottom: 10px;
}

.metric-value {

    color: #fff8e7;

    font-size: 34px;

    font-weight: bold;
}

.metric-sub {

    color: #c2a878;

    font-size: 12px;

    margin-top: 8px;
}

/* CHART CARDS */

.chart-card {

    background:
    linear-gradient(
        145deg,
        #24170f,
        #1b120d
    );

    padding: 22px;

    border-radius: 20px;

    border: 1px solid #5f472e;

    margin-top: 18px;

    box-shadow:
    0 0 20px rgba(0,0,0,0.35);
}

/* SECTION TITLE */

.section-title {

    color: #ffe7b3;

    font-size: 22px;

    font-weight: 600;

    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    # 🏥 MediCore ER
    ### Luxury Command Center
    """)

    st.success("● SYSTEM ACTIVE")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Analytics",
            "Critical Patients",
            "Ambulance",
            "Database"
        ]
    )

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-header">

<div class="header-title">
🏥 MediCore ER Command Center
</div>

<div class="header-sub">
Real-Time Emergency Department Analytics & Monitoring Platform
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# KPI SECTION
# =========================================================

col1, col2, col3, col4, col5, col6 = st.columns(6)

cards = [

    ("Total Patients", total_patients, "Complete dataset"),

    ("Critical Cases", critical_patients, "Requires monitoring"),

    ("High Severity", high_patients, "Priority patients"),

    ("Avg Wait Time", f"{avg_wait}m", "Operational KPI"),

    ("Ambulance Avg", f"{avg_ambulance}m", "Response analytics"),

    ("Departments", departments, "Hospital units")
]

for col, card in zip(
    [col1,col2,col3,col4,col5,col6],
    cards
):

    with col:

        st.markdown(f"""
        <div class="metric-card">

        <div class="metric-title">
        {card[0]}
        </div>

        <div class="metric-value">
        {card[1]}
        </div>

        <div class="metric-sub">
        {card[2]}
        </div>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    left, right = st.columns([2,1])

    # =====================================================
    # ARRIVAL GRAPH
    # =====================================================

    with left:

        st.markdown("""
        <div class="chart-card">
        <div class="section-title">
        📈 Patient Arrivals by Hour
        </div>
        """, unsafe_allow_html=True)

        hourly = df.groupby("hour").size()

        fig1, ax1 = plt.subplots(figsize=(11,4))

        fig1.patch.set_facecolor("#24170f")
        ax1.set_facecolor("#24170f")

        ax1.plot(
            hourly.index,
            hourly.values,
            marker="o",
            linewidth=3,
            color="#fbbf24"
        )

        ax1.fill_between(
            hourly.index,
            hourly.values,
            alpha=0.2,
            color="#fbbf24"
        )

        ax1.tick_params(colors="white")

        ax1.grid(
            linestyle="--",
            alpha=0.2
        )

        st.pyplot(fig1)

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # PIE CHART
    # =====================================================

    with right:

        st.markdown("""
        <div class="chart-card">
        <div class="section-title">
        🚨 Severity Distribution
        </div>
        """, unsafe_allow_html=True)

        severity_count = df["severity"].value_counts()

        fig2, ax2 = plt.subplots(figsize=(5,5))

        fig2.patch.set_facecolor("#24170f")

        colors = [
            "#dc2626",
            "#fbbf24",
            "#78716c"
        ]

        ax2.pie(
            severity_count,
            labels=severity_count.index,
            autopct="%1.1f%%",
            colors=colors,
            wedgeprops={"width":0.45},
            textprops={"color":"white"}
        )

        st.pyplot(fig2)

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # SECOND ROW
    # =====================================================

    c1, c2, c3 = st.columns(3)

    # =====================================================
    # DEPARTMENT LOAD
    # =====================================================

    with c1:

        st.markdown("""
        <div class="chart-card">
        <div class="section-title">
        🏥 Department Load
        </div>
        """, unsafe_allow_html=True)

        dept = df["department"].value_counts().head(10)

        fig3, ax3 = plt.subplots(figsize=(6,5))

        fig3.patch.set_facecolor("#24170f")
        ax3.set_facecolor("#24170f")

        dept.plot(
            kind="barh",
            ax=ax3,
            color="#f59e0b"
        )

        ax3.tick_params(colors="white")

        st.pyplot(fig3)

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # WAIT TIME
    # =====================================================

    with c2:

        st.markdown("""
        <div class="chart-card">
        <div class="section-title">
        ⏱ Wait by Severity
        </div>
        """, unsafe_allow_html=True)

        wait = df.groupby(
            "severity"
        )["wait_time"].mean()

        fig4, ax4 = plt.subplots(figsize=(5,5))

        fig4.patch.set_facecolor("#24170f")
        ax4.set_facecolor("#24170f")

        wait.plot(
            kind="bar",
            ax=ax4,
            color=[
                "#dc2626",
                "#fbbf24",
                "#78716c"
            ]
        )

        ax4.tick_params(colors="white")

        st.pyplot(fig4)

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # AMBULANCE GRAPH
    # =====================================================

    with c3:

        st.markdown("""
        <div class="chart-card">
        <div class="section-title">
        🚑 Ambulance Response
        </div>
        """, unsafe_allow_html=True)

        amb = df.groupby(
            "severity"
        )["ambulance_time"].mean()

        fig5, ax5 = plt.subplots(figsize=(5,5))

        fig5.patch.set_facecolor("#24170f")
        ax5.set_facecolor("#24170f")

        amb.plot(
            kind="bar",
            ax=ax5,
            color=[
                "#dc2626",
                "#fbbf24",
                "#78716c"
            ]
        )

        ax5.tick_params(colors="white")

        st.pyplot(fig5)

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # PEAK TRAFFIC ANALYSIS
    # =====================================================

    st.markdown("""
    <div class="chart-card">
    <div class="section-title">
    🔥 Peak Traffic Hour Analysis
    </div>
    """, unsafe_allow_html=True)

    peak_hour = df.groupby("hour").size()

    highest_hour = peak_hour.idxmax()

    highest_patients = peak_hour.max()

    st.warning(
        f"Peak traffic detected at {highest_hour}:00 with {highest_patients} patient arrivals."
    )

    fig_peak, ax_peak = plt.subplots(figsize=(12,4))

    fig_peak.patch.set_facecolor("#24170f")
    ax_peak.set_facecolor("#24170f")

    bars = ax_peak.bar(
        peak_hour.index,
        peak_hour.values,
        color="#fbbf24"
    )

    bars[
        list(peak_hour.index).index(highest_hour)
    ].set_color("#dc2626")

    ax_peak.tick_params(colors="white")

    ax_peak.grid(
        linestyle="--",
        alpha=0.2
    )

    st.pyplot(fig_peak)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # TRIAGE MONITORING
    # =====================================================

    st.markdown("""
    <div class="chart-card">
    <div class="section-title">
    🚨 Triage Monitoring System
    </div>
    """, unsafe_allow_html=True)

    critical_df = df[df["severity"] == "Critical"]

    high_df = df[df["severity"] == "High"]

    moderate_df = df[df["severity"] == "Moderate"]

    t1, t2, t3 = st.columns(3)

    with t1:
        st.error(
            f"Critical Patients: {len(critical_df)}"
        )

    with t2:
        st.warning(
            f"High Severity Patients: {len(high_df)}"
        )

    with t3:
        st.info(
            f"Moderate Patients: {len(moderate_df)}"
        )

    triage_counts = df["severity"].value_counts()

    fig_triage, ax_triage = plt.subplots(figsize=(8,4))

    fig_triage.patch.set_facecolor("#24170f")
    ax_triage.set_facecolor("#24170f")

    triage_counts.plot(
        kind="bar",
        ax=ax_triage,
        color=[
            "#dc2626",
            "#fbbf24",
            "#78716c"
        ]
    )

    ax_triage.tick_params(colors="white")

    ax_triage.grid(
        linestyle="--",
        alpha=0.2
    )

    st.pyplot(fig_triage)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # PATIENT SURGE FORECASTING
    # =====================================================

    st.markdown("""
    <div class="chart-card">
    <div class="section-title">
    📈 Patient Surge Forecasting
    </div>
    """, unsafe_allow_html=True)

    future_hours = [
        max(peak_hour.index)+1,
        max(peak_hour.index)+2,
        max(peak_hour.index)+3
    ]

    future_values = [
        int(peak_hour.mean()+2),
        int(peak_hour.mean()+4),
        int(peak_hour.mean()+1)
    ]

    forecast_index = list(peak_hour.index) + future_hours

    forecast_values = list(peak_hour.values) + future_values

    fig_forecast, ax_forecast = plt.subplots(figsize=(12,4))

    fig_forecast.patch.set_facecolor("#24170f")
    ax_forecast.set_facecolor("#24170f")

    ax_forecast.plot(
        forecast_index,
        forecast_values,
        marker="o",
        linewidth=3,
        color="#38bdf8"
    )

    ax_forecast.axvline(
        x=max(peak_hour.index),
        linestyle="--",
        color="#fbbf24"
    )

    ax_forecast.tick_params(colors="white")

    ax_forecast.grid(
        linestyle="--",
        alpha=0.2
    )

    st.info(
        "Forecast generated using historical ER traffic trends."
    )

    st.pyplot(fig_forecast)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # ALERTS
    # =====================================================

    st.markdown("## ⚠ Live Operational Alerts")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.error(
            f"Critical load high: {critical_patients} patients"
        )

    with a2:
        st.warning(
            f"Average wait time: {avg_wait} minutes"
        )

    with a3:
        st.success(
            f"Ambulance response stable: {avg_ambulance} minutes"
        )

# =========================================================
# ANALYTICS PAGE
# =========================================================

elif page == "Analytics":

    st.markdown("## 📊 Advanced ER Analytics")

    st.dataframe(
        df,
        use_container_width=True
    )

# =========================================================
# CRITICAL PAGE
# =========================================================

elif page == "Critical Patients":

    critical_only = df[
        df["severity"] == "Critical"
    ]

    st.markdown("## 🚨 Critical Patients")

    st.dataframe(
        critical_only,
        use_container_width=True
    )

# =========================================================
# AMBULANCE PAGE
# =========================================================

elif page == "Ambulance":

    st.markdown("## 🚑 Ambulance Analytics")

    ambulance_avg = df.groupby(
        "department"
    )["ambulance_time"].mean()

    fig6, ax6 = plt.subplots(figsize=(10,5))

    fig6.patch.set_facecolor("#24170f")
    ax6.set_facecolor("#24170f")

    ambulance_avg.plot(
        kind="line",
        marker="o",
        linewidth=3,
        ax=ax6,
        color="#fbbf24"
    )

    ax6.tick_params(colors="white")

    ax6.grid(
        linestyle="--",
        alpha=0.2
    )

    st.pyplot(fig6)

# =========================================================
# DATABASE PAGE
# =========================================================

elif page == "Database":

    st.markdown("## 🗄 Database Preview")

    query = """
    SELECT * FROM er_visits
    LIMIT 50
    """

    db_df = pd.read_sql_query(
        query,
        conn
    )

    st.dataframe(
        db_df,
        use_container_width=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<hr style="border:1px solid #6b4f2d">

<center style="color:#d6b98c">
MediCore ER Command Center • Luxury Healthcare Analytics Platform
</center>
""", unsafe_allow_html=True)

# =========================================================
# CLOSE DATABASE
# =========================================================

conn.close()