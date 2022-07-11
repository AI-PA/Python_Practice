edades= {"Gino":15,"Nora":45}
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