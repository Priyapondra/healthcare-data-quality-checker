
import pandas as pd

df = pd.read_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/enriched_providers.csv')

print("Total Records:", len(df))
print("Missing First Names:", df['provider_first_name'].isna().sum())
print("Unique ZIP Codes:", df['Provider Business Mailing Address Postal Code'].nunique())
print("Top 5 Specialties:\n", df['specialty'].value_counts().head())




