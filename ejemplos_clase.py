#!/usr/bin/env python
'''
Matplotlib [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import matplotlib.pyplot as plt


def line_plot():
    years = [1900, 1970, 1990, 2000, 2020]
    poblacion = [1650, 3692, 5263, 6070, 7800]

    # Realizaremos un gráfico "plot" con:
    # years como "x"
    # poblacion como "y"
    fig = plt.figure()
    fig.suptitle('Población histórica mundial', fontsize=16)
    ax = fig.add_subplot()

    ax.plot(years, poblacion, c='darkgreen', label='poblacion')
    ax.legend()
    ax.grid()
    plt.show()
    print("Fin line plot")


def multi_line_plot():
    mes = [3, 4, 5, 6]
    gasto_carne = [1650, 2600, 3100, 4000]
    gasto_verdura = [2500, 2200, 1800, 600]

    # Calcular el gasto total como la suma
    # de las listas gasto_carne y gasto_verdura
    gasto_total = []
    for i in range(len(gasto_carne)):
        total = gasto_carne[i] + gasto_verdura[i]
        gasto_total.append(total)

    # Realizaremos un gráfico "plot" con:
    # mes como "x"
    # gasto_carne como "y1"
    # gasto_cargasto_verdurane como "y2"
    # gasto_total como "y3"
    fig = plt.figure()
    fig.suptitle('Gastos mensuales', fontsize=16)
    ax = fig.add_subplot()

    ax.plot(mes, gasto_carne, label='carne')
    ax.plot(mes, gasto_verdura, label='verdura')
    ax.plot(mes, gasto_total, label='total')
    ax.legend()
    ax.grid()
    plt.show()
    print("Fin multi line plot")


def scatter_plot():
    years = []
    poblacion = []

    # Los datos en el archivo poblacion
    # no estan ordenados por año
    with open('poblacion.csv') as fi:
        data = csv.DictReader(fi)
        for line in data:
            years.append(int(line['year']))
            poblacion.append(int(line['poblacion']))

    fig = plt.figure()
    fig.suptitle('Población histórica mundial', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)  # 1 fila, 2 columnas, axes nº1
    ax2 = fig.add_subplot(1, 2, 2)  # 1 fila, 2 columnas, axes nº2

    # Como los datos no están ordenados por año
    # el plot no funcionará bien en este caso
    ax1.plot(years, poblacion, c='darkgreen')
    ax1.legend()
    ax1.grid()

    ax2.scatter(years, poblacion, c='darkred')
    ax2.legend()
    ax2.grid()
    plt.show()
    print("Fin scatter plot")


def bar_plot():
    years = []
    poblacion = []
    objetivos = [2000, 2005, 2010, 2015, 2020]

    # Los datos en el archivo poblacion
    # no estan ordenados por año
    with open('poblacion.csv') as fi:
        data = csv.DictReader(fi)
        for line in data:
            year = int(line['year'])
            # Filtramos los datos por un criterio de búsqueda
            if year in objetivos:
                years.append(year)
                poblacion.append(int(line['poblacion']))

    # Here's how it works:
    #                       1- The code reads a CSV file named 'poblacion.csv' using csv.DictReader(fi).
    # This function treats the first row of the CSV file as the header and creates a dictionary 
    # {'key': value} for each subsequent row, where the keys of the dictionary are the header column
    # names, and the values are the corresponding values in each row.
    # The code then iterates over each line (row) in the data object (which represents the CSV 
    # file's contents AS A LIST OF DICTIONARIES) using the for line in data loop.
    # Within each iteration, the 'year' field is extracted from the line dictionary and converted to
    # an integer using int(line['year']). This value is assigned to the year variable.
    # The code checks if the year value is present in the objetivos list using the if year in
    # objetivos condition. If the condition is true (i.e., the year is in objetivos), the following
    # code block is executed.
    # Inside the code block, the year value is appended to the years list using years.append(year).
    # Similarly, the 'poblacion' value from the line dictionary is extracted, converted to an
    # integer, and appended to the poblacion list using poblacion.append(int(line['poblacion'])).

    # This line appends the population value corresponding to the current year to the poblacion list.
    # In summary, the code appends the 'poblacion' value to the poblacion list only if the
    # corresponding 'year' value is present in the objetivos list. It ensures that the population
    # value is associated with the desired year of interest.
    
    fig = plt.figure()
    fig.suptitle('Población histórica mundial', fontsize=16, label='poblacion')
    ax = fig.add_subplot()

    ax.bar(years, poblacion)
    ax.legend()
    ax.grid()
    plt.show()
    print("Fin bar plot")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    line_plot()
    multi_line_plot()
    scatter_plot()
    bar_plot()
