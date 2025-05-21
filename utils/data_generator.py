# utils/data_generator.py

import pandas as pd
import random
from faker import Faker
import os

fake = Faker()

def generate_synthetic_loan_data(num_samples=5000):
    data = []

    for _ in range(num_samples):
        age = random.randint(21, 65)
        income = round(random.uniform(20000, 150000), 2)
        employment_years = random.randint(0, age - 20)
        credit_score = random.randint(300, 850)
        loan_amount = round(random.uniform(5000, 50000), 2)
        loan_purpose = random.choice(["Home", "Car", "Education", "Business", "Personal"])
        has_criminal_record = random.choice([0, 1])
        past_defaults = random.randint(0, 5)

        # Simple logic: high income, high credit score, low past defaults → likely approval
        approval_probability = (
            0.4 * (income / 150000) +
            0.3 * ((credit_score - 300) / 550) +
            0.2 * (employment_years / 45) -
            0.2 * (past_defaults / 5) -
            0.1 * has_criminal_record
        )
        is_approved = 1 if approval_probability > 0.5 else 0

        data.append({
            "Name": fake.name(),
            "Age": age,
            "Employment_Years": employment_years,
            "Annual_Income": income,
            "Credit_Score": credit_score,
            "Loan_Amount": loan_amount,
            "Loan_Purpose": loan_purpose,
            "Past_Defaults": past_defaults,
            "Has_Criminal_Record": has_criminal_record,
            "Loan_Approved": is_approved
        })

    df = pd.DataFrame(data)

    os.makedirs("data", exist_ok=True)
    file_path = "data/synthetic_loan_data.csv"
    df.to_csv(file_path, index=False)
    print(f"✅ Generated synthetic data with {num_samples} rows at: {file_path}")

    return file_path

# To run standalone:
if __name__ == "__main__":
    generate_synthetic_loan_data(5000)
