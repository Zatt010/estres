# Inicializar todas las respuestas en False
estres_diario = False
factores_externos = False
entorno_familiar = False
presion_academica = False
discriminacion_acoso = False
entorno_universitario = False
habilidades_afrontamiento = False
ayuda_profesional1 = False
ayuda_profesional2 = False
# Leer el nombre del encuestado desde el teclado
nombre_encuestado = input("Ingrese su nombre: ")

# Pregunta 1
respuesta1 = input("¿Siente estrés en su vida diaria? (Sí/No)")
if respuesta1 == "Si" or respuesta1 == "si":
    estres_diario = True

# Pregunta 2
respuesta2 = input("¿Cree que el estrés que experimenta se debe principalmente a factores externos? (Sí/No)")
if respuesta2 == "Si" or respuesta2 == "si":
    factores_externos = True

# Pregunta 3
respuesta3 = input("¿Considera que su entorno familiar contribuye al estrés que experimenta? (Sí/No)")
if respuesta3 == "Si" or respuesta3 == "si":
    entorno_familiar = True

# Pregunta 4
respuesta4 = input("¿Siente que la presión académica es demasiado alta? (Sí/No)")
if respuesta4 == "Si" or respuesta4 == "si":
    presion_academica = True

# Pregunta 5
respuesta5 = input("¿Ha experimentado discriminación o acoso en el entorno universitario? (Sí/No)")
if respuesta5 == "Si" or respuesta5 == "si":
    discriminacion_acoso = True

# Pregunta 6
respuesta6 = input("¿Cree que su entorno universitario contribuye al estrés que experimenta? (Sí/No)")
if respuesta6 == "Si" or respuesta6 == "si":
    entorno_universitario = True

# Pregunta 7
respuesta7 = input("¿Ha buscado ayuda profesional para manejar su estrés? (Sí/No)")
if respuesta7 == "Si" or respuesta7 == "si":
    ayuda_profesional1 = True

# Pregunta 8
respuesta8a = input("¿Ha utilizado alguna vez ejercicio físico para manejar el estrés? (Sí/No)")
if respuesta8a == "Si" or respuesta8a == "si":
    ejercicio_fisico = True

respuesta8b = input("¿Ha utilizado alguna vez meditación o técnicas de relajación para manejar el estrés? (Sí/No)")
if respuesta8b == "Si" or respuesta8b == "si":
    tecnicas_relajacion = True

respuesta8c = input("¿Ha hablado con amigos o familiares para manejar el estrés? (Sí/No)")
if respuesta8c == "Si" or respuesta8c == "si":
    hablar_amigos_familiares = True

respuesta8d = input("¿Ha buscado ayuda profesional para manejar el estrés?(Si/No)")
if respuesta8d == "Si" or respuesta8d == "si":
    ayuda_profesional2 = True


# Mensaje de agradecimiento
print("\n¡Gracias por completar!")

if estres_diario == True and factores_externos == True and entorno_familiar ==True and presion_academica == True and discriminacion_acoso == True and entorno_universitario == True and habilidades_afrontamiento == False and ayuda_profesional1 == False and ayuda_profesional2 == False:
    print("\nFACTOR EXTERNO")

if estres_diario == False and factores_externos == False and entorno_familiar ==False and presion_academica == True and discriminacion_acoso == True and entorno_universitario == True and habilidades_afrontamiento == False and ayuda_profesional1 == False and ayuda_profesional2 == False:
    print("\nFACTOR FALSE")
