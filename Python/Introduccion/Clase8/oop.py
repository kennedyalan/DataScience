# Programacion orientada a objetos:
# clases: 
class Perro:
    especie = "Canino" # atributo de clase

    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre # atributo de instancia
        self.edad = edad # atributo de instancia

    # Comportamiento (metodo) de la clase
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"
    

perro1 = Perro("Firulais", 3)
print(perro1.nombre) # Accediendo al atributo de instancia
print(perro1.especie) # Accediendo al atributo de clase
print(perro1.ladrar()) # Llamar al método de la clase
print(repr(perro1))
print(type(perro1))


class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return f"El {self.marca} {self.modelo} está siendo conducido."
    
coche1 = Coche("Toyota", "Corolla", 2020)
print(coche1.marca)
print(coche1.conducir())

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2
    
    def restar(self):
        return self.numero1 - self.numero2
    
    def multiplicar(self):
        return self.numero1 * self.numero2
    
    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero no permitida."
        
    
calculadora = Calculadora(10, 5)
print(f"Suma: {calculadora.sumar()}")
print(f"Resta: {calculadora.restar()}")
print(f"Multiplicación: {calculadora.multiplicar()}")
print(f"División: {calculadora.dividir()}")
