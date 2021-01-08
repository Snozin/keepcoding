class Termometro():
  def __init__(self):
    self.__unidadM = 'C'
    self.__temperatura = 0
  
  def __conversor(self, temp, unidad):
    if unidad == 'C':
      return "{}º F".format(temp * 9/5 + 32)
    elif unidad == 'F':
      return "{}º C".format((temp -32) * 5/9)
    else:
      return "Unidad incorrecta"

  def __str__(self):
    return "{}º {}".format(self.__temperatura, self.__unidadM)

  # Getter - Setter pythoniano
  def unidadMedida(self, uniM = None):
    if uniM == None:
      return self.__unidadM
    else:
      if uniM == 'F' or uniM == 'C':
        self.__unidadM = uniM

  def temp(self, temperatura = None):
    if temperatura == None:
      return self.__temperatura
    else:
      self.__temperatura = temperatura

  def medir(self, uniM = None):
    if uniM == None or uniM == self.__unidadM:
      return self.__str__()
    else:
      return self.__conversor(self.__temperatura, self.__unidadM)


t = Termometro()

t.temp = 32
t.unidadMedida = 'C'

z = t.medir('F')

# print(t.temp, t.unidadMedida)
print(z)