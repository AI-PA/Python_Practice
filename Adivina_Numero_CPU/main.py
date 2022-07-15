import random
def adivina_numero(x):
    print("=========================")
    print("¡Bienvenido(a) al Juego!")
    print("=========================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinar el numero.")

    limite_inferior=1
    limite_superior=x
    respuesta= ""
    while respuesta.upper() != "C":
        if limite_inferior != limite_superior: 
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion= limite_inferior
        respuesta=input(f"La prediccion es {prediccion}, si es muy alta, ingrese (A). Si es muy baja (B). Si es correcta, ingrese (C): ")