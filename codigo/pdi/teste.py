from datasetBruto import *
from fabricarDataset import *
from grupoDeDados import *
from random import randint
from histoEquaDataset import *

dataset = Dataset(CAMINHO_ABSOLUTO_DATASET + '/17_11_2020-9:3:36')
histEquaDataset = HistogramaEqualizationDataset(dataset)
histEquaDataset.aplicarHistogramaTreinoPositivo()
histEquaDataset.aplicarHistogramaTreinoNegativo()
histEquaDataset.aplicarHistogramaValidacaoPositivo()
histEquaDataset.aplicarHistogramaValidacaoNegativo()
'''
datasetBruto = DatasetBruto()
fabricarDataset = FabricarDataset(datasetBruto, CAMINHO_ABSOLUTO_DATASET)
fabricarDataset.criarEstrutura()
fabricarDataset.dividirTreinoEValidacao(0.5, 'ordenado')
fabricarDataset.dividirTreinoPositivoENegativo(0.5)
fabricarDataset.dividirValidacaoPositivoENegativo(0.7)

grupoDeDados = GrupoDeDados(fabricarDataset.pegarNovoDataset())
grupoDeDados.aplicarPigmentacaoTreinoPositivo()
grupoDeDados.aplicarPigmentacaoValidacaoPositivo()
grupoDeDados.mudarParaFormatoPNGTreinoNegativo()
grupoDeDados.mudarParaFormatoPNGValidacaoNegativo()
'''

'''
dataset = Dataset(CAMINHO_ABSOLUTO_DATASET + '/11_11_2020-17:47:10')
##testeList = ['zeron', 'sombras']
lista = dataset.pegarDadosValidacaoNegativo() 
print(lista)
##print(listaVazia(testeList))
'''