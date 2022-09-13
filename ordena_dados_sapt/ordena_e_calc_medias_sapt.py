###############################################################################
#
#   Esse script tanto ordena os valores de energia em ordem crescente quanto
# calcula os valores de energia média para cada interação.
#
############################################################################### 



import numpy as np
import os


def caminho(diretorio, arquivo):
    '''
    Essa função recebe o diretório e o arquivo com os dados de energia SAPT e
    retorna o caminho de onde os arquivos estão.
    '''
    return os.path.join(diretorio, arquivo)

def pega_metodo_base(nome_sitio):
    '''
    Essa função recebe o nome de um certo sítio de interação
    e retorna o método e a base que as interações foram calculadas,
    no formato: metodo/base.
    '''
    mb =  caminho(dir, arq).replace('./', '').split('/')[1].replace('_'
                                   + nome_sitio + '_', '/').replace('.dat', '')
    return mb

def distancia_energia_sapt(caminho):
    '''
    Essa função recebe um caminho de um arquivo com os dados de distancia
    e energia SAPT para diferentes bases e métodos e retorna uma tupla cujos
    elementos são arrays de distância e energia SAPT.
    '''
    dados =  np.loadtxt(caminho, comments='#')
    distancia = dados[:, 0]
    esapt = dados[:, 5]
    return distancia, esapt

def indice_para_menor_energia_sapt(esapt):
    '''
    Essa função recebe o array de energia SAPT e retorna o valor de índice
    associado a menor energia do array.
    '''
    return list(esapt).index(min(esapt))

def ordena_dicionario(d):
    '''
    Essa função recebe um dicionario cuja chave designa o método e a base do
    cálculo e o valor é uma tupla com a distancia de equilibrio e a energia
    sapt total. A função retorna um dicionario em ordem crescente de energia
    sapt. Por exemplo: {
    'sapt0/aug-cc-pvtz': (3.8, -14.387572),
    'sapt2+/aug-cc-pvtz': (3.8, -14.3323951),
    'sapt2+3/aug-cc-pvtz': (3.8, -14.0726924)
    }
    '''
    dic_ordenado = {}
    for item in sorted(d, key=d.get):
        dic_ordenado[item] = d[item]
    return dic_ordenado

def calc_medias(valores1, valores2, valores3):
    '''
    A função recebe três tipos de valores que correspondem as tuplas com
    distancia e energia em cada sitio: (distancia, energia). E retorna
    a medias das distâncias e das energias para os 3 sítios.
    '''
    med_dist = (sitio1_mol4_ord[i][0] + sitio2_mol4_ord[j][0] + sitio3_mol4_ord[k][0]) / 3
    med_ener = (sitio1_mol4_ord[i][1] + sitio2_mol4_ord[j][1] + sitio3_mol4_ord[k][1]) / 3

    return round(med_dist, 2), round(med_ener, 2)

molecula1 = 'Ar'
molecula2 = 'He'
molecula3 = 'Ne'
molecula4 = 'Kr'

sitio1 = 's1'
sitio2 = 's2'
sitio3 = 's3'

metodos = ['sapt0', 'sapt2', 'sapt2+', 'sapt2+(3)', 'sapt2+3']
bases = ['aug-cc-pvdz', 'aug-cc-pvtz', 'jun-cc-pvdz']

sitio1_mol1 = {}
sitio2_mol1 = {}
sitio3_mol1 = {}

sitio1_mol2 = {}
sitio2_mol2 = {}
sitio3_mol2 = {}

sitio1_mol3 = {}
sitio2_mol3 = {}
sitio3_mol3 = {}

sitio1_mol4 = {}
sitio2_mol4 = {}
sitio3_mol4 = {}

