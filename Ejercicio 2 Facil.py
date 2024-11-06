personas = {
  "Juan": 32,
  "María": 28,
  "Pedro": 45,
  "Ana": 20
}

# Agregar una nueva persona
nombre_nuevo = input("Ingrese el nombre de la persona: ")
edad_nueva = int(input("Ingrese la edad de la persona: "))
personas[nombre_nuevo] = edad_nueva

print(f"Se ha agregado a {nombre_nuevo} con {edad_nueva} años a la lista de personas.")

# Eliminar una persona
nombre_eliminar = input("Ingrese el nombre de la persona que desea eliminar: ")

if nombre_eliminar in personas:
  del personas[nombre_eliminar]
  print(f"Se ha eliminado a {nombre_eliminar} de la lista de personas.")
else:
  print(f"No se encontró a {nombre_eliminar} en la lista de personas.")

# Buscar una persona
nombre_buscar = input("Ingrese el nombre de la persona que desea buscar: ")

if nombre_buscar in personas:
  edad_persona = personas[nombre_buscar]
  print(f"{nombre_buscar} tiene {edad_persona} años.")
else:
  print(f"No se encontró a {nombre_buscar} en la lista de personas.")
