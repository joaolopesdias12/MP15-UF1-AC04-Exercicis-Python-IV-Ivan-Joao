import matplotlib.pyplot as plt
import numpy
import csv


# Estacions
with open('CSV/2020_MeteoCat_Estacions.csv') as csvfile_estacions:
    dades_estacions = list(csv.DictReader(csvfile_estacions))
    list_dades = list(dades_estacions)
    ndarray_estacions = numpy.ndarray(shape=(len(dades_estacions), 2), offset=numpy.int_().itemsize)
    for i, fila in enumerate(list_dades):
        ndarray_estacions[i] = [fila['CODI'], fila['NOM']]

# Detall Estacions
with open('CSV/2022_MeteoCat_Detall_Estacions.csv') as csvfile_detall_estacions:
    dades_detall = list(csv.DictReader(csvfile_detall_estacions))

    ndarray_detall_estacions = numpy.ndarray(shape=len(dades_detall),offset=numpy.int_().itemsize)
    for fila in dades_detall:
        ndarray_detall_estacions = numpy.append(ndarray_detall_estacions, fila)
        ndarray_detall_estacions = ndarray_detall_estacions.reshape((len(dades_detall)))

# Metadades
with open('CSV/MeteoCat_Metadades.csv') as csvfile_metadades:
    dades_metadades = list(csv.DictReader(csvfile_metadades))
    ndarray_metadades = numpy.ndarray(shape=len(dades_metadades),offset=numpy.int_().itemsize)
    for fila in dades_metadades:
        ndarray_metadades = numpy.append(ndarray_metadades, fila)
    ndarray_metadades = ndarray_metadades.reshape((len(dades_metadades)))


print(ndarray_estacions)
# print forma of matrix
print(ndarray_estacions.shape)

def temp_mitjana_febrer(ndarray_estacions: list, ndarray_detall_estacions: list, ndarray_metadades: list):
    dies = numpy.array([i for i in range(1, 29)])
    #print(ndarray_detall_estacions)



temp_mitjana_febrer(ndarray_estacions, ndarray_detall_estacions, ndarray_metadades)