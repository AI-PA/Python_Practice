import random
def adivina_numero(x):
    print("=========================")
    print("¡Bienvenido(a) al Juego!")
    print("=========================")
    print("Tu meta es adivinar el número generado por la computadora.")

    num= random.randint(1,x) #Numero aletorio entre 1 y x 
    adivinar=0 

    while (adivinar != num):
        adivinar = int(input(f"Adivina un numero entre 1 y {x}: "))

        if adivinar < num: 
            print("Intenta otra vez. Este numero es muy  pequeño")
        elif adivinar> num: 
            print("Intenta otra vez. Este numero es muy grande.")
    print(f"¡Felicitaciones! Adivinaste el numero {num} correctamente.")

adivina_numero(10)