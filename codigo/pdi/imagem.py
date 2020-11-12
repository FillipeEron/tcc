from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from matplotlib.pyplot import imshow
from nomeArquivo import *
import cv2
import os
import pathlib

class Imagem:

    def __init__(self, caminhoDaImage):
        self.CAMINHO_DA_IMAGEM = caminhoDaImage
        self.carregarImage(caminhoDaImage)

    def carregarImage(self, caminhoDaImage):
        self.IMAGEM_CARREGADA = Image.open(caminhoDaImage)

    def salvarImagem(self, novoCaminhoDaImage, nome):
        self.IMAGEM_CARREGADA.save(novoCaminhoDaImage + "/" + nome)

    # Alteracao feitas na imagem persistem apenas no formato png
    def salvarImagemFormatoPNG(self, novoCaminhoDaImage):
        nomeFinalPNG = alterarPrefixoArquivo(self.CAMINHO_DA_IMAGEM, "png")
        self.IMAGEM_CARREGADA.save(novoCaminhoDaImage + "/" + nomeFinalPNG)

    def imprimirImagem(self):
        imshow(np.asarray(self.IMAGEM_CARREGADA))

    def pegarCaminho(self):
        return self.CAMINHO_DA_IMAGEM
    
    def pegarNomeDaImagem(self):
        return pegarNomeDoArquivo(self.CAMINHO_DA_IMAGEM)
    
    def pegarAltura(self):
        largura, altura = self.IMAGEM_CARREGADA.size 
        return altura
    
    def pegarLargura(self):
        largura, altura = self.IMAGEM_CARREGADA.size
        return largura
    
    def pegarImagem(self):
        return self.IMAGEM_CARREGADA
    
    def habilitarEdicao(self):
        self.IMAGEM_EDICAO = ImageDraw.Draw(self.IMAGEM_CARREGADA)

    def modificarPixel(self, pontoX, pontoY, vermelho, verde, azul):
        #red, green, blue = self.IMAGEM_CARREGADA.getpixel((15,15))
        #self.IMAGEM_EDICAO.point((pontoX, pontoY), fill=( int(red * 1.70), int(green * 0.30), int(blue * 0.30)))
        self.IMAGEM_EDICAO.point((pontoX, pontoY), fill=( vermelho, verde, azul))
    
    def pegarValorPixelRGB(self, pontoX, pontoY):
        vermelho, verde, azul = self.IMAGEM_CARREGADA.getpixel((pontoX, pontoY))
        return vermelho, verde, azul

    def imprimirMetadados(self):
        print("Formato: " + self.IMAGEM_CARREGADA.format)
        print("Modo: " + self.IMAGEM_CARREGADA.mode)
        print("Tamanho: " + str(self.IMAGEM_CARREGADA.size))

    def excluirImagem(self):
        os.remove(self.CAMINHO_DA_IMAGEM)