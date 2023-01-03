# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas
    ropita_json = {
                "nombre": "Ropita",
                "apellido": "De Vestir",
                "DNI": "6666666",
                "prendas": [
                    {
                     "prenda": "zapatillas", "cantidad": 4
                    },
                    {
                     "prenda": "remeras", "cantidad": 12
                    },
                    {
                     "prenda": "pantalones", "cantidad": 5
                    }
                    ]
                }
    # json_data = {...}
    json_string = json.dumps(ropita_json, indent=4)
    print(json_string)
    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina
    with open('json_de_ropita.json', 'w') as jsonfile:
        data = [ropita_json]
        json.dump(data, jsonfile, indent=4)
    # Observe el archivo y verifique que se almaceno lo deseado


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()
    with open('json_de_ropita.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
    json_string = json.dumps(json_data, indent=4)
    print('Mostrar el contenido del archivo mi_json')
    print(json.dumps(json_string, indent=4))

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")