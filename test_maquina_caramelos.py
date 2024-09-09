import pytest
from codigo_pruebas import MaquinaDeCaramelos

def test_fabricar_caramelo_limon():
    maquina = MaquinaDeCaramelos()
    resultado = maquina.fabricar_caramelo_limon(10)
    assert resultado == "SE ESTAN PRODUCIENDO 10 CARAMELOS SABOR A LIMÓN"
    assert maquina.mezcla_ingredientes == {
        "azucar": 30,
        "agua": 20,
        "colorante amarillo": 20,
        "saborizante de limon": 50
    }

def test_fabricar_caramelo_naranja():
    maquina = MaquinaDeCaramelos()
    resultado = maquina.fabricar_caramelo_naranja(10)
    assert resultado == "SE ESTAN PRODUCIENDO 10 CARAMELOS SABOR A NARANJA"
    assert maquina.mezcla_ingredientes == {
        "azucar": 30,
        "agua": 20,
        "colorante anaranjado": 20,
        "saborizante de naranja": 50
    }

def test_aumentar_produccion():
    maquina = MaquinaDeCaramelos()
    nueva_produccion = maquina.aumentar_produccion()
    assert nueva_produccion == 600
    nueva_produccion = maquina.aumentar_produccion()
    assert nueva_produccion == 700

def test_mostrar_ingredientes_despues_de_fabricar():
    maquina = MaquinaDeCaramelos()
    maquina.fabricar_caramelo_limon(10)
    ingredientes = maquina.mostrar_ingredientes()
    assert ingredientes == {
        "azucar": 30,
        "agua": 20,
        "colorante amarillo": 20,
        "saborizante de limon": 50



    }