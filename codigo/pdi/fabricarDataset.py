from diretorio import *
from dataset import *
from imagem import *

class FabricarDataset():

    # DADOS DE TREINO
    DADOS_TREINO = []
    DADOS_TREINO_POSITIVO = []
    DADOS_TREINO_NEGATIVO = []
    # DADOS DE VALIDACAO
    DADOS_VALIDACAO = []
    DADOS_VALIDACAO_POSITIVO = []
    DADOS_VALIDACAO_NEGATIVO = []

    def __init__(self, datasetBruto, caminhoNovoDataset):
        self.DATASET_BRUTO = datasetBruto
        self.CAMINHO_NOVO_DATASET =  caminhoNovoDataset

    def divirdirQuantidadeDeDados(self, porcentagem, quantidadeTotalDados):
        grupoUm = int (porcentagem * quantidadeTotalDados)
        grupoDois = quantidadeTotalDados - grupoUm 
        return grupoUm, grupoDois
    
    def criarEstrutura(self):
        self.NOVO_DATASET = Dataset(self.criarEstruturaDiretorioDataset(self.CAMINHO_NOVO_DATASET))

    # Retornar um dicionario com a estrutura do novo dataset
    def criarEstruturaDiretorioDataset(self, caminhoNovoDataset):
        novoDiretorioRaizDataset = criarDiretorioPadra(caminhoNovoDataset)

        if(existeDiretorio(novoDiretorioRaizDataset)):
            dirTreino = criarDiretorioComNome(novoDiretorioRaizDataset,"treino")
            dirValidacao = criarDiretorioComNome(novoDiretorioRaizDataset,"validacao")
        
            if( existeDiretorio(dirTreino) and existeDiretorio(dirValidacao) ):
                dirTreinoPositivo = criarDiretorioComNome(dirTreino, "positivo")
                dirTreinoNegativo = criarDiretorioComNome(dirTreino, "negativo")
                dirValidacaoPositivo = criarDiretorioComNome(dirValidacao, "positivo")
                dirValidacaoNegativo = criarDiretorioComNome(dirValidacao, "negativo")
        return novoDiretorioRaizDataset
    

    def dividirTreinoEValidacao(self, porcentagem, modo):
        self.QUANTIDADE_TREINO, self.QUANTIDADE_VALIDACAO = self.divirdirQuantidadeDeDados(porcentagem, self.DATASET_BRUTO.pegarQuantTotaldeDados())
        if( modo == "ordenado"):
            datasetBruto = self.DATASET_BRUTO.retornarTodoDataset()
        elif(modo == "aleatorio"):
            datasetBruto = self.DATASET_BRUTO.retornarTodoDatasetAleatorio()

        i = 0
        while i <= (self.QUANTIDADE_TREINO - 1):
            self.DADOS_TREINO.append(datasetBruto[i])  
            i+=1
            
        while i <= ( self.QUANTIDADE_TREINO  + self.QUANTIDADE_VALIDACAO - 1):
            self.DADOS_VALIDACAO.append(datasetBruto[i])
            i+=1


    def dividirTreinoPositivoENegativo(self, porcentagem):
        self.QUANTIDADE_TREINO_POSITIVO, self.QUANTIDADE_TREINO_NEGATIVO = self.divirdirQuantidadeDeDados(porcentagem, self.QUANTIDADE_TREINO)
        i = 0
        while i <= (self.QUANTIDADE_TREINO_POSITIVO - 1):
            self.DADOS_TREINO_POSITIVO.append(self.DADOS_TREINO[i])
            i+=1
        
        while i <= (self.QUANTIDADE_TREINO_POSITIVO + self.QUANTIDADE_TREINO_NEGATIVO -1):
            self.DADOS_TREINO_NEGATIVO.append(self.DADOS_TREINO[i])
            i+=1

        self.trasferirDados(self.DADOS_TREINO_POSITIVO, self.NOVO_DATASET.pegarCaminhoAbsolutoTreinoPositivo())
        self.trasferirDados(self.DADOS_TREINO_NEGATIVO, self.NOVO_DATASET.pegarCaminhoAbsolutoTreinoNegativo())

    def dividirValidacaoPositivoENegativo(self, porcentagem):
        self.QUANTIDADE_VALIDACAO_POSITIVO, self.QUANTIDADE_VALIDACAO_NEGATIVO = self.divirdirQuantidadeDeDados(porcentagem, self.QUANTIDADE_VALIDACAO)
        i = 0
        while i <= (self.QUANTIDADE_VALIDACAO_POSITIVO - 1):
            self.DADOS_VALIDACAO_POSITIVO.append(self.DADOS_VALIDACAO[i])
            i+=1
        
        while i <= (self.QUANTIDADE_VALIDACAO_POSITIVO + self.QUANTIDADE_VALIDACAO_NEGATIVO - 1):
            self.DADOS_VALIDACAO_NEGATIVO.append(self.DADOS_VALIDACAO[i])
            i+=1

        self.trasferirDados(self.DADOS_VALIDACAO_POSITIVO, self.NOVO_DATASET.pegarCaminhoAbsolutoValidacaoPositivo())
        self.trasferirDados(self.DADOS_VALIDACAO_NEGATIVO, self.NOVO_DATASET.pegarCaminhoAbsolutoValidacaoNegativo())


    # origem, destino
    def trasferirDados(self, caminhoDeOrigem, caminhoDeDestino):
        for index, dado in enumerate(caminhoDeOrigem):
            imagem = Imagem(dado)
            imagem.salvarImagem(caminhoDeDestino, imagem.pegarNomeDaImagem())

    # Treino
    
    def pegarQuantidadeDadosTreino(self):
        return self.QUANTIDADE_TREINO

    def pegarDadosTreino(self):
        return self.DADOS_TREINO

    def pegarQuantidadeDadosTreinoPositivo(self):
        return self.QUANTIDADE_TREINO_POSITIVO
    
    def pegarDadosTreinoPositivo(self):
        return self.DADOS_TREINO_POSITIVO
    
    def pegarDadosTreinoNegativo(self):
        return self.DADOS_TREINO_NEGATIVO
    
    def pegarQuantidadeDadosTreinoNegativo(self):
        return self.QUANTIDADE_TREINO_NEGATIVO
    
    # Validacao

    def pegarQuantidadeDadosValidacao(self):
        return self.QUANTIDADE_VALIDACAO

    def pegarQuantidadeDadosValidacaoPositivo(self):
        return self.QUANTIDADE_VALIDACAO_POSITIVO
    
    def pegarQuantidadeDadosValidacaoNegativo(self):
        return self.QUANTIDADE_VALIDACAO_NEGATIVO
    
    def pegarDadosValidacaoPositivo(self):
        return self.DADOS_VALIDACAO_POSITIVO

    def pegarDadosValidacaoNegativo(self):
        return self.DADOS_VALIDACAO_NEGATIVO

    def pegarDadosValidacao(self):
        return self.DADOS_VALIDACAO

    

    def pegarNovoDataset(self):
        return self.NOVO_DATASET