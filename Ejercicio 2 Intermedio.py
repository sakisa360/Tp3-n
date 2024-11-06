def contar_letras(inscripcion):
  frecuencias = {}
  for letra in inscripcion.lower():
    if letra in frecuencias:
      frecuencias[letra] += 1
    else:
      frecuencias[letra] = 1
  return frecuencias

inscripcion_antigua = input("Ingrese la inscripción antigua: ")

frecuencias_letras = contar_letras(inscripcion_antigua)

for letra, frecuencia in frecuencias_letras.items():
  print(f"Letra '{letra}': {frecuencia} veces")
