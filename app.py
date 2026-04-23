st.subheader("📊 Detailed Tax Breakdown")

# -------------------------------
# OLD REGIME BREAKDOWN
# -------------------------------
st.markdown("## 🧾 Old Regime Breakdown")

st.write(f"Gross Total Income: ₹ {gross_income:,.2f}")
st.write(f"Less: Deductions: ₹ {deductions:,.2f}")
st.write(f"Less: Standard Deduction: ₹ 50,000")

st.write(f"👉 Taxable Income: ₹ {old_income:,.2f}")

# Slab Calculation Display
old_slab_data = []

basic = basic_exemption(age)

if old_income > basic:
    slab_amt = min(old_income - basic, 250000)
    old_slab_data.append(["5%", slab_amt, slab_amt*0.05])

if old_income > 500000:
    slab_amt = min(old_income - 500000, 500000)
    old_slab_data.append(["20%", slab_amt, slab_amt*0.20])

if old_income > 1000000:
    slab_amt = old_income - 1000000
    old_slab_data.append(["30%", slab_amt, slab_amt*0.30])

old_df = pd.DataFrame(old_slab_data, columns=["Rate", "Income", "Tax"])
st.table(old_df)

st.write(f"Tax on Slabs: ₹ {old_tax:,.2f}")
st.write(f"Capital Gains Tax: ₹ {cg_tax:,.2f}")

# Rebate
if assessee_type == "Individual" and old_income <= 500000:
    st.write("Rebate u/s 87A Applied: YES")
else:
    st.write("Rebate u/s 87A Applied: NO")

st.write(f"Surcharge: ₹ {old_s:,.2f}")
st.write(f"HEC (4%): ₹ {old_cess:,.2f}")

st.write(f"👉 Total Tax: ₹ {final_old:,.2f}")

st.write(f"Less: Advance Tax + TDS: ₹ {advance_tax + tds:,.2f}")

st.write(f"Interest 234A: ₹ {interest_234A(final_old, months_delay):,.2f}")
st.write(f"Interest 234B: ₹ {interest_234B(final_old, advance_tax):,.2f}")
st.write(f"Interest 234C: ₹ {interest_234C(final_old, advance_tax):,.2f}")

st.write(f"✅ Final Payable: ₹ {final_old_payable:,.2f}")


# -------------------------------
# NEW REGIME BREAKDOWN
# -------------------------------
st.markdown("## 🧾 New Regime Breakdown")

st.write(f"Gross Total Income: ₹ {gross_income:,.2f}")
st.write(f"Less: Standard Deduction: ₹ 50,000")

st.write(f"👉 Taxable Income: ₹ {new_income:,.2f}")

new_slab_data = []

slabs = [(300000,0),(600000,0.05),(900000,0.10),(1200000,0.15),(1500000,0.20),(float('inf'),0.30)]
prev = 0

for limit, rate in slabs:
    if new_income > prev:
        amt = min(new_income, limit) - prev
        if rate > 0:
            new_slab_data.append([f"{int(rate*100)}%", amt, amt*rate])
    prev = limit

new_df = pd.DataFrame(new_slab_data, columns=["Rate", "Income", "Tax"])
st.table(new_df)

st.write(f"Tax on Slabs: ₹ {new_tax:,.2f}")
st.write(f"Capital Gains Tax: ₹ {cg_tax:,.2f}")

if assessee_type == "Individual" and new_income <= 700000:
    st.write("Rebate u/s 87A Applied: YES")
else:
    st.write("Rebate u/s 87A Applied: NO")

st.write(f"Surcharge: ₹ {new_s:,.2f}")
st.write(f"HEC (4%): ₹ {new_cess:,.2f}")

st.write(f"👉 Total Tax: ₹ {final_new:,.2f}")

st.write(f"Less: Advance Tax + TDS: ₹ {advance_tax + tds:,.2f}")

st.write(f"Interest 234A: ₹ {interest_234A(final_new, months_delay):,.2f}")
st.write(f"Interest 234B: ₹ {interest_234B(final_new, advance_tax):,.2f}")
st.write(f"Interest 234C: ₹ {interest_234C(final_new, advance_tax):,.2f}")

st.write(f"✅ Final Payable: ₹ {final_new_payable:,.2f}")