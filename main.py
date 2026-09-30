import json
import presentacion
import datos
import seleccion


def main():

      try:
         planta = datos.cargar_planta()

      except FileNotFoundError:
        print("No se encontró el archivo de la planta")
        return

      except json.JSONDecodeError:
        print("El archivo JSON contiene datos inválidos")
        return

      presentacion.mostrar_datos_planta(planta)
      presentacion.mostrar_equipos(planta["equipos"])

      while True:
         try :
            numero= int(input ("Ingrese el equipo que desea buscar:  "))
            equipo_seleccionado = seleccion.seleccionar_equipo(planta["equipos"], numero)

            if equipo_seleccionado is not None:  
               print(f"Equipo seleccionado: {equipo_seleccionado['nombre']}")
               print(f"Potencia: {equipo_seleccionado['potencia_kw']} kW")
               print(f"Estado: {equipo_seleccionado['estado']}")
               break
            else:
                print("selecion no valida") 
                        
         except ValueError: 
               print("Debe ingresar un número entero")
  
if __name__ == "__main__":
    main()

