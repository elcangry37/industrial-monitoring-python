import json
import presentacion
import datos



def main():
      planta = datos.cargar_planta()
      presentacion.mostrar_datos_planta(planta)
      presentacion.mostrar_equipos(planta["equipos"])
  
  
if __name__ == "__main__":
    main()

