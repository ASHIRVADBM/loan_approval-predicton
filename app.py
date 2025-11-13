import streamlit as st
import numpy as np
import pandas as pd
import pickle

# -----------------------------
# Load Model and Scaler
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Loan Approval Predictor", page_icon="💰")

st.title("💰 Loan Approval Prediction App")
st.write("Fill the applicant details below to predict whether the loan will be approved.")

# -----------------------------
# User Input Form
# -----------------------------
with st.form("loan_form"):

    no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, step=1)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    income_annum = st.number_input("Annual Income", min_value=0, step=1000)
    loan_amount = st.number_input("Loan Amount", min_value=0, step=1000)
    loan_term = st.number_input("Loan Term (in months)", min_value=0, step=1)

    cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, step=1)
    assets = st.number_input("Total Assets Value", min_value=0, step=1000)

    submitted = st.form_submit_button("Predict Loan Approval")

# -----------------------------
# Prediction Logic
# -----------------------------
if submitted:

    # Convert categorical values
    education_val = 1 if education == "Graduate" else 0
    self_emp_val = 1 if self_employed == "Yes" else 0

    # Create DataFrame for model
    input_df = pd.DataFrame([[
        no_of_dependents,
        education_val,
        self_emp_val,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        assets
    ]], columns=[
        'no_of_dependents', 'education', 'self_employed', 'income_annum',
        'loan_amount', 'loan_term', 'cibil_score', 'assets'
    ])

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]

    # Output result
    if prediction == 1:
        st.success("🎉 Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")
