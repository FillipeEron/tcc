from formatoPigmentacao import *
from imagem import *
from coloracaoPigmentacao import *
from random import randint


class Pigmentacao():

    PONTOS_TOTAIS_APLICACAO = set ()
    PONTOS_SECUNDARIOS_APLICACAO = set()
    PONTOS_CENTRAIS_APLICACAO = set()

    def __init__(self, imagem):
        self.IMAGEM = imagem

    def aplicacaoAleatoria(self, quantidade):
        # Algoritmo com possibilidade de gerar a mesma coordenada mais de uma vez
        for i in range(quantidade):
            x = self.numeroAleatorioInteiro(0, self.IMAGEM.pegarLargura() + 1)
            y = self.numeroAleatorioInteiro(0, self.IMAGEM.pegarAltura() + 1)
            self.PONTOS_CENTRAIS_APLICACAO.add((x,y))

    def aplicacaoDeterminada(self, coordenadasDeAplicacao):
        self.PONTOS_CENTRAIS_APLICACAO.add(coordenadasDeAplicacao) 

    def moldeQuadratico(self):
        for ponto in self.PONTOS_CENTRAIS_APLICACAO:
            self.PONTOS_SECUNDARIOS_APLICACAO = self.PONTOS_SECUNDARIOS_APLICACAO.union(formatoQuadratico(ponto[0], ponto[1]))

    def tipoVermelhoVariavel(self, porcentagemDeVariacaoMin, porcentagemDeVariacaoMax):
        self.PORCENTAGEM_VARIACAO_MINIMA = porcentagemDeVariacaoMax
        self.PORCENTAGEM_VARIACAO_MAXIMA = porcentagemDeVariacaoMin

    def iniciarPigmentacao(self):
        self.IMAGEM.habilitarEdicao()
        self.totalizarPontosPrimariosESecundarios()
        
        for ponto in self.PONTOS_TOTAIS_APLICACAO:
            vermelho, verde, azul = self.IMAGEM.pegarValorPixelRGB(ponto[0], ponto[1])
            vermelho, verde, azul = coloracaoVermelhoVariavel(self.PORCENTAGEM_VARIACAO_MINIMA, self.PORCENTAGEM_VARIACAO_MAXIMA, vermelho, verde, azul)
            self.IMAGEM.modificarPixel(ponto[0], ponto[1], vermelho, verde, azul)   

    def totalizarPontosPrimariosESecundarios(self):
        self.PONTOS_TOTAIS_APLICACAO = self.PONTOS_CENTRAIS_APLICACAO.union(self.PONTOS_SECUNDARIOS_APLICACAO)
        self.filtrarPontosInvalidos()

    def filtrarPontosInvalidos(self):
        pontosInvalidos = set()
        for ponto in self.PONTOS_TOTAIS_APLICACAO:
            pontoX = ponto[0]
            pontoY = ponto[1]
            if( (pontoX >= self.IMAGEM.pegarLargura()) or (pontoX < 0)):
                pontosInvalidos.add((pontoX, pontoY))
            elif ( (pontoY >= self.IMAGEM.pegarAltura()) or (pontoY < 0) ):
                pontosInvalidos.add((pontoX, pontoY))
        self.PONTOS_TOTAIS_APLICACAO = self.PONTOS_TOTAIS_APLICACAO.difference(pontosInvalidos)

    def pegarPontosTotais(self):
        return self.PONTOS_TOTAIS_APLICACAO

    def pegarPontosSecundarios(self):
        return self.PONTOS_SECUNDARIOS_APLICACAO

    def pegarPontosCentrais(self):
        return self.PONTOS_CENTRAIS_APLICACAO

    def numeroAleatorioInteiro(self, min, max):
        valor = randint(min, max)
        return valor
    
    def encerrarProcesso(self):
        self.PONTOS_CENTRAIS_APLICACAO.clear()
        self.PONTOS_SECUNDARIOS_APLICACAO.clear()
        self.PONTOS_SECUNDARIOS_APLICACAO.clear()