import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

os.makedirs("models", exist_ok=True)

data = pd.DataFrame({
    "temperature": [5, 10, 15, 20, 25, 30],
    "humidity": [30, 40, 50, 60, 70, 80],
    "days": [10, 9, 7, 5, 3, 2]
})

X = data[["temperature", "humidity"]]
y = data["days"]

model = LinearRegression()
model.fit(X, y)

with open("models/food_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Food model trained")