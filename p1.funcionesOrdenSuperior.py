# Las funciones de orden superior son las que admiten otras funciones
# como parametros o devuelven una funcion como resultado o ambas cosas.

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

print(sumaTodos(100, sumaNormal))
print(sumaTodos(3, sumaCuadrados))

""" Al llamar a la funcion sumaNormal o sumaCuadrados no se les asigna ningun
parametro, este parametro es añadido dentro de la funcion sumaTodos cuando se
le asigna el valor i"""