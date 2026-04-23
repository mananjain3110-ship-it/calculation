import streamlit as st
import pandas as pd

st.title("💰 Income Tax Calculator")

# Inputs
salary = st.number_input("Salary", 0)
house = st.number_input("House Property", 0)
business = st.number_input("Business", 0)
other = st.number_input("Other Income", 0)

# Define BEFORE use
gross_income = salary + house + business + other

if st.button("Calculate Tax"):

    st.subheader("📊 Breakdown")

    # Now safe to use
    st.write(f"Gross Total Income: ₹ {gross_income:,.2f}")
st.write(f"✅ Final Payable: ₹ {final_new_payable:,.2f}")
