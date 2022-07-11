# len() devuelve la cantidad de caracteres que tiene una cadena. 
txt="Hola"
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