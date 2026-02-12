const form = document.getElementById("predictForm");
const resultDiv = document.getElementById("result");
const probabilityValue = document.getElementById("probabilityValue");
const riskFill = document.getElementById("riskFill");
const riskLabel = document.getElementById("riskLabel");

let survivalChart = null;
let featureChart = null;

/* ================================
   LOAD PATIENT IDS FROM DATASET
================================ */
window.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch("http://127.0.0.1:5000/patients");
        const data = await response.json();

        const dropdown = document.getElementById("patient_id");
        dropdown.innerHTML = '<option value="">-- Select Patient --</option>';

        data.patients.forEach(id => {
            const option = document.createElement("option");
            option.value = id;
            option.textContent = id;
            dropdown.appendChild(option);
        });

    } catch (error) {
        console.error("Error loading patient IDs:", error);
    }
});


/* ================================
   AUTO-FILL WHEN PATIENT SELECTED
================================ */
document.getElementById("patient_id").addEventListener("change", async function () {

    const patientId = this.value;
    if (!patientId) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/patient/${patientId}`);
        const data = await response.json();

        if (!data.error) {
            document.getElementById("age").value = data.age;
            document.getElementById("tumor_size").value = data.tumor_size;
            document.getElementById("lymph_nodes").value = data.lymph_nodes;
            document.getElementById("grade").value = data.grade;
        } else {
            alert("Patient not found");
        }

    } catch (error) {
        alert("Error fetching patient data");
        console.error(error);
    }
});


/* ================================
   PREDICTION
================================ */
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const payload = {
        age: Number(document.getElementById("age").value),
        tumor_size: Number(document.getElementById("tumor_size").value),
        lymph_nodes: Number(document.getElementById("lymph_nodes").value),
        grade: Number(document.getElementById("grade").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        console.log("🔥 Backend response:", data);

        if (!data.error && data.survival_probability !== undefined) {

            resultDiv.style.display = "block";

            const survival = Number(data.survival_probability);
            const risk = 100 - survival;

            probabilityValue.textContent = survival + "%";

            /* ===== Risk Bar (REAL PERCENTAGE) ===== */
            riskFill.style.width = risk + "%";

            if (data.risk_level === "Low") {
                riskFill.style.background = "#2ecc71";
                riskLabel.textContent = "Low Risk";
                riskLabel.style.color = "#2ecc71";
            }
            else if (data.risk_level === "Medium") {
                riskFill.style.background = "#f1c40f";
                riskLabel.textContent = "Medium Risk";
                riskLabel.style.color = "#f1c40f";
            }
            else if (data.risk_level === "High") {
                riskFill.style.background = "#e74c3c";
                riskLabel.textContent = "High Risk";
                riskLabel.style.color = "#e74c3c";
            }

            /* ===== Survival vs Risk Chart ===== */
            if (survivalChart) survivalChart.destroy();
            survivalChart = new Chart(
                document.getElementById("survivalChart"),
                {
                    type: "bar",
                    data: {
                        labels: ["Survival Probability", "Risk Probability"],
                        datasets: [{
                            data: [survival, risk],
                            backgroundColor: ["#2ecc71", "#e74c3c"],
                            borderRadius: 8
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: { beginAtZero: true, max: 100 }
                        },
                        plugins: {
                            legend: { display: false }
                        }
                    }
                }
            );

            /* ===== Feature Importance Chart ===== */
            if (featureChart) featureChart.destroy();
            featureChart = new Chart(
                document.getElementById("featureChart"),
                {
                    type: "bar",
                    data: {
                        labels: ["Age", "Tumor Size", "Lymph Nodes", "Grade"],
                        datasets: [{
                            label: "Importance",
                            data: data.feature_importance || [0.30, 0.40, 0.20, 0.10],
                            backgroundColor: "#78A1BB",
                            borderRadius: 6
                        }]
                    },
                    options: {
                        indexAxis: "y",
                        responsive: true,
                        plugins: { legend: { display: false } },
                        scales: { x: { beginAtZero: true } }
                    }
                }
            );

        } else {
            alert("Error from backend: " + (data.error || "Invalid response"));
        }

    } catch (error) {
        alert("Backend not reachable. Make sure Flask is running.");
        console.error(error);
    }
});


/* ================================
   PDF DOWNLOAD (FIXED BUG)
================================ */
function downloadPDF() {

    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF();

    const patientId = document.getElementById("patient_id").value;
    const age = document.getElementById("age").value;
    const tumor = document.getElementById("tumor_size").value;
    const nodes = document.getElementById("lymph_nodes").value;
    const grade = document.getElementById("grade").value;

    pdf.setFontSize(16);
    pdf.text("Breast Cancer Survival Prediction Report", 20, 20);

    pdf.setFontSize(12);
    pdf.text(`Patient ID: ${patientId}`, 20, 40);
    pdf.text(`Age: ${age}`, 20, 50);
    pdf.text(`Tumor Size: ${tumor} cm`, 20, 60);
    pdf.text(`Lymph Nodes: ${nodes}`, 20, 70);
    pdf.text(`Grade: ${grade}`, 20, 80);

    pdf.text(`Survival Probability: ${probabilityValue.textContent}`, 20, 100);
    pdf.text(`Risk Level: ${riskLabel.textContent}`, 20, 110);

    pdf.text("Generated by ML-based Survival Prediction System", 20, 140);

    pdf.save("Breast_Cancer_Prediction_Report.pdf");
}