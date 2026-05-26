from flask import Flask, jsonify
import pandas as pd

# Create Flask App
app = Flask(__name__)

# Load Dataset
df = pd.read_csv("data/er_data.csv")

# ==============================
# API 1 - ALL DATA
# ==============================

@app.route("/patients")

def patients():

    return jsonify(df.to_dict(orient="records"))

# ==============================
# API 2 - WAIT TIME
# ==============================

@app.route("/waittime")

def waittime():

    avg_wait = df["wait_time"].mean()

    return jsonify({
        "average_wait_time": round(avg_wait,2)
    })

# ==============================
# API 3 - CRITICAL PATIENTS
# ==============================

@app.route("/critical")

def critical():

    critical_cases = len(df[df["severity"] == "Critical"])

    return jsonify({
        "critical_patients": critical_cases
    })

# ==============================
# RUN SERVER
# ==============================

if __name__ == "__main__":

    app.run(debug=True)