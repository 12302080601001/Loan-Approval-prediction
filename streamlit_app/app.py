# streamlit_app/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Loan Approval Risk Analyzer", layout="centered")

st.title("🏦 Loan Approval Risk Analyzer")
st.markdown("Analyze whether a loan should be approved based on applicant's profile.")

with st.form("loan_form"):
    age = st.slider("Age", 21, 65, 30)
    employment_years = st.slider("Years of Employment", 0, 40, 5)
    income = st.number_input("Annual Income (USD)", 20000.0, 200000.0, 50000.0)
    credit_score = st.slider("Credit Score", 300, 850, 650)
    loan_amount = st.number_input("Loan Amount Requested (USD)", 1000.0, 100000.0, 15000.0)
    past_defaults = st.slider("Number of Past Defaults", 0, 10, 0)
    has_criminal_record = st.radio("Criminal Record?", ["No", "Yes"])

    submitted = st.form_submit_button("Predict Loan Approval")

if submitted:
    api_url = "http://127.0.0.1:8000/predict"
    input_data = {
        "Age": age,
        "Employment_Years": employment_years,
        "Annual_Income": income,
        "Credit_Score": credit_score,
        "Loan_Amount": loan_amount,
        "Past_Defaults": past_defaults,
        "Has_Criminal_Record": 1 if has_criminal_record == "Yes" else 0,
    }

    try:
        response = requests.post(api_url, json=input_data)
        result = response.json()

        if result["prediction"] == 1:
            st.success(f"✅ Loan Approved (Confidence: {result['probability']*100:.1f}%)")
        else:
            st.error(f"❌ Loan Rejected (Confidence: {result['probability']*100:.1f}%)")

    except Exception as e:
        st.error(f"API Connection Error: {e}")
