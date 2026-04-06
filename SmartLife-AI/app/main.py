from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
food_model = pickle.load(open("models/food_model.pkl", "rb"))
health_model = pickle.load(open("models/health_model.pkl", "rb"))
food_model = pickle.load(open("models/food_model.pkl", "rb"))
health_model = pickle.load(open("models/health_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "SmartLife AI Running 🚀"}

@app.get("/food")
def predict_food(temp: float, humidity: float):
    result = food_model.predict([[temp, humidity]])
    return {"remaining_days": float(result[0])}

@app.get("/health")
def predict_health(age: int, bmi: float):
    result = health_model.predict([[age, bmi]])
    return {"risk": int(result[0])}