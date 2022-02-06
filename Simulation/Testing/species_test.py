import pytest
from pathlib import Path
from sys import path, set_coroutine_origin_tracking_depth
import logging

path.append(str(Path(__file__).parent.parent.absolute()))

from species import Species
from society import Society

def test_species() -> None:
    logging.basicConfig(filename='specie_test.log', filemode='w', format='%(levelname)s ~ %(asctime)s -> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    #Creando especies y poniendo caracteristicas por defecto
    humano = Species('Humano')
    assert humano.name == 'Humano'
    assert humano.characteristic["Poblacion"]["summation"] == 0
    assert humano.characteristic["Poblacion"]["mean"] == 0
    
    humano.Set_Default_Characteristics()
    assert len(humano.characteristic) == 13
    
    #Testeando caracteristicas
    humano.Change_Characteristic_Value('Poblacion', 50)
    humano.Change_Characteristic_Value('Poblacion', 40)
    assert humano.characteristic['Poblacion']["summation"] == 90
    
    assert len(humano.characteristic) == 13
    humano.Delete_Characteristic('Tamaño')
    assert len(humano.characteristic) == 12
    assert 'size' not in humano.characteristic
    humano.Delete_Characteristic('Tamaño')
    assert len(humano.characteristic) == 12
    
    humano.Change_Characteristic('Tamaño', 2)
    assert humano.characteristic['Tamaño']["initial"] == 2
    assert len(humano.characteristic) == 13
    
    
    alien = Species('Alien')
    assert alien.name == 'Alien'
    assert alien.characteristic["Poblacion"]["summation"] == 0
    
    alien.Set_Default_Characteristics()
    assert len(alien.characteristic) == 13    
    
    alien.Change_Characteristic_Value('Poblacion', 220)
    alien.Change_Characteristic_Value('Poblacion', 250)
    alien.Change_Characteristic_Value('Poblacion', 240)
    assert alien.characteristic['Poblacion']["summation"] == 710
    
    
def test_species_society() -> None:
    logging.basicConfig(filename='specie_test.log', filemode='w', format='%(levelname)s ~ %(asctime)s -> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    #Creando especies y poniendo caracteristicas por defecto
    humano = Species('Humano')
    assert humano.name == 'Humano'
    assert humano.characteristic["Poblacion"]["summation"] == 0
    assert humano.characteristic["Poblacion"]["mean"] == 0
    
    humano.Set_Default_Characteristics()
    assert len(humano.characteristic) == 13
    
    #Creando sociedades y poniendo caracteristicas por defecto
    cubano = Society("cubano", humano)
    yuma = Society("yuma", humano)
    assert humano.Get_Characteristic_Summation("Tamaño") == 2
    assert humano.Get_Characteristic_Mean("Tamaño") == 1
    assert humano.Get_Characteristic_Summation("Poblacion") == 20 
    assert humano.Get_Characteristic_Mean("Poblacion") == 10 
    assert humano.societies == 2 
    
    cubano.Set_Default_Characteristics()
    yuma.Set_Default_Characteristics()
    assert humano.Get_Characteristic_Summation("Tamaño") == 2 
    assert humano.Get_Characteristic_Mean("Tamaño") == 1 
    
    cubano.Change_Characteristic("Poblacion", 10)
    yuma.Change_Characteristic("Poblacion", 30)
    cubano.Change_Characteristic("Poblacion", 25)
    
    assert humano.Get_Characteristic_Summation("Poblacion") == 55
    assert humano.Get_Characteristic_Mean("Poblacion") == 27.5
    
    #Creando especies y poniendo caracteristicas por defecto
    yedi = Species('Yedi')
    assert yedi.name == 'Yedi'
    assert yedi.characteristic["Poblacion"]["summation"] == 0
    assert yedi.characteristic["Poblacion"]["mean"] == 0
    
    yedi.Set_Default_Characteristics()
    yedi.Delete_Characteristic("Tolerancia a Extranjeros")
    assert len(yedi.characteristic) == 12
    
    #Creando sociedades y poniendo caracteristicas por defecto
    extraterrestre = Society("cubano", yedi)
    assert humano.Get_Characteristic_Summation("Tamaño") == 2
    assert humano.Get_Characteristic_Mean("Tamaño") == 1
    assert humano.Get_Characteristic_Summation("Poblacion") == 55 
    assert humano.Get_Characteristic_Mean("Poblacion") == 27.5 
    assert humano.societies == 2 
    assert yedi.Get_Characteristic_Summation("Tamaño") == 1
    assert yedi.Get_Characteristic_Mean("Tamaño") == 1
    assert yedi.Get_Characteristic_Summation("Poblacion") == 10 
    assert yedi.Get_Characteristic_Mean("Poblacion") == 10 
    assert yedi.societies == 1 