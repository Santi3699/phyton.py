#persona = {
#    "nombre": "Carlos",
#    "edad": 30,
#    "ciudad": "Bogotá"
#}

#print(persona["nombre"])
#print(persona["edad"])
#print(persona["ciudad"])

#persona["profesión"] = "Ingeniero"
#persona["edad"] = 31

#print(persona)

#clave = input("Ingrese una clave: ")

#if clave in persona:
#    print(f"{clave} existe y su valor es: {persona[clave]}")
#else:
#    print(f"{clave} no existe en el diccionario.")

#del persona["ciudad"]
#print(persona)

#respuestas = {
#    "hola": "hola como estas",
#    "que cursos tiene disponibles": "cursos de ai, programacion",
#    "donde estan ubicados": "estamos en la cra 34 #98",
#    "como me puedo inscribir": "para incribirme visitar la pagina de talento tech",
#    "chao": "hasta luego fue un gusto ayudarte"
#}
#del persona["hola"]
#print(persona)

#clave = input ("ingrese una clave: ")


#def obtener_respuesta(mensaje)
#if clave in persona:
#    print(f"{clave} existe y su valor es: {persona[clave]}")
#else:
#    print(f"{clave} no existe en el diccionario.")

#print(len(persona))

#def obtener_respuesta(mensaje):
#    if mensaje in respuestas:
#        return respuestas[mensaje]
#    else:
#        return"no entiendo tu pregunta"

#print("hola soy un chatbot de soporte al cliente")
#while True:
#    mensaje = input("ingrese su consulta")
#    if mensaje.lower()=="salir":
#        break
#    respuesta = obtener_respuesta(mensaje)
#    print(respuesta)

#pip install google-generativeai- Se debe cargar la libreria en el terminal para poder anclarlo 
import google.generativeai as genai

GEMINI_API_KEY = "su_keyAIzaSyAdYUmLipLDUs49S8GoJQ7CoyvNJYKEYPA"
genai.configure(api_key=GEMINI_API_KEY)
modelo = genai.GenerativeModel("gemini-2.0-flash")

def obtener_respuesta(mensaje):
    try:
        respuesta = modelo.generate_content(mensaje)
        return respuesta.text.strip()
    except Exception as e:
        print("Error al generar respuesta:", e)
        return "Lo siento, hubo un problema al procesar tu pregunta."
    
print("hola soy un chabot de soporte al cliente")
while True:
    mensaje = input("ingrese su consulta")
    if mensaje.lower() == "salir":
        break
    respuesta = obtener_respuesta(mensaje)
    print(respuesta)
