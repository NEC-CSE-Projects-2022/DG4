Team Number – Project Title
DG4-Predicting Breast Cancer Survival :An Approach Using Deep Learning And Machine Learning Techniques
---------
## Team Info
22471A05L7 — Ch Chandrika Tirumala ( [LinkedIn](https://www.linkedin.com/in/chandrika-tirumala-chennupalli-b87491270/) )
Work Done:Data preprocessing,FeautreExtraxtion, model training, evaluation 

- 22471A05M7 — K Jayamma ( [LinkedIn](https://www.linkedin.com/in/jayamma-kodavati-a562a5289/) )
_Work Done:Documentation

- 23475A0501 — P Haseena ( [LinkedIn](https://www.linkedin.com/in/haseena-parlapalli-0b4935298/) )
_Work Done:Frontend/Backend

---
## Abstract
Breast cancer survival prediction plays an important role in medical decision-making and patient prognosis. In this project, we analyze and compare different survival analysis techniques using the METABRIC breast cancer dataset, which includes clinical and genomic features of patients. Traditional models such as Cox Proportional Hazards (CoxPH) and Random Survival Forest (RSF) were evaluated along with deep learning models like DeepSurv, DeepHit, and our proposed SA-DGNet (Self-Attention Deep Gated Network).

Our study shows that classical models like CoxPH and RSF achieved higher prediction accuracy in terms of Concordance Index (C-index), while SA-DGNet demonstrated the ability to capture complex feature relationships and provide interpretable insights using attention mechanisms. Although deep models did not outperform traditional methods on this dataset, they offer flexibility for handling complex medical data.

This work highlights the effectiveness of survival analysis models for predicting patient survival and supports the use of both statistical and deep learning approaches in healthcare applications.

---

## Paper Reference (Inspiration)
👉 **[Paper Title xxxxxxxxxx
  – Author Names xxxxxxxxxx
 ](Paper URL here)**
Original conference/IEEE paper used as inspiration for the model.

---

## Our Improvement Over Existing Paper
xxxxxxxxxx

---

## About the Project
Give a simple explanation of:
- What your project does
- Predicts survival time of breast cancer patients using genomic data.
- Why it is useful
- Helps in early prognosis, personalized treatment planning, and risk assessment.
- General project workflow (input → processing → model → output)
- Dataset → Preprocessing → Feature Selection → SA-DGNet Model → Survival Time Prediction

---

## Dataset Used
👉 **[METABRIC Breast Cancer Dataset](https://www.cbioportal.org/study/summary?id=brca_metabric)**

**Dataset Details:**
Total records: ~1,900 breast cancer patient samples
Features: Clinical attributes (age, tumor stage, survival status), gene expression data, mutation information
Target variable: Survival time and censoring indicator (event occurred or not)
Domain: Medical — Breast Cancer Survival Analysis


---

## Dependencies Used
Python – Core programming language
NumPy – Numerical computations
Pandas – Data handling and preprocessing
Scikit-learn – Data splitting and preprocessing utilities
Lifelines / Scikit-survival – CoxPH and Random Survival Forest models
PyTorch / TensorFlow – Deep learning model (SA-DGNet) implementation
Matplotlib & Seaborn – Visualization of results and survival curves


---

## EDA & Preprocessing
Missing value handling
Feature normalization
Gene feature selection
Data split into train/test sets

---

## Model Training Info
-Trained multiple survival analysis models:
         -Cox Proportional Hazards (CoxPH)
         -Random Survival Forest (RSF)
         -DeepSurv (Neural Cox model)
         -DeepHit (Deep survival model)
         -SA-DGNet (Proposed Self-Attention Deep Gated Network)

-Hyperparameters were optimized using validation-based tuning and performance monitoring with C-index.
-The proposed SA-DGNet model combines gated neural layers and self-attention mechanisms to capture both short-term and long-range dependencies in patient survival patterns.
-Models were compared based on survival prediction accuracy, concordance index, and error metrics.

---

## Model Testing / Evaluation
A train–test split was used to evaluate model performance.
Metrics used:
   -Concordance Index (C-index) – Measures how well the model correctly ranks survival times.
   -Mean Absolute Error (MAE) – Measures the average difference between predicted and actual survival time.
   -Loss Function (Survival Loss) – Used during training to monitor convergence.

Cross-validation and validation monitoring were used to ensure model stability and reduce overfitting.

---

## Results
Best Model: Cox Proportional Hazards (CoxPH)
  - CoxPH C-index: 0.87
  - Random Survival Forest C-index: 0.82
  - SA-DGNet C-index: 0.75
-Traditional models like CoxPH and Random Survival Forest performed better than deep learning models on the METABRIC dataset.
-Even though SA-DGNet had slightly lower accuracy, it was able to capture complex patterns and provided better interpretability.
-These results show that classical survival models are very effective for structured medical datasets.

---

## Limitations & Future Work
Limitations:
-The dataset size is relatively limited.
-METABRIC represents a specific patient cohort, which may affect generalization to other populations.
-Some clinical and genetic factors influencing survival may not be included in the dataset.
Future Work:
-Training the model on larger and more diverse medical datasets.
-Incorporating multi-modal data such as imaging and clinical reports.
-Improving deep learning architectures for better survival prediction accuracy.

---

## Deployment Info
xxxxxxxxxx

---
