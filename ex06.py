#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.

dicionario = {'Ana':'estudante','Anderson':'professor', 'Cadeira':'Couro'}

def ordenar_chaves(dicionario):
    chaves_ordenadas = sorted(dicionario.keys())
    lista_ordenada = [(chave, dicionario[chave]) for chave in chaves_ordenadas]
    print(lista_ordenada)
        

ordenar_chaves(dicionario)