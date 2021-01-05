from p1FuncionesOrdenSuperior import sumaTodos

""" Las funciones lambda son funciones anonimas que pueden definirse en una
sola linea, pueden pasarse como parametros o ser devueltas """

# Lambda insertada como parametro y definida en la misma inserción
# print(sumaTodos(3, lambda x: x**3))

doble = lambda n: n*2

triple = lambda n: n*3

print(sumaTodos(2, triple))