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
    plt.ylabel("Temperatura (ºC)")
    plt.xlabel("Dia")
    plt.xticks(range(1,29))
    plt.title("Temperatura mitjana de febrer 2022")
    plt.show()
    return mitjanes
                
#print(temp_mitjana_febrer(estacions, detall_estacions, metadades))

def predict_temp_mitjana_febrer_2023(estacions: numpy.ndarray, detall_estacions: numpy.ndarray, metadades: numpy.ndarray):
    mitjanes = temp_mitjana_febrer(estacions, detall_estacions, metadades)
# Supongamos que tienes una lista de temperaturas medias diarias para febrero de 2022
    temperaturas_febrero_2022 = numpy.array(mitjanes)[:,1]
    # Crear un histograma para visualizar la distribución de las temperaturas de febrero de 2022
    plt.hist(temperaturas_febrero_2022, bins=range(-10, 26), edgecolor='black')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas en febrero de 2022')
    plt.show()

    # Calcular la media y la desviación estándar de las temperaturas de febrero de 2022
    media = numpy.mean(temperaturas_febrero_2022)
    desviacion_estandar = numpy.std(temperaturas_febrero_2022)

    # Generar valores aleatorios para febrero de 2023 basados en la distribución de 2022
    temperaturas_febrero_2023 = numpy.random.normal(media, desviacion_estandar, 28)  # Suponiendo 28 días en febrero

    # Graficar la distribución de las temperaturas de febrero de 2023
    plt.hist(temperaturas_febrero_2023, bins=range(-10, 26), edgecolor='black')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas en febrero de 2023')
    plt.show()

print(predict_temp_mitjana_febrer_2023(estacions, detall_estacions, metadades))
