Team Number – Project Title
-------------------
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
👉 **[Paper Title: Deep Gated Neural Network With Self-Attention Mechanism for Survival Analysis

  – Author Names K.Somasekhar,Ch.Chandrika Tirumala,K.Jayamma,P.Haseena
 ](https://ieeexplore.ieee.org/document/10769011)**
Description:

The paper introduces a new deep learning model called SA-DGNet, which is developed to improve survival analysis. Traditional survival models like the Cox Proportional Hazards model depend on assumptions such as proportional hazards and fixed statistical distributions. These assumptions may not hold true for complex medical data. SA-DGNet overcomes these limitations by using a flexible deep learning approach that can learn nonlinear relationships and time-dependent patterns directly from the data.

A key concept of the model is that survival prediction is treated as a time-series forecasting problem. Time is used as an important input to the model, allowing it to learn how risk changes over different time periods. Instead of directly modeling hazard functions like traditional methods, SA-DGNet predicts the probability of an event occurring at different time points, which provides a more dynamic and data-driven survival prediction.

---

## Our Improvement Over Existing Paper
The existing reference paper mainly focuses on designing the SA-DGNet model using gated neural networks and self-attention for survival analysis. It concentrates more on the deep learning architecture and theoretical modeling of time-to-event data.

In contrast, our work improves and extends the reference paper in the following simple ways:

First, we focus on real clinical datasets such as breast cancer survival data. We carefully handle missing values, normalize features, and properly structure censored survival data. This makes the model more practical for real hospital data.

Second, instead of evaluating only one model, we perform a comprehensive comparison between classical models (CoxPH, Random Forest Survival) and deep learning models (DeepSurv, DeepHit, SA-DGNet). This helps us understand which method works best for structured medical datasets.

Third, we improve training stability by applying regularization techniques and proper hyperparameter tuning. This reduces overfitting and improves generalization.

Fourth, we emphasize interpretability. Along with attention mechanisms, we also analyze feature importance and generate survival curves for risk groups. This makes the predictions easier for doctors to understand.

Finally, our work builds a complete survival prediction pipeline, including data preprocessing, model training, evaluation using C-index and MAE, and risk prediction. This makes the system more practical and ready for real-world clinical use.

Overall, while the reference paper focuses mainly on architectural innovation, our work improves it by making the model more stable, interpretable, well-evaluated, and suitable for real-world medical applications.

---

## About the Project
This project focuses on predicting breast cancer survival using advanced machine learning and deep learning techniques. Survival prediction is important in healthcare because it helps doctors understand a patient’s risk level, plan treatments, and make better clinical decisions.

In this work, we use the METABRIC breast cancer dataset, which contains clinical and genomic information of patients along with survival time and censoring details. The main goal is to develop a system that can accurately estimate a patient’s survival risk based on their medical features. 

We implement and compare different types of survival models, including:

Cox Proportional Hazards (CoxPH) – a classical statistical survival model

Random Forest Survival (RFS) – a machine learning–based method

Deep learning models such as DeepSurv, DeepHit, and the proposed SA-DGNet (Self-Attentive Deep Gated Network)

The proposed SA-DGNet model combines gated neural networks and self-attention mechanisms to learn complex, time-dependent patterns in patient data. In addition to prediction, the system also provides interpretability, such as risk group analysis, survival curves, and feature importance, which are useful for medical understanding. 

The project follows a complete pipeline: data preprocessing, model training, evaluation using survival metrics like C-index and MAE, and survival risk prediction. This makes the system not just a research model but a step toward a practical AI-based survival prediction tool for healthcare applications. 

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
The proposed breast cancer survival prediction model was deployed using a Python-based environment to ensure easy access, testing, and integration. The trained survival models (CoxPH, Random Forest Survival, and SA-DGNet) were connected to a simple web interface where users can enter patient clinical details to obtain survival risk predictions.

All data preprocessing steps, including feature normalization and encoding, are handled on the backend. The model then performs prediction and generates outputs such as risk score, survival probability, and risk group classification, which are displayed to the user along with survival insights.

The system can be deployed on local servers or cloud platforms, making it suitable for real-world clinical and research environments. Tools such as Flask/Streamlit, along with Google Colab or local machines, were used for development, testing, and deployment. This setup ensures fast predictions, scalability, and user-friendly access for healthcare professionals and researchers.

---
