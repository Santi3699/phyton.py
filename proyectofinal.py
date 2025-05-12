import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("country_health_indicators_v3.csv")

valores = df.dropna(subset=["birth rate"])
valores = valores.sort_values(by="birth rate")

x=valores["Country_Region"]
y = valores["birth rate"]
y= y.sort_values()


plt.bar(x, y)
plt.title("Tasa de natalidad en el mundo")
plt.xlabel("País")
plt.ylabel("Valores")
plt.xticks(rotation=90, fontsize=6)
plt.show()

# Diccionario país → continente (agrega más si es necesario)
continentes = {
    "Afghanistan" : "Asia",
    "Albania" : "Europe",
    "Algeria" : "Africa",
    "Andorra" : "Europe",
    "Angola" : "Africa",
    "Antigua and Barbuda" : "North America",
    "Argentina" : "South America",
    "Armenia" : "Asia",
    "Australia" : "Oceania",
    "Austria" : "Europe",
    "Azerbaijan" : "Asia",
    "Bahamas" : "North America",
    "Bahrain" : "Asia",
    "Bangladesh" : "Asia",
    "Barbados" : "North America",
    "Belarus" : "Europe",
    "Belgium" : "Europe",
    "Belize" : "North America",
    "Benin" : "Africa",
    "Bhutan" : "Asia",
    "Bolivia" : "South America",
    "Bosnia and Herzegovina" : "Europe",
    "Botswana" : "Africa",
    "Brazil" : "South America",
    "Brunei" : "Asia",
    "Bulgaria" : "Europe",
    "Burkina Faso" : "Africa",
    "Burma" : "Asia",
    "Burundi" : "Africa",
    "Cabo Verde" : "Africa",
    "Cambodia" : "Asia",
    "Cameroon" : "Africa",
    "Canada" : "North America",
    "Central African Republic" : "Africa",
    "Chad" : "Africa",
    "Chile" : "South America",
    "China" : "Asia",
    "Colombia" : "South America",
    "Congo (Brazzaville)" : "Africa",
    "Congo (Kinshasa)" : "Africa",
    "Costa Rica" : "North America",
    "Cote d'Ivoire" : "Africa",
    "Croatia" : "Europe",
    "Cuba" : "North America",
    "Cyprus" : "Asia",
    "Czechia" : "Europe",
    "Denmark" : "Europe",
    "Diamond Princess" : "Other",
    "Djibouti" : "Africa",
    "Dominica" : "North America",
    "Dominican Republic" : "North America",
    "Ecuador" : "South America",
    "Egypt" : "Africa",
    "El Salvador" : "North America",
    "Equatorial Guinea" : "Africa",
    "Eritrea" : "Africa",
    "Estonia" : "Europe",
    "Eswatini" : "Africa",
    "Ethiopia" : "Africa",
    "Fiji" : "Oceania",
    "Finland" : "Europe",
    "France" : "Europe",
    "Gabon" : "Africa",
    "Gambia" : "Africa",
    "Georgia" : "Asia",
    "Germany" : "Europe",
    "Ghana" : "Africa",
    "Greece" : "Europe",
    "Grenada" : "North America",
    "Guatemala" : "North America",
    "Guinea" : "Africa",
    "Guinea-Bissau" : "Africa",
    "Guyana" : "South America",
    "Haiti" : "North America",
    "Holy See" : "Europe",
    "Honduras" : "North America",
    "Hungary" : "Europe",
    "Iceland" : "Europe",
    "India" : "Asia",
    "Indonesia" : "Asia",
    "Iran" : "Asia",
    "Iraq" : "Asia",
    "Ireland" : "Europe",
    "Israel" : "Asia",
    "Italy" : "Europe",
    "Jamaica" : "North America",
    "Japan" : "Asia",
    "Jordan" : "Asia",
    "Kazakhstan" : "Asia",
    "Kenya" : "Africa",
    "Korea, South" : "Asia",
    "Kosovo" : "Europe",
    "Kuwait" : "Asia",
    "Kyrgyzstan" : "Asia",
    "Laos" : "Asia",
    "Latvia" : "Europe",
    "Lebanon" : "Asia",
    "Liberia" : "Africa",
    "Libya" : "Africa",
    "Liechtenstein" : "Europe",
    "Lithuania" : "Europe",
    "Luxembourg" : "Europe",
    "MS Zaandam" : "Other",
    "Madagascar" : "Africa",
    "Malaysia" : "Asia",
    "Maldives" : "Asia",
    "Mali" : "Africa",
    "Malta" : "Europe",
    "Mauritania" : "Africa",
    "Mauritius" : "Africa",
    "Mexico" : "North America",
    "Moldova" : "Europe",
    "Monaco" : "Europe",
    "Mongolia" : "Asia",
    "Montenegro" : "Europe",
    "Morocco" : "Africa",
    "Mozambique" : "Africa",
    "Namibia" : "Africa",
    "Nepal" : "Asia",
    "Netherlands" : "Europe",
    "New Zealand" : "Oceania",
    "Nicaragua" : "North America",
    "Niger" : "Africa",
    "Nigeria" : "Africa",
    "North Macedonia" : "Europe",
    "Norway" : "Europe",
    "Oman" : "Asia",
    "Pakistan" : "Asia",
    "Panama" : "North America",
    "Papua New Guinea" : "Oceania",
    "Paraguay" : "South America",
    "Peru" : "South America",
    "Philippines" : "Asia",
    "Poland" : "Europe",
    "Portugal" : "Europe",
    "Qatar" : "Asia",
    "Romania" : "Europe",
    "Russia" : "Europe",
    "Rwanda" : "Africa",
    "Saint Kitts and Nevis" : "North America",
    "Saint Lucia" : "North America",
    "Saint Vincent and the Grenadines" : "North America",
    "San Marino" : "Europe",
    "Saudi Arabia" : "Asia",
    "Senegal" : "Africa",
    "Serbia" : "Europe",
    "Seychelles" : "Africa",
    "Sierra Leone" : "Africa",
    "Singapore" : "Asia",
    "Slovakia" : "Europe",
    "Slovenia" : "Europe",
    "Somalia" : "Africa",
    "South Africa" : "Africa",
    "Spain" : "Europe",
    "Sri Lanka" : "Asia",
    "Sudan" : "Africa",
    "Suriname" : "South America",
    "Sweden" : "Europe",
    "Switzerland" : "Europe",
    "Syria" : "Asia",
    "Taiwan*" : "Asia",
    "Tanzania" : "Africa",
    "Thailand" : "Asia",
    "Timor-Leste" : "Asia",
    "Togo" : "Africa",
    "Trinidad and Tobago" : "North America",
    "Tunisia" : "Africa",
    "Turkey" : "Asia",
    "US" : "North America",
    "Uganda" : "Africa",
    "Ukraine" : "Europe",
    "United Arab Emirates" : "Asia",
    "United Kingdom" : "Europe",
    "Uruguay" : "South America",
    "Uzbekistan" : "Asia",
    "Venezuela" : "South America",
    "Vietnam" : "Asia",
    "West Bank and Gaza" : "Asia",
    "Zambia" : "Africa",
    "Zimbabwe" : "Africa"
}

