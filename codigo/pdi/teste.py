from datasetBruto import *
from fabricarDataset import *
from grupoDeDados import *
from random import randint


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
dataset = Dataset(CAMINHO_ABSOLUTO_DATASET + '/11_11_2020-17:47:10')
##testeList = ['zeron', 'sombras']
lista = dataset.pegarDadosValidacaoNegativo() 
print(lista)
##print(listaVazia(testeList))
'''