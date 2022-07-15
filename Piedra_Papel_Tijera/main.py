import random 
def gano_el_jugador(jugador,oponente):
    if ((jugador =='pi' and oponente =='ti') or (jugador == 'ti' and oponente =='pa') or (jugador == 'pa 'and oponente =='pi')):
        return True
    else: 
        return False

def jugar():
    usuario = input("Escope una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n").lower()
    computadora=random.choice(["pi","pa","ti"]) 

    if usuario == computadora:
        return '¡Empate! \n' + escoger_computadora(computadora)

    if gano_el_jugador(usuario,computadora):
        return '¡Ganaste! \n' +escoger_computadora(computadora)
    return '¡Perdiste! \n'  + escoger_computadora(computadora)

def escoger_computadora(seleccion):
    if seleccion =='pi':
        return 'la Computadora escogio Piedra.'
    elif seleccion =='pa':
        return 'la Computadora escogio Papel.'
    else: 
        return 'la Computadora escogio Tijeras.'


print(jugar())