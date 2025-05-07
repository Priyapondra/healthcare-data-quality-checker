import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/keert/Desktop/healthcare-data-quality-checker/enriched_providers.csv')
df['specialty'].value_counts().head(10).plot(kind='bar')
plt.title("Top Specialties")
plt.show()



