print("Hello World!")
# Comentario 
num = 15 # 15
print(num)

num = 8
print(num) # 8
# Asignacion de variables y reglas para nombrar variables.
# Las variables pueden y deben iniciar con un nombre o con un guion bajo. 
# Se distingue entre mayusculas y minusculas  "edad" diferente de "Edad"
edad = 24 
Edad = 70
EDAD = 15 
print(edad) # 24
print(Edad) # 70
print(EDAD) # 15
txt= "hola" 
# type() devuelve el tipo de dato que es aquello que pongamos entre los parentesis. 
print(type(18)) #Integer
print(type(18.5)) #Float
print(type(True)) #Bolean 
print(type("Hola")) #Str
print(type(num))
print(type(txt))
# len() devuelve la cantidad de caracteres que tiene una cadena. 
print(len("Hola")) #4
print(len(txt)) #4
print(txt[3])

# Slicing  <cadena> [inicio:fin]. ,cadena[inicio:], <cadena>[:fin], <cadena>[:]
palabra= "Python"
print(palabra[1:4]) # yth
frase="¡Hola, Mundo!"
print(frase[7:12]) # Mundo 

# <cadena>[inicio:fin:paso] como salta de un caracter al siguiente. 
print(palabra[1:6:2]) # yhn
# Metodos <cadena>.metodo(valor)
#.capitalize , Devuelve una copia de la cadena con el primer caracter en mayusculas y el resto en minusculas.
#.find encuentra aquello que busquemos. 
#.index nos dice la posicion de lo que buscamos. 
#.isalnum , isalpha , isdecimal etc. nos permite comprobar si el dato es numerico, decimal, cadena etc.. 
#.lower y .upper nos permite modificar las cadenas para que sean minusculas o mayusculas. 
# input(mensaje) nos permite ingresar datos al programa. 
num = input("inserte un numero: ")
print(num)
print(type(num)) # str
print(type(int(num)))
# input siempre regresa un dato str.
# ** exponenciacion
# % retorna el resto de la division. 
# // regresa la parte entera de la division.  
print(5**3) #125 


# if <condicion>: /n #Codigo
temp = 15 
if temp < 0: 
    print("Muy Frio")
elif temp <25:
    print("Frio")
else: 
    print("Calor")


# Lista
letras = ["a","b","c","d"]
print(letras[0])
letras.append("e")
# <lista>.append(element) agrega un elemnto a la lista, este estaria en el ultimo lugar. 
print(letras) #[a,b,c,d,e]
# <lista>.insert(indice,elemento) agrega un elemento en el indice indicado. 
nums=[1,2,3,4,5]
nums.insert(0,6)
print(nums) # [6,1,2,3,4,5]

a=[1,2,3,4,5,4]
a.remove(4) 
print(a) #[1,2,3,5,4]
# <lsita>.remove(element) elimina el primer elemento que coincida con lo que se quiere eliminar 

#index(element) retorna el primera posicion que se encuentra lo que estamos buscando y en caso de no encontralo regresa un error.
a.index(4) #4

6 in a #False. 

letras[0]="z"
print(letras) # [z,b,c,d,e]

#Metodos con listas. 
#.count(elem)  , cuantas veces se repite la lista
#.extend(lista) , extinede una lista copiando los elementos de otra. 
#.pop , elimina un elemento de una lista.
#.reverse ,voltea una lista. 
#.sort , ordena una lista. 

#Tuplas 
#ordenada e inmutable. 
a = (1,2,3,4)
#a[0]=5 , Produce ERROR!. 

print(a[0]) #1
print(a.index(4)) #3
print(a.count(4)) # 1 

#Diccionarios
# Unicas e inmutables.
#<diccionrio>[Clave]
edades= {"Gino":15,"Nora":45}

print(edades["Gino"]) #15
print(edades.get("Nora")) #45

edades["Talina"]=67
print(edades) #{'Gino':15,'Nora':45, 'Talina':67}

#del <dicc>[<clave>]
del edades["Talina"]
print(edades) # {Gino:15, Nora:45}


# Ciclo For y While. 
for i in range(4): #
    print(i)
# range(start,stop,step)
#ciclos sobre iterables. 
for char in "Loops":
    print(char) # L O O P S

for edad in edades:
    print(edad)

for clave,valor in edades.items():
    print(clave,valor)

x=20
while x < 35: 
    print(x)
    x+=3
#Ciclo se ejecuta hasta que la condicion sea falsa. 
# Crt + C para terminar la ejecuccion. 

#Funciones. 
# Bloque de codigo reutilizable. 
# def <function>(parametro): 
def mostrar_mensaje():
    print("Hola Mundo!.")

mostrar_mensaje() 
#Parametros, variable que esta en la funcion y se usan cuando sean llamados. 

def mostar_doble(num):
    print(num*2)

#Argumento es el valor que le damos a los parametros. 
mostar_doble(2)

#Return regresa un valor donde es llamada. 
# return<valor>
def sumar(x,y):
    return x+y 

print(sumar(2,3))

#Recursion, es llamar a la funcion a si misma. 
def fibonacchi(n): 
    if n == 0 or n==1 : 
        return n 
    else: 
        return fibonacchi(n-1)+fibonacchi(n-2)

print(fibonacchi(3)) #2

#Archivos 
# Senetncia With se puede abrir y cerrar un archivo 
# with open("nombre del archibo.txt", "Modo de apertura ") as archivo 
with open ("grases_famosas.txt","r") as archivo: 
    for linea in archivo: 
        print("===Frase===")
        print(linea)

# r read leer
# w write - escribor , ¡cambia completamente el contenido del archivo!
# a append -añadir 
# añadir + permite leer el archivo. 

notas = {
    "Nora": 87, 
    "Gino": 100,
    "Loretto": 67, 
    "Talia":45
}
with open("data_estudiantes.txt","w") as archivo: 
    for nombre, nota in notas.item():
        archivo.write(nombre +": "+str(nota) + "\n")

nuevas_notas={
    "Emily": 54,
    "Daniel": 98, 
    "Julienne":78
}
with open("data_estudiantes.txt","a") as archivo: 
    for nombre, nota in nuevas_notas.item():
        archivo.write(nombre +": "+str(nota) + "\n")


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
mi_cuenta.generar_balance() #10,000