# Crear nueva columna 'Continent'
df["Continent"] = df["Country_Region"].map(continentes)

# Asegurar que la categoría esté en formato numérico
df["Diarrhea & common infectious diseases (%)"] = pd.to_numeric(
    df["Diarrhea & common infectious diseases (%)"], errors='coerce'
)

# Eliminar filas sin continente o sin datos de la categoría
df_filtrado = df.dropna(subset=["Continent", "Diarrhea & common infectious diseases (%)"])

# Crear gráfico de dispersión
plt.figure(figsize=(12, 6))
sns.stripplot(
    data=df_filtrado,
    x="Continent",
    y="Diarrhea & common infectious diseases (%)",
    jitter=True,
    palette="Set2"
)

# Estética
plt.title("Enfermedades Diarreicas e Infecciosas por Continente", fontsize=14)
plt.ylabel("Diarrhea & common infectious diseases (%)")
plt.xlabel("Continente")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Cargar el archivo CSV (ajusta la ruta si es necesario)
df = pd.read_csv("country_health_indicators_v3.csv")

# Lista de países de América del Sur y América Central
paises_america_sur_central = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
    "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela",
    "Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras",
    "Nicaragua", "Panama", "Cuba", "Dominican Republic", "Jamaica", "Trinidad and Tobago"
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
plt.title("Causas principales de defunción en Colombia")
plt.show()


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
