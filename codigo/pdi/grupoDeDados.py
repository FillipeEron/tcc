from imagem import *
from pigmentacao import *

class GrupoDeDados():
    def __init__(self, dataset):
        self.DATASET = dataset

    def aplicarPigmentacaoTreinoPositivo(self):
       dadosTreinoPositivo = self.DATASET.pegarDadosTreinoPositivo()  

       for dado in dadosTreinoPositivo:
           imagem = Imagem(dado)
           pigmentacao = Pigmentacao(imagem)
           pigmentacao.aplicacaoAleatoria(60)
           pigmentacao.moldeQuadratico()
           pigmentacao.tipoVermelhoVariavel(0.1, 0.5)
           pigmentacao.iniciarPigmentacao()
           pigmentacao.encerrarProcesso()
           imagem.salvarImagemFormatoPNG(self.DATASET.pegarCaminhoAbsolutoTreinoPositivo())
           imagem.excluirImagem()
    
    def aplicarPigmentacaoValidacaoPositivo(self):
        dadosValidacaoPositivo = self.DATASET.pegarDadosValidacaoPositivo()

        for dado in dadosValidacaoPositivo:
           imagem = Imagem(dado)
           pigmentacao = Pigmentacao(imagem)
           pigmentacao.aplicacaoAleatoria(60)
           pigmentacao.moldeQuadratico()
           pigmentacao.tipoVermelhoVariavel(0.1, 0.5)
           pigmentacao.iniciarPigmentacao()
           pigmentacao.encerrarProcesso()
           imagem.salvarImagemFormatoPNG(self.DATASET.pegarCaminhoAbsolutoValidacaoPositivo())
           imagem.excluirImagem()
    
    def mudarParaFormatoPNGTreinoNegativo(self):
        dadosTreinoNegativo = self.DATASET.pegarDadosTreinoNegativo()
        
        for dado in dadosTreinoNegativo:    
            imagem = Imagem(dado)
            imagem.salvarImagemFormatoPNG(self.DATASET.pegarCaminhoAbsolutoTreinoNegativo())
            imagem.excluirImagem()

    def mudarParaFormatoPNGValidacaoNegativo(self):
        dadosValidacaoNegativo = self.DATASET.pegarDadosValidacaoNegativo()

        for dado in dadosValidacaoNegativo:
            imagem = Imagem(dado)
            imagem.salvarImagemFormatoPNG(self.DATASET.pegarCaminhoAbsolutoValidacaoNegativo())
            imagem.excluirImagem()   