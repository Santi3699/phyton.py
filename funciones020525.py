#def saludar():
#    print("¡Hola, mundo!")

# Llamar a la función
#saludar()  # Imprime "¡Hola, mundo!"
#saludar()
#saludar()

#def saludar(nombre):
#    print(f"¡Hola, {nombre}!")
    
#minombre = input ("ingrese su nombre")

# Llamar a la función con un argumento
#saludar("Santiago")  # Imprime "¡Hola, Ana!"

#def saludar(minombre):
#    print(f"¡Hola, {minombre}!")
    
#minombre = input ("ingrese nombre y apellido")

# Llamar a la función con un argumento
#saludar("Pedro Marquez")  # Imprime "¡Hola, Ana!"

def saludar(nombre,apellido):
    print(f"¡Hola, {nombre}{apellido}")

minombre = input ("ingrese su nombre")
miapellido = input("ingrese su apellido")

saludar(minombre,miapellido)
