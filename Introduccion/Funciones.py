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