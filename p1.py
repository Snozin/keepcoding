# Prueba de funcion para el control de versiones

def sumaTodos(limite):
  resultado = 0
  for i in range(0, limite+1):
    resultado += i

  return resultado

print(sumaTodos(100))