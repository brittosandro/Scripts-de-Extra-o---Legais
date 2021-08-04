import re


with open('teste1.txt') as f:
    lista_dados = f.readlines()

    teste1 = 'Maximum Force            0.000009     0.000450     YES'
    teste2 = 'RMS     Force            0.000002     0.000300     YES'
    teste3 = 'Maximum Displacement     0.000480     0.001800     YES'
    teste4 = 'RMS     Displacement     0.000106     0.001200     YES'

    yes = slice(51, 54)
    conta_yes = 0
    #for linha in str_dados:
        #print(linha, end='')
    #if linha[yes] == teste1 and linha[yes] == teste2 and linha[yes] == teste3 and linha[yes] == teste4:
    #lista_dados = str_dados.split(sep1)[1].split(sep2)[0]

    #lista_dados = str_dados.split('\n')
    grande_l = []
    for dados in lista_dados:
        if dados[yes] == teste1:
            conta_yes = 1
        if dados[yes] == teste2:
            conta_yes += 1
        if dados[yes] == teste3:
            conta_yes += 1
        if dados[yes] == teste4:
            conta_yes += 1
        if conta_yes == 4:
            grande_l.append(dados)
            #print(dados)
            #l1 = dados.split(sep1)
            #print(l1)

#print(grande_l)
#s = ' '.join(grande_l)
#print(s)
#l = s.split()
#l1 = ' '.join(l).split(sep2)
#print(l1)
#l = s.split(sep1)[1].split(sep2)[0]
#print(l)
#print(conta_yes)
expressao_regular = '|'.join(map(re.escape, delimitadores))
l = re.split(expressao_regular, s)
print(l)
