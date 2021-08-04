with open('texto1.txt') as f:
    lista = f.read().split('\n')

    conta_linha = 0
    #conta_yes1 = 0
    #conta_yes2 = 0
    #condicao = slice(0, 6)
    #yes = slice(3, 6)

    for i_linha, j_linha, k_linha, m_linha in zip(lista, lista[1:], lista[2:], lista[3:]):
        conta_linha += 1
        #print(f'conta linha = {conta_linha}')
        #conta_linha += 1
        if 'Yes' in i_linha and 'Yes' in j_linha and 'Yes' in k_linha and 'Yes' in m_linha:
            print(f'Condição 1 = {i_linha} | Condição 2 = {j_linha} na linha {conta_linha}')
            print(conta_linha)
            ini = conta_linha + 6
            fim = conta_linha + 11
            for i in range(ini, fim):
                print(lista[i])

        #if linha[condicao] == 'c1 Yes':
        #    conta_yes1 = 1
        #    print(f'conta_Yes1 = {conta_yes1} na linha {conta_linha}')
        #if linha[condicao] == 'c2 Yes':
        #    conta_yes2 = 1
        #    print(f'conta_Yes2 = {conta_yes2} na linha {conta_linha}')
        #if linha[condicao] != 'c1 Yes':
        #    conta_yes1 = False
        #if linha[condicao] != 'c2 Yes':
        #    conta_yes2 = False

        #print(f'conta_Yes1 = {conta_yes1} | conta_Yes2 = {conta_yes2}')

        #if conta_yes1 + conta_yes2 == 2:
        #    print(linha)
            #lista.append(linha)


        #print(f'conta_Yes1 = {conta_yes1} na linha {conta_linha}')
        #print(f'conta_Yes2 = {conta_yes2} na linha {conta_linha}')

        #print()
