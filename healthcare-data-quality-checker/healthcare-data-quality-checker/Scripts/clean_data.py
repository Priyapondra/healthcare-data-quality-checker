import pandas as pd

# Load the messy data
df = pd.read_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/npidata_pfile.csv', dtype=str)
df.fillna('', inplace=True)

# Clean the names and phone numbers
df['provider_first_name'] = df['Lower_First_name'].astype(str).str.title().str.strip()
df['provider_business_phone_number'] = df['Provider Business Mailing Address Telephone Number'].str.replace(r'\D', '', regex=True)

# Save the cleaned version
df.to_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/cleaned_providers.csv', index=False)

