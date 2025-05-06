import pandas as pd

# Crear una Serie
#serie = pd.Series([1, 2, 3, 4, 5])

# Crear un DataFrame
#datos = {"Nombre": ["Ana", "Juan", "Pedro"], "Edad": [25, 30, 35]}
#df = pd.DataFrame(datos)
#print(df)

df = pd.read_csv("poblacion.csv")
#data = df[["Date","COL"]]
#print(data[data["Date"]>2000])

# Calcular estadísticas
media = df["COL"].mean()
mediana = df["COL"].median()
desviacion = df["COL"].std()

print("Media", media)
print("Mediana", mediana)
print("Desviacion estandar", desviacion)
