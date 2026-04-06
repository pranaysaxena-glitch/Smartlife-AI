# SmartLife AI

This is an MLOps project that predicts:
- Food expiry
- Health risk

## How to run

1. Install dependencies:
pip install -r requirements.txt

2. Train models:
python train/train_food.py
python train/train_health.py

3. Run API:
uvicorn app.main:app --reload

4. Open browser:
http://127.0.0.1:8000/docs



SmartLife-AI/
│
├── app/
├── models/
├── train/
├── requirements.txt
├── Dockerfile
├── README.md