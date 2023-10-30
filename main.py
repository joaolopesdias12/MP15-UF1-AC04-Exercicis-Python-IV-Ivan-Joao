import matplotlib.pyplot as plt
import numpy
import csv

# Exercici 2: Carregar dades
def getMatrixFromFile(fileName):
    file = open(fileName, 'r')
    reader = csv.reader(file)
    header = next(reader)  # skip the header row if it exists
    myList = [ row for row in reader]
    ndarray = numpy.array(list(myList))
    file.close()
    return ndarray

estacions = getMatrixFromFile('CSV/2020_MeteoCat_Estacions.csv')
detall_estacions = getMatrixFromFile('CSV/2022_MeteoCat_Detall_Estacions.csv')
metadades = getMatrixFromFile('CSV/MeteoCat_Metadades.csv')
print(estacions.shape)
print(detall_estacions.shape)
print(metadades.shape)

# Exercici 3: Temperatura mitjana de febrer
def temp_mitjana_febrer(estacions: numpy.ndarray, detall_estacions: numpy.ndarray, metadades: numpy.ndarray):
    dies_temperatures = {}
    for row in detall_estacions:
        data = row[0]
        tm = row[3]
        dia = data.split("-")[2]
        mes = data.split("-")[1]
        # Relate days with average temperature
        if mes == "02" and tm == "TM":
            dia_int = int(dia)
            temperatura = float(row[4])
            if dia_int not in dies_temperatures:
                dies_temperatures[dia_int] = []
            dies_temperatures[dia_int].append(temperatura)
    mitjanes = []
    for dia, temperatures in dies_temperatures.items():
        mitjana = sum(temperatures) / len(temperatures)
        mitjanes.append((dia, mitjana))
    # Create a numpy array from the list of mitjanes and create a plot
    print(numpy.array(mitjanes))
    plt.plot(numpy.array(mitjanes)[:,0], numpy.array(mitjanes)[:,1])
    plt.xticks(range(1,29))
    plt.title("Temperatura mitjana de febrer")
    plt.show()
                
    




print(temp_mitjana_febrer(estacions, detall_estacions, metadades))