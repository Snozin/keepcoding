""" Las funciones de orden superior son las que admiten otras funciones
como parametros o devuelven una funcion como resultado o ambas cosas. """


# Ejemplos de funciones que reciben funciones como params
def sumaNormal(n):
  return n

def sumaCuadrados(n):
  return n * n

def sumaTodos(limite, funcion):
  resultado = 0

  for i in range(limite + 1):
    # Sumaremos en la variable resultado la operación devuelta por la func
    resultado += funcion(i) 

  return resultado

# print(sumaTodos(100, sumaNormal))
# print(sumaTodos(3, sumaCuadrados))

""" Al llamar a la funcion sumaNormal o sumaCuadrados no se les asigna ningun
parametro, este parametro es añadido dentro de la funcion sumaTodos cuando se
le asigna el valor i"""


# Ejemplos de funciones que devuelven funciones
def minimo(*params):
  if len(params) == 0:
    return 0
  
  min = 0
  for i in range(len(params)):
    if params[i] < min:
      min = params[i]
  
  return min

def maximo(*params):
  if len(params) == 0:
    return 0
  
  max = 0
  for i in range(len(params)):
    if params[i] > max:
      max = params[i]
  
  return max

nFunciones = {
  'max' : maximo,
  'min' : minimo
}

def dameFuncion(nombre):
  nombre = nombre.lower()
  if nombre in nFunciones.keys():
    return nFunciones[nombre]
  
  return None

# Control para que solo imprima cuando se ejecuta por consola directamente
# este archivo.
if __name__ == '__main__':
  print(dameFuncion('max')(2,7,-3,1))