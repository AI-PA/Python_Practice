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