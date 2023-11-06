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

# Funció per calcular la mitjana segons el acrònim
def calcular_mitjana(filtre: str) -> list:
    dies = {}
    for row in detall_estacions:
        data = row[0]
        acronim = row[3]
        dia = data.split("-")[2]
        mes = data.split("-")[1]
        # Filtrem les dades de febrer i amb l'acrònim 
        if mes == "02" and acronim == filtre.upper():
            dia_int = int(dia)
            valor = float(row[4])
            if dia_int not in dies:
                dies[dia_int] = []
            dies[dia_int].append(valor)
    mitjanes = []
    for dia, valors in dies.items():
        mitjana = sum(valors) / len(valors)
        mitjanes.append((dia, mitjana))

    return mitjanes

# Exercici 3: Temperatura mitjana de febrer
def temp_mitjana_febrer():
    mitjanes = calcular_mitjana("TM")
    # Create a numpy array from the list of mitjanes and create a plot
    print(numpy.array(mitjanes))
    plt.plot(numpy.array(mitjanes)[:,0], numpy.array(mitjanes)[:,1])
    plt.ylabel("Temperatura (ºC)")
    plt.xlabel("Dia")
    plt.xticks(range(1,29))
    plt.title("Temperatura mitjana de febrer 2022")
    plt.show()
                
print(temp_mitjana_febrer())

def predict_temp_mitjana_febrer_2023():
    
    mitjanes = calcular_mitjana("TM")

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

print(predict_temp_mitjana_febrer_2023())

def predict_pluja_febrer_2023():
    
    precipitacio_mitjana_febrero_2022 = numpy.array(calcular_mitjana("PPT"))


    # Umbral de lluvia para considerar si lloverá en 2023
    umbral_lluvia = 5

    # Predicción para febrero de 2023 en formato booleano
    lluvia_2023 = precipitacio_mitjana_febrero_2022 > umbral_lluvia
    print(lluvia_2023)

    # Calcular la proporción de días de lluvia y días sin lluvia
    dias_lluvia = numpy.sum(lluvia_2023)
    dias_sin_lluvia = len(lluvia_2023) - dias_lluvia

    # Sectors
    labels = 'SI', 'NO'
    valors = [dias_lluvia, dias_sin_lluvia]
    plt.pie(valors, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Per a que el sector es dibuixi com a cercle

    plt.title("Proporció de dies de pluja pel Febrer 2023")
    plt.show()

    # Barres barh
    dias = numpy.arange(1, len(lluvia_2023) + 1)
    print(dias)
    plt.barh(dias, valors)
    plt.xlabel("Lluvia (SÍ o NO)")
    plt.ylabel("Dies de Febrero de 2023")
    plt.title("Proporció de dies de pluja pel Febrer 2023")
    plt.yticks(dias, [str(d) for d in dias])
    plt.show()
   
    

print(predict_pluja_febrer_2023())


