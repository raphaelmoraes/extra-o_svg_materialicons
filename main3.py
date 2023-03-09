#listar todos os arquivos de um diretorio

import os


arquivos = os.listdir('C:/Users/Raphael/Desktop/outlined/')
for arquivo in arquivos:
    #renomear os arquivos para o padrao nome do arquivo + _outlined
    #se o arquivo ja conttiver _outlined, nao renomear
    if '_outlined' not in arquivo:
        os.rename('C:/Users/Raphael/Desktop/outlined/'+arquivo, 'C:/Users/Raphael/Desktop/outlined/'+arquivo[:-4]+'_outlined'+arquivo[-4:])