import seleccion


equipos = [
    {
        "nombre": "Motor principal",
        "potencia_kw": 15,
        "estado": "En revision"
    },
    {
        "nombre": "Boba alimentacion",
        "potencia_kw": 22.5,
        "estado": "En revision"
    },
    {
        "nombre": "Compresor auxiliar",
        "potencia_kw": 18,
        "estado": "operativo"
    }
]


def test_seleccionar_equipo_valido():
    resultado = seleccion.seleccionar_equipo(equipos, 2)

    assert resultado == equipos[1]


def test_seleccionar_equipo_invalido():
    resultado = seleccion.seleccionar_equipo(equipos, 4)

    assert resultado is None