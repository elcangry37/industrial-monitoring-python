import calculos

def test_calcular_consumo_kwh():
    resultado=calculos.calcular_consumo_kwh(15,8)
    assert resultado==120,"El calculo del consumo es incorrecto"


