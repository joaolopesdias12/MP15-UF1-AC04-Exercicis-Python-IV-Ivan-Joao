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


# Funció per calcular la mitjana segons el acrònim
def calcular_mitjana(filtre_acronim: str, filtre_codi: str) -> list:
    dies = {}
    for row in detall_estacions:
        data = row[0]
        acronim = row[3]
        dia = data.split("-")[2]
        mes = data.split("-")[1]
        codi_stacio = row[2]
        # Filtrem les dades de febrer i amb l'acrònim 
        if mes == "02" and acronim == filtre_acronim.upper() and (codi_stacio == filtre_codi or filtre_codi == "TOTS"):
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
    mitjanes_totes = numpy.array(calcular_mitjana("TM", "TOTS"))
    mitjanes_d5 = numpy.array(calcular_mitjana("TM", "D5"))
    mitjanes_x4 = numpy.array(calcular_mitjana("TM", "X4"))
    mitjanes_x8 = numpy.array(calcular_mitjana("TM", "X8"))
    mitjanes_x2 = numpy.array(calcular_mitjana("TM", "X2"))
    
    # Dies i temperatures de totes les estacions
    plt.plot(mitjanes_totes[:,0], mitjanes_totes[:,1], marker='o', linestyle='-', color='black')
    plt.title("Temperatura mitjana febrer 2022")
    plt.xlabel("Dies")
    plt.xticks(range(1,29))
    plt.ylabel("Temperatura ºC")
    plt.grid(True)
    plt.show()

    plt.plot(mitjanes_d5[:,0], mitjanes_d5[:,1], label='Estació D5', marker='o', linestyle='-', color='blue')
    plt.plot(mitjanes_x4[:,0], mitjanes_x4[:,1], label='Estació X4', marker='o', linestyle='-', color='red')
    plt.plot(mitjanes_x8[:,0], mitjanes_x8[:,1], label='Estació X8', marker='o', linestyle='-', color='green')
    plt.plot(mitjanes_x2[:,0], mitjanes_x2[:,1], label='Estació X2', marker='o', linestyle='-', color='orange')
    plt.legend()
    plt.title("Temperatura mitjana febrer 2022 per estació")
    plt.xlabel("Dies")
    plt.xticks(range(1,29))
    plt.ylabel("Temperatura ºC")
    plt.grid(True)

    plt.show()

    # Per estació
    fig, axes = plt.subplots(4, 1, figsize=(10, 10), sharex=True, sharey=True)

    axes[0].plot(mitjanes_d5[:,0], mitjanes_d5[:,1], label='Estació D5', marker='o', linestyle='-', color='blue')
    axes[0].set_title('Estació D5')

    axes[1].plot(mitjanes_d5[:,0], mitjanes_x4[:,1], label='Estació X4', marker='o', linestyle='-', color='red')
    axes[1].set_title('Estació X4')

    axes[2].plot(mitjanes_d5[:,0], mitjanes_x8[:,1], label='Estació X8', marker='o', linestyle='-', color='green')
    axes[2].set_title('Estació X8')

    axes[3].plot(mitjanes_x2[:,0], mitjanes_x2[:,1], label='Estació X2', marker='o', linestyle='-', color='orange')
    axes[3].set_title('Estació X2')
    
    for ax in axes:
        ax.set_xlabel('Dies')
        ax.set_xticks(range(1,29))
        ax.set_ylabel('Temperatura Mitjana (°C)')
        ax.grid(True)

    plt.tight_layout()
    plt.show()

#print(temp_mitjana_febrer())

def predict_temp_mitjana_febrer_2023():
    
    mitjanes = calcular_mitjana("TM", "TOTS")

    temperaturas_febrero_2022 = numpy.array(mitjanes)[:,1]
    
    # Crear un histograma para visualizar la distribución de las temperaturas de febrero de 2022
    plt.hist(temperaturas_febrero_2022, bins=range(8, 22), edgecolor='black', color="orange")
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Freqüència (Dies)')
    plt.grid(True)
    plt.title('Distribució de temperatures de febrer de 2022')
    plt.show()

    # Calcular la media y la desviación estándar de las temperaturas de febrero de 2022
    media = numpy.mean(temperaturas_febrero_2022)
    desviacion_estandar = numpy.std(temperaturas_febrero_2022)

    # Generar valores aleatorios para febrero de 2023 basados en la distribución de 2022
    temperaturas_febrero_2023 = numpy.random.normal(media, desviacion_estandar, 28)  # Suponiendo 28 días en febrero

    # Graficar la distribución de las temperaturas de febrero de 2023
    plt.hist(temperaturas_febrero_2023, bins=range(8, 22), edgecolor='black')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Freqüència (Dies)')
    plt.grid(True)
    plt.title('Distribució de temperatures de febrer de 2023')
    plt.show()

#print(predict_temp_mitjana_febrer_2023())

def predict_pluja_febrer_2023():
    
    precipitacio_mitjana_febrero_2022 = numpy.array(calcular_mitjana("PPT", "TOTS"))
    print(precipitacio_mitjana_febrero_2022)

    
    # Calcular la proporción de días de lluvia y días sin lluvia
    dias_lluvia = numpy.count_nonzero(precipitacio_mitjana_febrero_2022[:,1])

    dias_sin_lluvia = len(precipitacio_mitjana_febrero_2022) - dias_lluvia
    mitjana_precipitacio = numpy.mean(precipitacio_mitjana_febrero_2022[:,1])
    desviacion_estandar = numpy.std(precipitacio_mitjana_febrero_2022[:,1])

    print(mitjana_precipitacio)
    print(desviacion_estandar)
    # Sectors
    labels = 'SI', 'NO'
    valors = [dias_lluvia, dias_sin_lluvia]
    plt.pie(valors, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Per a que el sector es dibuixi com a cercle

    plt.title("Proporció de dies de pluja pel Febrer 2023")
    plt.show()

    # Barres barh
    dias = numpy.arange(1, len(precipitacio_mitjana_febrero_2022) + 1)
    plt.barh(dias, valors)
    plt.xlabel("Lluvia (SÍ o NO)")
    plt.ylabel("Dies de Febrer de 2023")
    plt.title("Proporció de dies de pluja pel Febrer 2023")
    plt.yticks(dias, [str(d) for d in dias])
    plt.show()
   
    

print(predict_pluja_febrer_2023())


