import os
import pathlib
import datetime 

def criarDiretorioPadra(caminho):
    try:
            dataEhora = datetime.datetime.now()
            novoCaminho = caminho + "/" + str(dataEhora.day) + "_" + str(dataEhora.month) + "_" + str(dataEhora.year) + "-" + str(dataEhora.hour) + ":" + str(dataEhora.minute) + ":" + str(dataEhora.second)
            os.mkdir(novoCaminho)
            return novoCaminho
    except OSError:
        print ("Creation of the directory %s failed" % novoCaminho) 
        return False
    else:
        print ("Successfully created the directory %s " % novoCaminho)

def criarDiretorioComNome(caminho, nomeDiretorio):
    try:
        novoCaminho = caminho + "/" + nomeDiretorio
        os.mkdir(novoCaminho)
        return novoCaminho
    except OSError:
        print ("Creation of the directory %s failed" % novoCaminho) 
        return False
    else:
        print ("Successfully created the directory %s " % novoCaminho)

def existeDiretorio(caminho):
    return os.path.isdir(caminho)