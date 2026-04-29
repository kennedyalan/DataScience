# Herencia:
# La herencia es un concepto fundamental en la programación orientada a objetos que permite crear nuevas clases basadas en clases existentes. 
# La clase nueva, llamada clase derivada o subclase, hereda atributos y métodos de la clase existente, llamada clase base o superclase. 
# Esto promueve la reutilización de código y facilita la creación de jerarquías de clases.

class Vehiculo:
    def __init__(self, marca, modelo, color="White", ruedas=4):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def info(self):
        return f"{self.marca} {self.modelo} de color {self.color}"
    
    def arrancar(self): 
        return f"El {self.modelo} está arrancando."
    
    def frenar(self):
        return f"El {self.modelo} está frenando."
    

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, color="White", puertas=4):
        super().__init__(marca, modelo, color, ruedas=4) # super() hace referencia al constructor padre (Vehiculo) para inicializar sus atributos
        self.puertas = puertas # Propiedad propia de la clase Coche
        self.año = año # Atributo específico de Coche, no heredado de Vehiculo

    def info(self):
        return f"{super().info()} con {self.puertas} puertas"
    
    def tocar_bocina(self):
        return f"¡El {self.modelo} está tocando la bocina!"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color="White", tipo="bmx"):
        super().__init__(marca, modelo, color, ruedas=2)
        self.tipo = tipo # Propiedad propia de la clase Bicicleta

    def info(self):
        return f"{super().info()} de tipo {self.tipo}"

    def hacer_wheelie(self):
        return f"¡El {self.modelo} está haciendo wheelie!"
    
coche1 = Coche("Toyota", "Corolla", 2020, "Rojo", 4)
print(coche1.info())
print(coche1.tocar_bocina())

bicicleta1 = Bicicleta("Giant", "Escape 3", "Negro", "urbana")
print(bicicleta1.info())
print(bicicleta1.hacer_wheelie())