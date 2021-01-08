class Perro():
  def __init__(self, nom,edad, peso):
    self.nombre = nom
    self.edad = edad
    self.peso = peso
  
  def ladrar(self):
    print("Guau guau!")

  def __str__(self):
    return "Perro {}, edad {}, peso {}".format(self.nombre, self.edad, self.peso)
