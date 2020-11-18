from imagem import *
import cv2

class HistogramaEqualizationDataset():
    def __init__(self, dataset):
        self.DATASET = dataset
    
    def aplicarHistogramaTreinoPositivo(self):
       dadosTreinoPositivo = self.DATASET.pegarDadosTreinoPositivo()  

       for dado in dadosTreinoPositivo:
           
           imagem = Imagem(dado)
           imagemCv = cv2.imread(str(dado))
           lab = cv2.cvtColor(imagemCv, cv2.COLOR_BGR2LAB)
           lab_planes = cv2.split(lab)
           clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
           lab_planes[0] = clahe.apply(lab_planes[0])
           lab = cv2.merge(lab_planes)
           imagemCv = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
           
           cv2.imwrite(self.DATASET.pegarCaminhoAbsolutoTreinoPositivo() + '/clahe-' + imagem.pegarNomeDaImagem(), imagemCv)
           
           imagem.excluirImagem()
    
    def aplicarHistogramaTreinoNegativo(self):
       dadosTreinoNegativo = self.DATASET.pegarDadosTreinoNegativo()  

       for dado in dadosTreinoNegativo:
           
           imagem = Imagem(dado)
           imagemCv = cv2.imread(str(dado))
           lab = cv2.cvtColor(imagemCv, cv2.COLOR_BGR2LAB)
           lab_planes = cv2.split(lab)
           clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
           lab_planes[0] = clahe.apply(lab_planes[0])
           lab = cv2.merge(lab_planes)
           imagemCv = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
           
           cv2.imwrite(self.DATASET.pegarCaminhoAbsolutoTreinoNegativo() + '/clahe-' + imagem.pegarNomeDaImagem(), imagemCv)
           
           imagem.excluirImagem()
    
    def aplicarHistogramaValidacaoPositivo(self):
       dadosValidacaoPositivo = self.DATASET.pegarDadosValidacaoPositivo()  

       for dado in dadosValidacaoPositivo:
           
           imagem = Imagem(dado)
           imagemCv = cv2.imread(str(dado))
           lab = cv2.cvtColor(imagemCv, cv2.COLOR_BGR2LAB)
           lab_planes = cv2.split(lab)
           clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
           lab_planes[0] = clahe.apply(lab_planes[0])
           lab = cv2.merge(lab_planes)
           imagemCv = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
           
           cv2.imwrite(self.DATASET.pegarCaminhoAbsolutoValidacaoPositivo() + '/clahe-' + imagem.pegarNomeDaImagem(), imagemCv)
           
           imagem.excluirImagem()
    
    def aplicarHistogramaValidacaoNegativo(self):
       dadosValidacaoNegativo = self.DATASET.pegarDadosValidacaoNegativo()  

       for dado in dadosValidacaoNegativo:
           
           imagem = Imagem(dado)
           imagemCv = cv2.imread(str(dado))
           lab = cv2.cvtColor(imagemCv, cv2.COLOR_BGR2LAB)
           lab_planes = cv2.split(lab)
           clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
           lab_planes[0] = clahe.apply(lab_planes[0])
           lab = cv2.merge(lab_planes)
           imagemCv = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
           
           cv2.imwrite(self.DATASET.pegarCaminhoAbsolutoValidacaoNegativo() + '/clahe-' + imagem.pegarNomeDaImagem(), imagemCv)
           
           imagem.excluirImagem()