import pathlib

class Dataset():
    def __init__(self, caminhoAbsoluto):
        self.CAMINHO_ABSOLUTO = caminhoAbsoluto

    def pegarCaminhoAbsolutoRaiz(self):
        return self.CAMINHO_ABSOLUTO
    
    def pegarCaminhoAbsolutoTreino(self):
        return self.CAMINHO_ABSOLUTO + "/treino"

    def pegarCaminhoAbsolutoTreinoPositivo(self):
        return self.CAMINHO_ABSOLUTO + "/treino/positivo"
    
    def pegarCaminhoAbsolutoTreinoNegativo(self):
        return self.CAMINHO_ABSOLUTO + "/treino/negativo"

    def pegarCaminhoAbsolutoValidacao(self):
        return self.CAMINHO_ABSOLUTO + "/validacao/"
    
    def pegarCaminhoAbsolutoValidacaoPositivo(self):
        return self.CAMINHO_ABSOLUTO + "/validacao/positivo"
    
    def pegarCaminhoAbsolutoValidacaoNegativo(self):
        return self.CAMINHO_ABSOLUTO + "/validacao/negativo"
    
    def pegarDadosTreinoPositivo(self):
        dadosTreinoPositivo = pathlib.Path(self.pegarCaminhoAbsolutoTreinoPositivo())
        if(self.listaVazia(list(dadosTreinoPositivo.glob('*.jpg')))):
            return list(dadosTreinoPositivo.glob('*.png'))
        else:
            return list(dadosTreinoPositivo.glob('*.jpg'))
    
    def pegarDadosTreinoNegativo(self):
        dadosTreinoNegativo = pathlib.Path(self.pegarCaminhoAbsolutoTreinoNegativo())
        if(self.listaVazia(list(dadosTreinoNegativo.glob('*.jpg')))):
            return list(dadosTreinoNegativo.glob('*.png'))
        else:    
            return list(dadosTreinoNegativo.glob('*.jpg'))
  
    def pegarDadosValidacaoPositivo(self):
        dadosValidacaoPositivo = pathlib.Path(self.pegarCaminhoAbsolutoValidacaoPositivo())
        if(self.listaVazia(list(dadosValidacaoPositivo.glob('*.jpg')))):
            return list(dadosValidacaoPositivo.glob('*.png'))
        else:    
            return list(dadosValidacaoPositivo.glob('*.jpg'))
    
    def pegarDadosValidacaoNegativo(self):
        dadosValidacaoNegativo = pathlib.Path(self.pegarCaminhoAbsolutoValidacaoNegativo())
        if(self.listaVazia(list(dadosValidacaoNegativo.glob('*.jpg')))):
            return list(dadosValidacaoNegativo.glob('*.png'))
        else:
            return list(dadosValidacaoNegativo.glob('*.jpg'))
    
    def listaVazia(self, lista):
        if(bool(lista)):
            return False
        else:
            return True