import pandas as pd
import json

df = pd.read_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/deduplicated_providers.csv')
with open('scripts/mock_api.json') as f:
    specialty_map = json.load(f)

df['specialty'] = df['Healthcare Provider Taxonomy Code_1'].map(specialty_map)
df.to_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/enriched_providers.csv', index=False)


