import pandas as pd

# Load the raw dataset
df = pd.read_csv("raw_customer_dataset.csv")

print("Initial Data Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ---------------- CLEANING ----------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing age with median
df['age'] = df['age'].fillna(df['age'].median())

# Fill missing last_purchase_date with a default date
df['last_purchase_date'] = df['last_purchase_date'].fillna("2023-01-01")

# Convert date columns to datetime
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'], errors='coerce')

# Feature Engineering: customer tenure in years
df['customer_tenure_years'] = (
    (df['last_purchase_date'] - df['signup_date']).dt.days / 365
)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Data cleaning completed. Cleaned file saved as cleaned_data.csv")
