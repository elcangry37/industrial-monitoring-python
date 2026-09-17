def mostrar_datos_planta (planta):

      print(f"Planta: ",planta["nombre"])
      print(f"Estado: ",planta["estado"])
      print(f"Ubicacion: ",planta["ubicacion"])
      print(f"Responsable: ",planta["responsable"])


def mostrar_equipos(equipos):

  for equipo in equipos:
      print(
          f"{equipo['nombre']} - "
          f"{equipo['potencia_kw']} kW - "
          f"{equipo['estado']}"
    )
