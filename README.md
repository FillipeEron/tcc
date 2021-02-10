# REPOSITÓRIO TCC

Repositório do TCC "Desenvolvimento de uma aplicação mobile fundamentado em aprendizado de máquina para auxílio ao diagnóstico da dengue baseado na prova do torniquete". Aqui estão todo os artefatos utilizados para a criação do prototipo de aplicação mobile. As devidas bibliografias e créditos oriundas de artigos, bibliotecas, api, dataset e ademais materiais estão registradas no TCC escrito (que será disponibilizado quando o trabalho for defendido e aceito pela banca).

## ESTRUTURA DO REPOSITÓRIO
```shell
|tcc
|--app
|--codigo
    |--cnn
    |--ENV
    |--pdi
|--dataset
    |--dataset
    |--17_11_2020-9:3:36
    |--17_11_2020-9:3:36(clahe)
    |--35
    |--simulacao-real
|--modelo
```
### app
Diretório contendo a aplicação mobile em android do projeto.

### codigo
Diretório contento scripts.

#### pdi
Diretório com os scripts de PDI e manipulação do dataset original.

#### ENV
Diretório referente ao python environment. 

#### cnn
Diretório usado para fazer prototipações da rede neural convolucional (não possui os scripts de treinamento e testes).

### dataset
Diretório contendo os datasets.

- 35: contém o dataset original.
- 17_11_2020-9:3:36: contém o dataset com petéquias.
- 17_11_2020-9:3:36(clahe): contém o dataset com petéquias com a equalização de histograma.
- simulacao-real: contém o dataset usado nos testes de desempenho da rede.

### modelo
Diretório contém o modelo e os gráficos de acuracia e perda.

## RNC
Os scripts referentes ao treinamento, teste e conversão do modelo treinado para versão mobile podem ser acessados no link a seguir, podendo ser baixados e importados para a plataforma [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb) e ser executado.

- [Scripts](https://drive.google.com/drive/folders/1Izs_JColma0nRr9GqW4rMzlw7JipUM0B?usp=sharing)