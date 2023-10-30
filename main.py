import matplotlib.pyplot as plt
import numpy
import csv


# Estacions
with open('CSV/2020_MeteoCat_Estacions.csv') as csvfile_estacions:
    dades_estacions = list(csv.DictReader(csvfile_estacions))
    list_dades = list(dades_estacions)
    ndarray_estacions = []
    for fila in list_dades:
        ndarray_estacions.append(fila)
    ndarray_estacions = numpy.array(ndarray_estacions)

# Detall Estacions
with open('CSV/2022_MeteoCat_Detall_Estacions.csv') as csvfile_detall_estacions:
    dades_detall = list(csv.DictReader(csvfile_detall_estacions))

    ndarray_detall_estacions = list()
    for fila in dades_detall:
        ndarray_detall_estacions.append(fila)
    ndarray_detall_estacions = numpy.array(ndarray_detall_estacions)

# Metadades
with open('CSV/MeteoCat_Metadades.csv') as csvfile_metadades:
    dades_metadades = list(csv.DictReader(csvfile_metadades))
    ndarray_metadades = list()
    for fila in dades_metadades:
        ndarray_metadades.append(fila)
    ndarray_metadades = numpy.array(ndarray_metadades)


#print(ndarray_estacions)
# print forma of matrix
#print("hola")
print(ndarray_estacions[0]["CODI_ESTACIO"])
print(ndarray_estacions.shape)

def temp_mitjana_febrer(ndarray_estacions: list, ndarray_detall_estacions: list, ndarray_metadades: list):
    dies = numpy.array([i for i in range(1, 29)])
    #print(ndarray_detall_estacions)
    print(dies)



temp_mitjana_febrer(ndarray_estacions, ndarray_detall_estacions, ndarray_metadades)