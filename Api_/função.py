dic = {
        "linguagens": [
        {"nome": "javascript", "criacao": 1996, 
        "paradigma": ["eventos","funcional"]},
        {"nome": "python", "criacao": 1991, 
        "paradigma": ["orientada a objetos","estruturada"]},
        {"nome": "haskell", "criacao": 1990, 
        "paradigma": ["funcional"]}
        ]
    }

#10 Escreva uma função "mais velha" que 
# recebe um dicionário como dic e 
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista

def mais_velha(dic):
    lista_linguagens = dic['linguagens']
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        if linguagem['criacao'] < ling_velha['criacao']:
            ling_velha = linguagem
    return ling_velha





#11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação

def todos_paradigmas(dic):
    lista_linguagens = dic['linguagens']
    paradigmas = []
    for linguagem in lista_linguagens:
        paradigmas_da_linguagem = linguagem['paradigma']
        for p in paradigmas_da_linguagem:
            if p not in paradigmas:
                paradigmas.append(p)
    return paradigmas 