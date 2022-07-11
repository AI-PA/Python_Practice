
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