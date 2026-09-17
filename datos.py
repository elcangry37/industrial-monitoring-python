import json

def cargar_planta():
   try:
      with open("planta.json", "r", encoding="utf-8") as archivo:
              planta= json.load(archivo)
      return planta
   except FileNotFoundError:
     print("No se encontró el archivo de la planta")

   except json.JSONDecodeError:
     print("El archivo JSON contiene datos inválidos")



