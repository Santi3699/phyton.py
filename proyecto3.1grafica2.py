import pandas as pd
import matplotlib.pyplot as plt  # <- Esta línea es necesaria

# Load the latest version
df = pd.read_csv("country_health_indicators_v3.csv")

print(df.describe())
print(df.info())

x = df[df['Country_Region'] == 'Colombia']

y = [
    "Cardiovascular diseases (%)", 
    "Cancers (%)",
    "Diabetes, blood, & endocrine diseases (%)",
    "Respiratory diseases (%)",
    "Liver disease (%)",
    "Diarrhea & common infectious diseases (%)",
    "Musculoskeletal disorders (%)",
    "HIV/AIDS and tuberculosis (%)",
    "Malaria & neglected tropical diseases (%)",
    "Nutritional deficiencies (%)"
]

# Extraer los valores numéricos de la fila correspondiente
x = [x[ind].values[0] for ind in y]

# Convertir a float por si vienen como strings
x = list(map(float, x))

plt.pie(x, labels=y, autopct='%1.1f%%',
        startangle=180, radius=1.1)
plt.title("Prevalencia de enfermedades en Colombia")
plt.show()
