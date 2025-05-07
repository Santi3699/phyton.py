import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv("C:/Users/Usuario/Desktop/PhytonSantiago/country_health_indicators_v3.csv")

# Filtrar por Colombia
colombia = df[df["Country_Region"] == "Colombia"]

# Indicadores seleccionados
indicadores = [
    "cases_growth",
    "death_growth",
    "life expectancy at birth",
    "hospital_beds_per10k",
    "maternal mortality rate",
    "infant mortality rate"
]

# Extraer los valores para Colombia
categorias = indicadores
valores = [colombia[ind].values[0] for ind in indicadores]

# Crear gráfico de barras 
#plt.figure(figsize=(10, 6))
#plt.bar(categorias, valores, color="skyblue")
#plt.title("Indicadores de Salud en Colombia")
#plt.xlabel("Indicador")
#plt.ylabel("Valor")
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()
