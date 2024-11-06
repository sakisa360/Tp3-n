def encontrar_palabra_mas_comun(manuscrito):
  palabras = manuscrito.lower().split()
  frecuencias_palabras = {}
  for palabra in palabras:
    if palabra in frecuencias_palabras:
      frecuencias_palabras[palabra] += 1
    else:
      frecuencias_palabras[palabra] = 1

  palabra_mas_comun = max(frecuencias_palabras, key=frecuencias_palabras.get)
  frecuencia_mas_comun = frecuencias_palabras[palabra_mas_comun]

  return palabra_mas_comun, frecuencia_mas_comun

manuscrito_antiguo = input("Ingrese el contenido del manuscrito antiguo: ")

palabra_mas_comun, frecuencia_mas_comun = encontrar_palabra_mas_comun(manuscrito_antiguo)

print(f"
