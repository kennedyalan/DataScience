# Palabra reservada pass
# Se utiliza para indicar que no se va a ejecutar nada
lista = []
print("==================Lista 1==================\n" )
for i in range(5):
    if i == 3: 
        pass

    lista.append(i)
    print(lista)

# Palabra reservada continue
lista2 = []
print("\n ==================Lista 2==================\n" )
for i in range(5):
    if i == 3: 
        continue # Esto hace que se salte el resto del código dentro del bucle para esa iteración y pase a la siguiente
    lista2.append(i)
    print(lista2)

# Palabra reservada break
lista3 = []
print("\n ==================Lista 3==================\n" )
for i in range(5):
    if i == 3: 
        break # Esto hace que se salga completamente del bucle cuando se cumple la condición
    lista3.append(i)
    print(lista3)


# Ejercicio dia de la semana

# Que dia de la semana sera dentro de 30 dias?
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

dia_actual = input("Ingrese el día de la semana actual: ")
