import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: READ DATA FROM CSV
# -----------------------------
# CSV file same folder me honi chahiye
df = pd.read_csv("payment_data.csv")

print("CSV file loaded successfully!\n")
print(df.head())

# -----------------------------
# STEP 2: PAYMENT METHOD USAGE
# -----------------------------
usage_count = df['payment_type'].value_counts()
total_amount = df.groupby('payment_type')['transaction_amount'].sum()

print("\nPayment Method Usage Count:")
print(usage_count)

print("\nTotal Transaction Amount per Payment Method:")
print(total_amount)

# -----------------------------
# STEP 3: STATISTICAL ANALYSIS
# -----------------------------
stats = df.groupby('payment_type')['transaction_amount'].agg(['mean','median','max','min'])
print("\nStatistical Analysis (Mean, Median, Max, Min):")
print(stats)

# -----------------------------
# STEP 4: VISUALIZATION
# -----------------------------
# Bar chart for total transaction amount
plt.bar(total_amount.index, total_amount.values, color='skyblue')
plt.xlabel("Payment Method")
plt.ylabel("Total Transaction Amount")
plt.title("Total Transaction Amount by Payment Method")
plt.show()

# Pie chart for usage distribution
plt.pie(
    usage_count.values,
    labels=usage_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Usage Distribution of Payment Methods")
plt.show()
