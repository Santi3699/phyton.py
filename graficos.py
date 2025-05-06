#Gráfico de barras
import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["A", "B", "C", "D"]
valores = [10, 15, 7, 10]

# Crear gráfico de barras
plt.bar(categorias, valores, color="skyblue")
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()

#Gráfico de líneas
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear gráfico de líneas
plt.plot(x, y, marker="o", color="green", linestyle="--")
plt.title("Gráfico de Líneas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

#Gráfico de dispersión
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# Crear gráfico de dispersión
plt.scatter(x, y, color="purple")
plt.title("Gráfico de Dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

#Mapas de color 
import numpy as np

# Datos de ejemplo
datos = np.random.rand(10, 10)

# Crear mapa de calor
plt.imshow(datos, cmap="viridis", interpolation="nearest")
plt.title("Mapa de Calor")
plt.colorbar()
plt.show()
plt.ylabel("Eje Y")
plt.show()

#Grafico circular 
import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["Categoría A", "Categoría B", "Categoría C"]
tamaños = [40, 35, 25]

# Crear gráfico circular
plt.pie(tamaños, labels=categorias, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()

