import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV (ajusta la ruta si es necesario)
df = pd.read_csv("country_health_indicators_v3.csv")

# Lista de países de América del Sur y América Central
paises_america_sur_central = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana",
    "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela",
    "Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras",
    "Nicaragua", "Panama", "Cuba", "Dominican Republic", "Haiti", "Jamaica", "Trinidad and Tobago"
]

# Filtrar los países de interés
df_filtrado = df[df["Country_Region"].isin(paises_america_sur_central)]

# Seleccionar las columnas de interés
columnas_interes = [
    "Country_Region", "population", "median age", "population growth rate",
    "birth rate", "death rate", "maternal mortality rate", "infant mortality rate",
    "life expectancy at birth", "total fertility rate"
]

# Reducir el dataframe a solo esas columnas
df_reducido = df_filtrado[columnas_interes].set_index("Country_Region")

# Asegurar que todos los datos sean numéricos
df_reducido = df_reducido.apply(pd.to_numeric, errors='coerce')

# Cambiar los nombres de columna para dividir en líneas (reemplazar espacios por saltos de línea)
df_reducido.columns = [col.replace(" ", "\n") for col in df_reducido.columns]

# Crear el mapa de calor
plt.figure(figsize=(15, 10))
sns.heatmap(df_reducido, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5)

# Ajustes de estilo
plt.title("Indicadores demográficos en América del Sur y Central", fontsize=14)
plt.xticks(rotation=0, ha="center", fontsize=8)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.show()
