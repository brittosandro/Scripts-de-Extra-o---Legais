import re


with open('teste1.txt') as f:
    lista = f.readlines()

    #lista = f.read().split('\n')

    conta_linha = 0

    for i_linha, j_linha, k_linha, m_linha in zip(lista, lista[1:], lista[2:], lista[3:]):
        conta_linha += 1
        if 'Yes' in i_linha and 'Yes' in j_linha and 'Yes' in k_linha and 'Yes' in m_linha:
            print(conta_linha)
            ini = conta_linha + 7
            fim = conta_linha + 12
            for i in range(ini, fim):
                print(lista[i], end='')

        #print()
'''
    teste1 = 'Condicional1'
    teste2 = 'Condicional2'
    teste3 = 'Condicional3'
    teste4 = 'Condicional4'

    sep1 = '         Peguie isso daqui'
    sep2 = '---------------------------------------------------------------------'
    sep3 = 'Condicional4                Yes'

    delimitadores = sep1, sep2

    yes = slice(28, 31)
    condition = slice(0, 12)
    conta_yes = 0
    conta_linha = 0
    for linha in str_dados:
        print(linha, end='')
    if linha[yes] == teste1 and linha[yes] == teste2 and linha[yes] == teste3 and linha[yes] == teste4:
    lista_dados = str_dados.split(sep1)[1].split(sep2)[0]
    lista_dados = str_dados.split('\n')
    grande_l = []
    for n, dados in enumerate(lista_dados):
        print(conta_linha)
        print(dados[condition])
        print(dados[yes])
        if dados[condition] == teste1 and dados[yes] == 'Yes':
            conta_yes = 1
        if dados[condition] == teste2 and dados[yes] == 'Yes' :
            conta_yes += 1
        if dados[condition] == teste3 and dados[yes] == 'Yes':
            conta_yes += 1
        if dados[condition] == teste4 and dados[yes] == 'Yes':
            conta_yes += 1
        if conta_yes == 4:
            grande_l.append(dados)
            print(dados)
            l1 = dados.split(sep1)
            print(l1)
        conta_linha += 1
        print(conta_yes)


print(grande_l)
s = ' '.join(grande_l)
print(s)
l = s.split()
l1 = ' '.join(l).split(sep2)
print(l1)
l = s.split(sep1)[1].split(sep2)[0]
print(l)
print(conta_yes)
expressao_regular = '|'.join(map(re.escape, delimitadores))
l = re.split(expressao_regular, s)
print(l)
'''
