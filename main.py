import matplotlib.pyplot as plt
import numpy as np
import csv


# Estacions
with open('CSV/2020_MeteoCat_Estacions.csv') as csvfile:
    ndarray_estacions = []
    dades = csv.reader(csvfile)
    for i, fila in enumerate(dades):
        ndarray_estacions.append(fila)

# Detall Estacions
with open('CSV/2022_MeteoCat_Detall_Estacions.csv') as csvfile:
    ndarray_detall_estacions = []
    dades = csv.reader(csvfile)
    for i, fila in enumerate(dades):
        ndarray_detall_estacions.append(fila)

# Metadades
with open('CSV/MeteoCat_Metadades.csv') as csvfile:
    ndarray_metadades = []
    dades = csv.reader(csvfile)
    for i, fila in enumerate(dades):
        ndarray_metadades.append(fila)

print(ndarray_estacions)