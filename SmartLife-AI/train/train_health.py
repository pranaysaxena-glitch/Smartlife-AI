print("SCRIPT STARTED")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Sample dataset
data = pd.DataFrame({
    "age": [20, 25, 30, 35, 40, 50, 60],
    "bmi": [18, 22, 25, 28, 32, 35, 38],
    "risk": [0, 0, 0, 1, 1, 1, 1]
})

# Features and target
X = data[["age", "bmi"]]
y = data["risk"]

# Model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save model
with open("models/health_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Health model trained")