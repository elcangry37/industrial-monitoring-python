def seleccionar_equipo(equipos, numero):

            if numero >= 1 and numero <= len(equipos):
               equipo_seleccionado = equipos[numero-1]
               return equipo_seleccionado
            else:        
               return None


