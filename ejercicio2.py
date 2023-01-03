# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import requests
import matplotlib.pyplot as plt



if __name__ == '__main__':
        print("Bienvenidos a otra clase de Inove con Python")
data = []
usuario = []
cant_completo = [] 
response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()
y = 0
x = 1
for user in data:
        if user['completed'] == True:
                y = y + 1  
        if user['userId'] != x :
                x = user ['userId']
                usuario.append (x)
                cant_completo.append(y)
                y = 0


fig = plt.figure() 

ax = fig.add_subplot()
ax.bar(usuario,cant_completo, color="green", label="N° de Usuario")
ax.set_title("Titulos Completados")
ax.set_ylabel(" Titulos ")
ax.set_xlabel(" Usuarios ")
ax.legend()
plt.xticks(usuario)
plt.show() 
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes        
    # Ejercicio de consumo de datos por AP
    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

print("terminamos")