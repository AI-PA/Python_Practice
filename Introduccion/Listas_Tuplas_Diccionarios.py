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