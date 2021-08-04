with open('B0TMC2_scan.log') as f:
    lista = f.readlines()

    conta_linha = 0
    conta_input = 0
    nome_base = 'B0TMC2'
    numero_atomico = slice(12, 18)
    coord_x_y_z = slice(35, 70)

    for i_linha, j_linha, k_linha, m_linha in zip(lista, lista[1:], lista[2:], lista[3:]):
        conta_linha += 1
        if 'YES' in i_linha and 'YES' in j_linha and 'YES' in k_linha and 'YES' in m_linha:
            ini = conta_linha + 528
            fim = conta_linha + 570
            conta_input += 1
            nome = nome_base + '_' + 'SAPT' + '_' + str(conta_input) + '.dat'
            with open(nome, 'w') as file:
                for i in range(ini, fim):
                    x_y_z = lista[i][coord_x_y_z]
                    na = lista[i][numero_atomico]
                    print(f'{na} {x_y_z}', end='\n', file=file)
                    
