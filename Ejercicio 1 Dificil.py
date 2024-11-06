import math

def convertir_a_polares(coordenadas_cartesianas):
  x, y = coordenadas_cartesianas
  radio = math.sqrt(x**2 + y**2)
  angulo = math.atan2(y, x) * 180 / math.pi
  return radio, angulo

coordenadas_cartesianas = (5, 12)
coordenadas_polares = convertir_a_polares(coordenadas_cartesianas)

print(f"Coordenadas polares: radio = {coordenadas_polares[0]:.2f}, ángulo = {coordenadas_polares[1]:.2f}°")
