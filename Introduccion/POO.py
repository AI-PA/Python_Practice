#Importaciones.
# import NombreModulo 
# import NombreModulo as matematicas , importar usando el modulo con un nombre alternativo. 
# from Modulo import element , importar solo un elemento del modulo. 
# Modulo.funcion(argumentos)
# Modulo.constante  
import math 
print(math.pow(9,2)) #81
print(math.pi)

from math import pow 
print(pow(9,2)) #81

#POO
# Clase representa la funcionalidad y atributos.
class CuentaBancaria:
    def __init__(self,num_cuenta,nombre_titular,balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
    
    def generar_balance(self):
        print(self.balance)
    
    def depositar(self,monto):
        if monto >0: 
            self.balance+= monto

mi_cuenta = CuentaBancaria(1867626,"Alan Paz",100)

print(mi_cuenta)
print(mi_cuenta.balance) # 100 
mi_cuenta.generar_balance() # 100 
mi_cuenta.depositar(9900)
mi_cuenta.generar_balance #10,000