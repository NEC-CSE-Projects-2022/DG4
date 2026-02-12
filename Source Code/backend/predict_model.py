import torch
import pickle
import json
import pandas as pd

# Import your model class from model.py
from model import SA_DGNet

# -----------------------------
# 1️⃣ Load scaler
# -----------------------------
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load all feature columns (691)
with open("feature_columns.json", "r") as f:
    feature_columns_all = json.load(f)

# -----------------------------
# 2️⃣ Only use the 200 features the model was trained on
# -----------------------------
# Replace this with the exact 200 features used during training
model_features = feature_columns_all[:200]

# -----------------------------
# 3️⃣ Load model
# -----------------------------
model = SA_DGNet(input_dim=len(model_features))  # input_dim=200
state_dict = torch.load(r"C:\Users\jagad\OneDrive\Desktop\Metabric_survival\Backend\sadgnet_survival.pth", map_location="cpu")
model.load_state_dict(state_dict)  # strict=True should work now
model.eval()

# -----------------------------
# 4️⃣ Prepare new input data
# -----------------------------
new_data_dict = {f: 0 for f in model_features}  # fill missing with 0
new_data_dict.update({
    "age": 60,
    "tumor_size": 20,
    "node_status": 1
    # add other known features here
})

# Convert to DataFrame in correct order
df = pd.DataFrame([new_data_dict], columns=model_features)

# Apply scaler
X_scaled = scaler.transform(df)
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

# -----------------------------
# 5️⃣ Make predictions
# -----------------------------
with torch.no_grad():
    predictions = model(X_tensor)

print("Predictions:", predictions)