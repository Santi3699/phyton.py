#import random

#jugador = input ("ingrese piedra, papel o tijeras")
#opciones = ["piedra", "papel", "tijeras"]

#juego = random.choice(opciones)
#print(juego)

#if juego == jugador:
#    print("juegue nuevamente")
#elif juego == "piedra" and jugador== "tijera":
#    print("perdiste")
#elif jugador == "piedra" and juego == "tijera":
#    print("Ganaste")
#elif juego == "tijera" and jugador == "papel":
#    print("perdiste")
#elif jugador ==  "tijera" and juego == "papel":
#    print("Ganaste")
#elif juego == "papel" and jugador == "piedra":
#    print("perdiste")
#elif jugador == "papel" and juego =="piedra":
#    print("Ganaste")
#else:
#    print("Intenta nuevamente")

#import random

#numero = random.randint(1,100)
#intentos = 0

#while True:
#    guess = int(input("ingrese un numero"))
#    if numero == guess:
#        intentos +=1
#        print(f"has ganado con {intentos} intentos")
#        break
#   elif numero < guess:
#        intentos +=1
#        print("el numero es menor")
#    elif numero>guess:
#        intentos +=1
#        print("el numero es mayor")
