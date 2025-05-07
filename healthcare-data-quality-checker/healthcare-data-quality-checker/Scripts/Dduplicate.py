import pandas as pd
from rapidfuzz import fuzz

df = pd.read_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/cleaned_providers.csv')
unique_records = []
seen = set()

for idx, row in df.iterrows():
    identity = f"{row['provider_first_name']} {row['Provider Last Name (Legal Name)']} {row['Provider Business Mailing Address Postal Code']}"
    is_duplicate = False
    for seen_id in seen:
        if fuzz.ratio(identity, seen_id) > 90:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_records.append(row)
        
        seen.add(identity)

pd.DataFrame(unique_records).to_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/deduplicated_providers.csv', index=False)

