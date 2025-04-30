# Importando as bibliotécas a serem utilizadas
import pandas as pd
import numpy as np
from datetime import datetime

#Criando uma função para validar se a entrada de datas está conforme o formato mencionado 
def valida_data():
    while True:
        try:
            data_range  = input("Digite o período de vendas a ser sorteado no formato de AAAA/MM/DD: ")            
            if data_range:
                data = datetime.strptime(data_range,"%Y-%m-%d")
                return data
        except ValueError:
            print("Digite um formato válido para o perído escolhido")

#Criando uma função para validar se a entrada de temperatura condizente com a realidade
def valida_temp():
    while True:
        try:
           
           temp_range  = input("Digite as várição de temperatura desejada e ºC entre 24 a 50: ")

           if temp_range:
               temp_range=int(temp_range)
               if 24 <= temp_range <= 50:
                temp = temp_range
                return temp
               else:
                   print('Digite uma temperatura entre 24 e 50 ºC')
        except ValueError:
            print('Entrada de valores invalidas')
                
#Criando uma função para validar se a entrada de linhas da base está entre 100 e 1000
def rows_validation():
    while True:
        try:
           linhas_range  = input("Digite a quantidade linhas desejadas para o base de dados: ")
           if linhas_range:
               linhas_range = int(linhas_range)
               if 100 <= linhas_range <= 1000:
                linhas = linhas_range
                return linhas
               else:
                   print('Digite um valor entre 100 e 1000')
        except ValueError:
            print('Entrada de valores invalidas')

# Atribuindo valores de data, linhas e temperatura a variaveis utilizando as funções
data_inc  = valida_data()            
data_fim  = valida_data()
temp_inic = valida_temp()
temp_fim  = valida_temp()
qt_rows  = rows_validation()
nm_arquivo = input('Digite o nome do arquivo: ')

# Gerando as datas com base na inserção do usuário, para a quntidade de linhas desejada
datas = pd.date_range(start=data_inc, end=data_fim, periods=qt_rows)

# Gerando temperaturas entre os valores digitados pelo usuário.
temperaturas = np.round(np.random.uniform(temp_inic, temp_fim, size=qt_rows), 0)

# Gerando vendas baseadas na temperatura (mais quente = mais vendas)
vendas = np.random.uniform(0,5, size=qt_rows).astype(int)

# Criando o DataFrame
df = pd.DataFrame({
    "Data": datas.strftime('%Y-%m-%d'),
    "Vendas ": vendas,
    
})

# Salvando em CSV
caminho_csv = f'dados/{nm_arquivo}.csv'
df.to_csv(caminho_csv, index=False)
caminho_csv