from random import random

# porcentagemDeVariacaoMin valor minino 0.1
# porcentagemDeVariacaoMax valor aconselhavel até 0.3
def coloracaoVermelhoVariavel(porcentagemDeVariacaoMin ,porcentagemDeVariacaoMax, vermelho, verde, azul):
    valorAleatorio = numeroAleatorio(porcentagemDeVariacaoMin, porcentagemDeVariacaoMax)
    vermelho = int(vermelho * (1.0 + valorAleatorio))
    verde =  int(verde * (1.0 - valorAleatorio))  
    azul = int(azul * (1.0 - valorAleatorio))
    return limitarPixelMaxEMin(vermelho), limitarPixelMaxEMin(verde), limitarPixelMaxEMin(azul)


def limitarPixelMaxEMin(valorPixel):
    if(valorPixel > 255):
        return 255
    elif(valorPixel < 0):
        return 0
    else:
        return valorPixel


def numeroAleatorio(min, max):
    valor = random()
    min = 0.1
    max = 0.4
    valorEscalonado = min + (valor * (max - min))
    return valorEscalonado