diretorio_corrente = '.'
for dir, subdirs, arqs in os.walk(diretorio_corrente):
    for arq in arqs:
        if sitio1 in caminho(dir, arq):
            if molecula1 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio1)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio1_mol1[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio1_mol1_ord = ordena_dicionario(sitio1_mol1)

            if molecula2 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio1)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio1_mol2[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio1_mol2_ord = ordena_dicionario(sitio1_mol2)

            if molecula3 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio1)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio1_mol3[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio1_mol3_ord = ordena_dicionario(sitio1_mol3)

            if molecula4 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio1)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio1_mol4[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio1_mol4_ord = ordena_dicionario(sitio1_mol4)

        if sitio2 in caminho(dir, arq):
            if molecula1 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio2)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio2_mol1[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio2_mol1_ord = ordena_dicionario(sitio2_mol1)

            if molecula2 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio2)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio2_mol2[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio2_mol2_ord = ordena_dicionario(sitio2_mol2)

            if molecula3 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio2)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio2_mol3[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio2_mol3_ord = ordena_dicionario(sitio2_mol3)

            if molecula4 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio2)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio2_mol4[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio2_mol4_ord = ordena_dicionario(sitio2_mol4)

        if sitio3 in caminho(dir, arq):
            if molecula1 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio3)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio3_mol1[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio3_mol1_ord = ordena_dicionario(sitio3_mol1)

            if molecula2 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio3)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio3_mol2[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio3_mol2_ord = ordena_dicionario(sitio3_mol2)

            if molecula3 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio3)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio3_mol3[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio3_mol3_ord = ordena_dicionario(sitio3_mol3)

            if molecula4 in caminho(dir, arq):
                metodo_base = pega_metodo_base(sitio3)
                dist, esapt = distancia_energia_sapt(caminho(dir, arq))
                ind_menor_en = indice_para_menor_energia_sapt(esapt)
                sitio3_mol4[metodo_base] = dist[ind_menor_en], min(esapt)
                sitio3_mol4_ord = ordena_dicionario(sitio3_mol4)

'''
print('#'*95)
print(f'Dicionários Referentes a molécula {molecula1} Organizados em ordem \
       crescente de energia.')
print('\n\n')

print(f'Sitio 1 {molecula1}')
print(sitio1_mol1_ord)
print()

print(f'Sitio 2 {molecula1}')
print(sitio2_mol1_ord)
print()

print(f'Sitio 3 {molecula1}')
print(sitio3_mol1_ord)
print('#'*95)
print('\n')
print(f'Valores Médios de Re e E para {molecula1} Organizados em ordem \
       crescente de energia.')
print('-'*95)

for i in sitio1_mol1_ord:
    for j in sitio2_mol1_ord:
        for k in sitio3_mol1_ord:
            if i == 'sapt0/aug-cc-pvdz' and j == 'sapt0/aug-cc-pvdz' and k == 'sapt0/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/aug-cc-pvtz' and j == 'sapt0/aug-cc-pvtz' and k == 'sapt0/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvtz' and j == 'sapt0/jun-cc-pvtz' and k == 'sapt0/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvdz' and j == 'sapt0/jun-cc-pvdz' and k == 'sapt0/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol1_ord:
    for j in sitio2_mol1_ord:
        for k in sitio3_mol1_ord:
            if i == 'sapt2/aug-cc-pvdz' and j == 'sapt2/aug-cc-pvdz' and k == 'sapt2/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/aug-cc-pvtz' and j == 'sapt2/aug-cc-pvtz' and k == 'sapt2/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvdz' and j == 'sapt2/jun-cc-pvdz' and k == 'sapt2/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvtz' and j == 'sapt2/jun-cc-pvtz' and k == 'sapt2/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol1_ord:
    for j in sitio2_mol1_ord:
        for k in sitio3_mol1_ord:
            if i == 'sapt2+/aug-cc-pvdz' and j == 'sapt2+/aug-cc-pvdz' and k == 'sapt2+/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/aug-cc-pvtz' and j == 'sapt2+/aug-cc-pvtz' and k == 'sapt2+/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvdz' and j == 'sapt2+/jun-cc-pvdz' and k == 'sapt2+/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvtz' and j == 'sapt2+/jun-cc-pvtz' and k == 'sapt2+/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol1_ord:
    for j in sitio2_mol1_ord:
        for k in sitio3_mol1_ord:
            if i == 'sapt2+(3)/aug-cc-pvdz' and j == 'sapt2+(3)/aug-cc-pvdz' and k == 'sapt2+(3)/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/aug-cc-pvtz' and j == 'sapt2+(3)/aug-cc-pvtz' and k == 'sapt2+(3)/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvdz' and j == 'sapt2+(3)/jun-cc-pvdz' and k == 'sapt2+(3)/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvtz' and j == 'sapt2+(3)/jun-cc-pvtz' and k == 'sapt2+(3)/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol1_ord:
    for j in sitio2_mol1_ord:
        for k in sitio3_mol1_ord:
            if i == 'sapt2+3/aug-cc-pvdz' and j == 'sapt2+3/aug-cc-pvdz' and k == 'sapt2+3/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/aug-cc-pvtz' and j == 'sapt2+3/aug-cc-pvtz' and k == 'sapt2+3/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvdz' and j == 'sapt2+3/jun-cc-pvdz' and k == 'sapt2+3/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvtz' and j == 'sapt2+3/jun-cc-pvtz' and k == 'sapt2+3/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)


print('#'*95)
print(f'Dicionários Referentes a molécula {molecula2} Organizados em ordem \
       crescente de energia.')
print('\n\n')

print(f'Sitio 1 {molecula2}')
print(sitio1_mol2_ord)
print()

print(f'Sitio 2 {molecula2}')
print(sitio2_mol2_ord)
print()

print(f'Sitio 3 {molecula2}')
print(sitio3_mol2_ord)
print('#'*95)
print('\n')
print(f'Valores Médios de Re e E para {molecula2} Organizados em ordem \
       crescente de energia.')
print('-'*95)

for i in sitio1_mol2_ord:
    for j in sitio2_mol2_ord:
        for k in sitio3_mol2_ord:
            if i == 'sapt0/aug-cc-pvdz' and j == 'sapt0/aug-cc-pvdz' and k == 'sapt0/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/aug-cc-pvtz' and j == 'sapt0/aug-cc-pvtz' and k == 'sapt0/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvtz' and j == 'sapt0/jun-cc-pvtz' and k == 'sapt0/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvdz' and j == 'sapt0/jun-cc-pvdz' and k == 'sapt0/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol2_ord:
    for j in sitio2_mol2_ord:
        for k in sitio3_mol2_ord:
            if i == 'sapt2/aug-cc-pvdz' and j == 'sapt2/aug-cc-pvdz' and k == 'sapt2/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/aug-cc-pvtz' and j == 'sapt2/aug-cc-pvtz' and k == 'sapt2/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvdz' and j == 'sapt2/jun-cc-pvdz' and k == 'sapt2/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvtz' and j == 'sapt2/jun-cc-pvtz' and k == 'sapt2/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol2_ord:
    for j in sitio2_mol2_ord:
        for k in sitio3_mol2_ord:
            if i == 'sapt2+/aug-cc-pvdz' and j == 'sapt2+/aug-cc-pvdz' and k == 'sapt2+/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/aug-cc-pvtz' and j == 'sapt2+/aug-cc-pvtz' and k == 'sapt2+/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvdz' and j == 'sapt2+/jun-cc-pvdz' and k == 'sapt2+/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvtz' and j == 'sapt2+/jun-cc-pvtz' and k == 'sapt2+/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol2_ord:
    for j in sitio2_mol2_ord:
        for k in sitio3_mol2_ord:
            if i == 'sapt2+(3)/aug-cc-pvdz' and j == 'sapt2+(3)/aug-cc-pvdz' and k == 'sapt2+(3)/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/aug-cc-pvtz' and j == 'sapt2+(3)/aug-cc-pvtz' and k == 'sapt2+(3)/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvdz' and j == 'sapt2+(3)/jun-cc-pvdz' and k == 'sapt2+(3)/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvtz' and j == 'sapt2+(3)/jun-cc-pvtz' and k == 'sapt2+(3)/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol2_ord:
    for j in sitio2_mol2_ord:
        for k in sitio3_mol2_ord:
            if i == 'sapt2+3/aug-cc-pvdz' and j == 'sapt2+3/aug-cc-pvdz' and k == 'sapt2+3/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/aug-cc-pvtz' and j == 'sapt2+3/aug-cc-pvtz' and k == 'sapt2+3/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvdz' and j == 'sapt2+3/jun-cc-pvdz' and k == 'sapt2+3/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvtz' and j == 'sapt2+3/jun-cc-pvtz' and k == 'sapt2+3/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

'''
print('#'*95)
print(f'Dicionários Referentes a molécula {molecula3} Organizados em ordem \
       crescente de energia.')
print('\n\n')
print(f'Sitio 1 {molecula3}')
print(sitio1_mol3_ord)
print()

print(f'Sitio 2 {molecula3}')
print(sitio2_mol3_ord)
print()

print(f'Sitio 3 {molecula3}')
print(sitio3_mol3_ord)
print('-'*95)
print(f'Valores Médios de Re e E para {molecula3} Organizados em ordem \
       crescente de energia.')
print('-'*95)

for i in sitio1_mol3_ord:
    for j in sitio2_mol3_ord:
        for k in sitio3_mol3_ord:
            if i == 'sapt0/aug-cc-pvdz' and j == 'sapt0/aug-cc-pvdz' and k == 'sapt0/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/aug-cc-pvtz' and j == 'sapt0/aug-cc-pvtz' and k == 'sapt0/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvtz' and j == 'sapt0/jun-cc-pvtz' and k == 'sapt0/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvdz' and j == 'sapt0/jun-cc-pvdz' and k == 'sapt0/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol3_ord:
    for j in sitio2_mol3_ord:
        for k in sitio3_mol3_ord:
            if i == 'sapt2/aug-cc-pvdz' and j == 'sapt2/aug-cc-pvdz' and k == 'sapt2/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/aug-cc-pvtz' and j == 'sapt2/aug-cc-pvtz' and k == 'sapt2/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvdz' and j == 'sapt2/jun-cc-pvdz' and k == 'sapt2/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvtz' and j == 'sapt2/jun-cc-pvtz' and k == 'sapt2/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol3_ord:
    for j in sitio2_mol3_ord:
        for k in sitio3_mol3_ord:
            if i == 'sapt2+/aug-cc-pvdz' and j == 'sapt2+/aug-cc-pvdz' and k == 'sapt2+/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/aug-cc-pvtz' and j == 'sapt2+/aug-cc-pvtz' and k == 'sapt2+/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvdz' and j == 'sapt2+/jun-cc-pvdz' and k == 'sapt2+/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvtz' and j == 'sapt2+/jun-cc-pvtz' and k == 'sapt2+/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol3_ord:
    for j in sitio2_mol3_ord:
        for k in sitio3_mol3_ord:
            if i == 'sapt2+(3)/aug-cc-pvdz' and j == 'sapt2+(3)/aug-cc-pvdz' and k == 'sapt2+(3)/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/aug-cc-pvtz' and j == 'sapt2+(3)/aug-cc-pvtz' and k == 'sapt2+(3)/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvdz' and j == 'sapt2+(3)/jun-cc-pvdz' and k == 'sapt2+(3)/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvtz' and j == 'sapt2+(3)/jun-cc-pvtz' and k == 'sapt2+(3)/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol3_ord:
    for j in sitio2_mol3_ord:
        for k in sitio3_mol3_ord:
            if i == 'sapt2+3/aug-cc-pvdz' and j == 'sapt2+3/aug-cc-pvdz' and k == 'sapt2+3/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/aug-cc-pvtz' and j == 'sapt2+3/aug-cc-pvtz' and k == 'sapt2+3/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvdz' and j == 'sapt2+3/jun-cc-pvdz' and k == 'sapt2+3/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvtz' and j == 'sapt2+3/jun-cc-pvtz' and k == 'sapt2+3/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

'''
print('#'*95)
print(f'Dicionários Referentes a molécula {molecula4} Organizados em ordem \
       crescente de energia.')
print('\n\n')

print(f'Sitio 1 {molecula4}')
print(sitio1_mol4_ord)
print()

print(f'Sitio 2 {molecula4}')
print(sitio2_mol4_ord)
print()

print(f'Sitio 3 {molecula4}')
print(sitio3_mol4_ord)
print('#'*95)
print('\n')
print(f'Valores Médios de Re e E para {molecula4} Organizados em ordem \
       crescente de energia.')
print('-'*95)

for i in sitio1_mol4_ord:
    for j in sitio2_mol4_ord:
        for k in sitio3_mol4_ord:
            if i == 'sapt0/aug-cc-pvdz' and j == 'sapt0/aug-cc-pvdz' and k == 'sapt0/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/aug-cc-pvtz' and j == 'sapt0/aug-cc-pvtz' and k == 'sapt0/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvtz' and j == 'sapt0/jun-cc-pvtz' and k == 'sapt0/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt0/jun-cc-pvdz' and j == 'sapt0/jun-cc-pvdz' and k == 'sapt0/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol4_ord:
    for j in sitio2_mol4_ord:
        for k in sitio3_mol4_ord:
            if i == 'sapt2/aug-cc-pvdz' and j == 'sapt2/aug-cc-pvdz' and k == 'sapt2/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/aug-cc-pvtz' and j == 'sapt2/aug-cc-pvtz' and k == 'sapt2/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvdz' and j == 'sapt2/jun-cc-pvdz' and k == 'sapt2/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2/jun-cc-pvtz' and j == 'sapt2/jun-cc-pvtz' and k == 'sapt2/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)


for i in sitio1_mol4_ord:
    for j in sitio2_mol4_ord:
        for k in sitio3_mol4_ord:
            if i == 'sapt2+/aug-cc-pvdz' and j == 'sapt2+/aug-cc-pvdz' and k == 'sapt2+/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/aug-cc-pvtz' and j == 'sapt2+/aug-cc-pvtz' and k == 'sapt2+/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvdz' and j == 'sapt2+/jun-cc-pvdz' and k == 'sapt2+/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+/jun-cc-pvtz' and j == 'sapt2+/jun-cc-pvtz' and k == 'sapt2+/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol4_ord:
    for j in sitio2_mol4_ord:
        for k in sitio3_mol4_ord:
            if i == 'sapt2+(3)/aug-cc-pvdz' and j == 'sapt2+(3)/aug-cc-pvdz' and k == 'sapt2+(3)/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/aug-cc-pvtz' and j == 'sapt2+(3)/aug-cc-pvtz' and k == 'sapt2+(3)/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvdz' and j == 'sapt2+(3)/jun-cc-pvdz' and k == 'sapt2+(3)/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+(3)/jun-cc-pvtz' and j == 'sapt2+(3)/jun-cc-pvtz' and k == 'sapt2+(3)/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)

for i in sitio1_mol4_ord:
    for j in sitio2_mol4_ord:
        for k in sitio3_mol4_ord:
            if i == 'sapt2+3/aug-cc-pvdz' and j == 'sapt2+3/aug-cc-pvdz' and k == 'sapt2+3/aug-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/aug-cc-pvtz' and j == 'sapt2+3/aug-cc-pvtz' and k == 'sapt2+3/aug-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvdz' and j == 'sapt2+3/jun-cc-pvdz' and k == 'sapt2+3/jun-cc-pvdz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
            elif i == 'sapt2+3/jun-cc-pvtz' and j == 'sapt2+3/jun-cc-pvtz' and k == 'sapt2+3/jun-cc-pvtz':
                print(i)
                d = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[0]
                e = calc_medias(sitio1_mol4_ord[i], sitio2_mol4_ord[j], sitio3_mol4_ord[k])[1]
                print(f' Re\t  Ee')
                print(f' {d}\t{e}')
                print('-'*55)
'''
