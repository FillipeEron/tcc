import pathlib

def pegarNomeDoArquivo(caminho):
    caminhoCompleto = pathlib.Path(caminho)
    nomeDoArquivo = caminhoCompleto.name
    return nomeDoArquivo

def alterarPrefixoArquivo(caminho, novoPrefixo):
    caminhoCompleto = pathlib.Path(caminho)
    nomeDoArquivo = caminhoCompleto.name
    nomeFragmentado = nomeDoArquivo.split('.')
    return nomeFragmentado[0] + "." + novoPrefixo
    
