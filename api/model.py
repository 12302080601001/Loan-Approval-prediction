# api/model.py

import joblib
import numpy as np

model = joblib.load("models/loan_model.pkl")

def predict_loan_risk(input_data: dict):
    features = [
        "Age", "Employment_Years", "Annual_Income",
        "Credit_Score", "Loan_Amount", "Past_Defaults",
        "Has_Criminal_Record"
    ]
    data = np.array([[input_data[feature] for feature in features]])
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    return {"prediction": int(prediction), "probability": round(probability, 2)}
