# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from api.model import predict_loan_risk
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Streamlit frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoanApplication(BaseModel):
    Age: int
    Employment_Years: int
    Annual_Income: float
    Credit_Score: int
    Loan_Amount: float
    Past_Defaults: int
    Has_Criminal_Record: int

@app.post("/predict")
def predict(applicant: LoanApplication):
    result = predict_loan_risk(applicant.dict())
    return result
