from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pandas as pd
import os

app = Flask(__name__, template_folder="templates")
CORS(app)

# ==============================
# 🔹 Load Dataset (Inside Backend Folder)
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "METABRIC_RNA_Mutation.csv")

# Check if file exists
if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ Dataset not found at: {data_path}")

data = pd.read_csv(data_path)

required_columns = [
    "patient_id",
    "age_at_diagnosis",
    "tumor_size",
    "lymph_nodes_examined_positive",
    "neoplasm_histologic_grade"
]

data = data.dropna(subset=required_columns)
data["patient_id"] = data["patient_id"].astype(int)

print("✅ Dataset Loaded Successfully")
print("📊 Total Patients:", len(data))

# ==============================
# 🔹 Prediction Function
# ==============================

def predict_survival_clinical(data_input):
    age = float(data_input.get("age", 50))
    tumor = float(data_input.get("tumor_size", 1))
    nodes = float(data_input.get("lymph_nodes", 0))
    grade = float(data_input.get("grade", 1))

    # Clinical style risk logic
    if nodes >= 4 or grade == 3:
        risk_level = "High"
        survival_prob = 30
    elif nodes >= 1:
        risk_level = "Medium"
        survival_prob = 60
    else:
        risk_level = "Low"
        survival_prob = 85

    return {
        "survival_probability": survival_prob,
        "risk_level": risk_level
    }

# ==============================
# 🔹 Frontend Routes
# ==============================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict-page")
def predict_page():
    return render_template("predict.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# ==============================
# 🔹 API Routes
# ==============================

@app.route("/patients", methods=["GET"])
def get_patients():
    patient_ids = data["patient_id"].unique().tolist()

    # Optional: sort for clean dropdown
    patient_ids = sorted(patient_ids)

    return jsonify({"patients": patient_ids})

@app.route("/patient/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    patient = data[data["patient_id"] == patient_id]

    if patient.empty:
        return jsonify({"error": "Patient not found"}), 404

    patient = patient.iloc[0]

    return jsonify({
        "age": float(patient["age_at_diagnosis"]),
        "tumor_size": float(patient["tumor_size"]),
        "lymph_nodes": float(patient["lymph_nodes_examined_positive"]),
        "grade": float(patient["neoplasm_histologic_grade"])
    })

@app.route("/predict", methods=["POST"])
def predict():
    data_input = request.get_json()
    result = predict_survival_clinical(data_input)
    return jsonify(result)

# ==============================
# 🔹 Run App
# ==============================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)