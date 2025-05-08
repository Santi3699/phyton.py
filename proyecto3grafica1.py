import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df = pd.read_csv("country_health_indicators_v3.csv")

# Lista de países de América Latina en el archivo
paises_latinoamerica = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana",
    "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela",
    "Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras",
    "Nicaragua", "Panama", "Cuba", "Dominican Republic", "Haiti", "Jamaica", "Trinidad and Tobago", "Mexico"
]

# Filtrar el DataFrame
df_latam = df[df["Country_Region"].isin(paises_latinoamerica)]

# Seleccionar columnas necesarias
columnas = ["Country_Region", "pneumonia-death-rates", "Share of deaths from smoking (%)"]
df_latam = df_latam[columnas]

# Asegurarse de que los valores sean numéricos
df_latam[["pneumonia-death-rates", "Share of deaths from smoking (%)"]] = df_latam[["pneumonia-death-rates", "Share of deaths from smoking (%)"]].apply(pd.to_numeric, errors='coerce')

# Reorganizar datos para gráfica de barras agrupadas
df_melted = df_latam.melt(id_vars="Country_Region", 
                          value_vars=["pneumonia-death-rates", "Share of deaths from smoking (%)"],
                          var_name="Categoría", value_name="Valor")

# Crear gráfica
plt.figure(figsize=(14, 7))
sns.barplot(data=df_melted, x="Country_Region", y="Valor", hue="Categoría")
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.title("Comparación de muertes por neumonía y tabaquismo en América Latina", fontsize=14)
plt.ylabel("Porcentaje / Tasa")
plt.xlabel("País")
plt.tight_layout()
plt.legend(title="Categoría")
plt.show()
