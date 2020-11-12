from constantes import *
import pathlib
import numpy.random 
import numpy as np

class DatasetBruto():
    def __init__(self):
        self.CAMINHO_ABSOLUTO_DATASET_ORIGINAL = CAMINHO_ABSOLUTO_DATASET_ORIGINAL

    def retornarTodoDataset(self): 
        caminhoAbsolutoDatasetOriginal = pathlib.Path(self.CAMINHO_ABSOLUTO_DATASET_ORIGINAL)
        return list(caminhoAbsolutoDatasetOriginal.glob('*.jpg'))
    
    def retornarTodoDatasetAleatorio(self): 
        caminhoAbsolutoDatasetOriginal = pathlib.Path(self.CAMINHO_ABSOLUTO_DATASET_ORIGINAL)
        listaDeTodoDataset = list(caminhoAbsolutoDatasetOriginal.glob('*.jpg'))
        np.random.shuffle(listaDeTodoDataset)
        return listaDeTodoDataset

    def pegarImagemDataset(self, nomeDaImagem):
        return pathlib.Path(self.CAMINHO_ABSOLUTO_DATASET_ORIGINAL + "/" + nomeDaImagem)

    def pegarQuantTotaldeDados(self):
        return len(self.retornarTodoDataset())

    def listarTodoDataset(self):
        for index, item in enumerate(self.retornarTodoDataset()):
            print(item)