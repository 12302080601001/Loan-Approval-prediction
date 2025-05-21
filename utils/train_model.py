# utils/train_model.py

import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(data_path="data/synthetic_loan_data.csv"):
    df = pd.read_csv(data_path)

    features = [
        "Age", "Employment_Years", "Annual_Income",
        "Credit_Score", "Loan_Amount", "Past_Defaults",
        "Has_Criminal_Record"
    ]
    target = "Loan_Approved"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/loan_model.pkl")
    print("✅ Model trained and saved to models/loan_model.pkl")

if __name__ == "__main__":
    train_model()
