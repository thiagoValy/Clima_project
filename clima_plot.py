from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


def ler_arquivo(path, datas, altas, baixas, datas_index, altas_index, baixas_index ):
    """Essa função possibilita a leitura de um arquivo CSV.Essa função é para arquivos leitura de temperaturas por datas"""
    """ IMPOTANTE: ao usar a função importe a Biblioteca csv do Python outras Bibliotecas como Datetime, Matplotlib e Path"""
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    heard_row = next(reader)

    #Estrair as informações do arquivo CSV.
    for row in reader:
        data_atual = datetime.strptime(row[datas_index], '%Y-%m-%d')
        try:
            alta = int(row[altas_index])
            baixa = int(row[baixas_index])
        except ValueError:
            print(f"Erro {data_atual}")
        else:   
            altas.append(alta)
            baixas.append(baixa)
            datas.append(data_atual) 

#Adicionado um arquivo para a geração do grafico.
path = Path('sitka_weather_07-2021_simple.csv')
datas, altas, baixas = [], [], []
ler_arquivo(path, datas, altas, baixas, datas_index=2, altas_index=4, baixas_index=5)

#plotar as informações
plt.style.use('seaborn-v0_8')
fig, ax =plt.subplots()
ax.plot(datas, altas, color='red')
ax.plot(datas, baixas, color='blue')

#formatar o grafico.
ax.set_title("Diario de Temperaturas", fontsize=28)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperatura(C°)", fontsize=16)
ax.tick_params(labelsize=16)
    
    
plt.show()
