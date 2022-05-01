import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns


def dados_templetes(arquivo):
    separador1 = '*' * 142
    separador2 = '\n\n   '

    with open(arquivo) as f:
        lista_dados = f.read().split(separador2)

    lista_dados_tratada1 = (''.join(lista_dados).split(separador1)[1:-1])
    #print(lista_dados_tratada1)

    string_lista_dados_tratada1 = ''.join(lista_dados_tratada1)
    #print(string_lista_dados_tratada1)

    lista_dados_tratada2 = string_lista_dados_tratada1.split('\n')[1:]
    #print(lista_dados_tratada2)

    string_lista_dados_tratada2 = ''.join(lista_dados_tratada2)
    #print(string_lista_dados_tratada2)

    lista_dados_tratada3 = string_lista_dados_tratada2.split('o  ')[1:]
    #print(lista_dados_tratada3)

    n_ele = 6
    lista_dividida = [lista_dados_tratada3[i:i + n_ele]
                      for i in range(0, len(lista_dados_tratada3), n_ele)]
    #print(lista_dividida)

    #for lista in lista_dividida:
    #    print(lista)
    #print(np.asarray(lista_dividida))
    return np.asarray(lista_dividida)


def dados_monomeros(arquivo):
    separador1 = '*' * 142
    separador2 = '\n\n   '

    with open(arquivo) as f:
        lista_dados = f.read().split(separador2)

    lista_dados_tratada1 = (''.join(lista_dados).split(separador1)[1:-1])
    #print(lista_dados_tratada1)

    string_lista_dados_tratada1 = ''.join(lista_dados_tratada1)
    #print(string_lista_dados_tratada1)

    lista_dados_tratada2 = string_lista_dados_tratada1.split('\n')[1:]
    #print(lista_dados_tratada2)

    string_lista_dados_tratada2 = ''.join(lista_dados_tratada2)
    #print(string_lista_dados_tratada2)

    lista_dados_tratada3 = string_lista_dados_tratada2.split('o  ')[1:]
    #print(lista_dados_tratada3)

    n_ele = 6
    lista_dividida = [lista_dados_tratada3[i:i + n_ele]
                      for i in range(0, len(lista_dados_tratada3), n_ele)]
    #print(lista_dividida)

    #for lista in lista_dividida:
    #    print(lista)

    return np.asarray(lista_dividida)


def dados_complexos(arquivo):
    separador1 = '*' * 142
    separador2 = '\n\n   '

    with open(arquivo) as f:
        lista_dados = f.read().split(separador2)

    lista_dados_tratada1 = (''.join(lista_dados).split(separador1)[1:-1])
    #print(lista_dados_tratada1)

    string_lista_dados_tratada1 = ''.join(lista_dados_tratada1)
    #print(string_lista_dados_tratada1)

    lista_dados_tratada2 = string_lista_dados_tratada1.split('\n')[1:]
    #print(lista_dados_tratada2)

    string_lista_dados_tratada2 = ''.join(lista_dados_tratada2)
    #print(string_lista_dados_tratada2)

    lista_dados_tratada3 = string_lista_dados_tratada2.split('o  ')[1:]
    #print(lista_dados_tratada3)

    n_ele = 6
    lista_dividida = [lista_dados_tratada3[i:i + n_ele]
                      for i in range(0, len(lista_dados_tratada3), n_ele)]
    #print(lista_dividida)

    #for lista in lista_dividida:
    #    print(lista)

    return np.asarray(lista_dividida)

def prop_fisicas(prop1, prop2, prop3):
    '''
    Essa função recebe três propriedades, que podem ser, por exemplo: entalpia
    do Templete, entalpia do Monomero e entalpia do complexo, retornando a
    variacao da entalpia (Delta H) em kcal/mol. Caso receba a energia de Gibbs,
    tera: energias de Gibbs do Templete, energia de Gibbs do monomero e energia
    de Gibbs do complexo, retornando a variacao da energia de Gibbs (Delta G)
    em kcal/mol.

    - prop1 = propriedade do monomero.
    - prop2 = propriedade do templete.
    - prop3 = propriedade do complexo.
    '''
    return (float(prop3) - (float(prop1) + float(prop2))) * 627.5

def prop_fisicas2mono(prop1, prop2, prop3):
    '''
    Essa função recebe três propriedades, que podem ser, por exemplo: entalpia
    do Templete, entalpia do Monomero e entalpia do complexo, retornando a
    variacao da entalpia (Delta H) em kcal/mol. Caso receba a energia de Gibbs,
    tera: energias de Gibbs do Templete, energia de Gibbs do monomero e energia
    de Gibbs do complexo, retornando a variacao da energia de Gibbs (Delta G)
    em kcal/mol. Mas calcula a propriedade considerando 2 monomeros.

    - prop1 = propriedade do monomero.
    - prop2 = propriedade do templete.
    - prop3 = propriedade do complexo.
    '''
    return (float(prop3) - (2*float(prop1) + float(prop2))) * 627.51

def prop_fisicas3mono(prop1, prop2, prop3):
    '''
    Essa função recebe três propriedades, que podem ser, por exemplo: entalpia
    do Templete, entalpia do Monomero e entalpia do complexo, retornando a
    variacao da entalpia (Delta H) em kcal/mol. Caso receba a energia de Gibbs,
    tera: energias de Gibbs do Templete, energia de Gibbs do monomero e energia
    de Gibbs do complexo, retornando a variacao da energia de Gibbs (Delta G)
    em kcal/mol. Mas calcula a propriedade considerando 3 monomeros.

    - prop1 = propriedade do monomero.
    - prop2 = propriedade do templete.
    - prop3 = propriedade do complexo.
    '''
    return (float(prop3) - (3*float(prop1) + float(prop2))) * 627.51

def graficando_propriedades(int_temp, prop1, prop1_qH, prop2, prop2_qH, prop3,
                            prop3_qH, monomero, solvente, templete, propriedade_geral):

    sns.set(style="ticks")
    fig, ax = plt.subplots(figsize=(8.5, 6))

    # Ajusta subplots.
    fig.subplots_adjust(
                          left = 0.100,
                          right = 0.785,  # Define as distâncias entre os extremos
                          bottom = 0.14,
                          top = 0.890,
                          hspace = 0.24,  # Organiza espaçoes entre os subplots
                          wspace = 0.23   # Organiza espaçoes entre os subplots
                       )

    fig1 = ax.plot(interval_temp, prop1, color='#4B0082', linewidth=2.8, label='1'+monomero)
    fig2 = ax.plot(interval_temp, prop1_qH, color='#6A5ACD', linewidth=2.8, label='1'+monomero+'(qH)')
    fig3 = ax.plot(interval_temp, prop2, color='#008080', linewidth=2.8, label='2'+monomero)
    fig4 = ax.plot(interval_temp, prop2_qH, color='#20B2AA', linewidth=2.8, label='2'+monomero+'(qH)')
    fig5 = ax.plot(interval_temp, prop3, color='#696969', linewidth=2.8, label='3'+monomero)
    fig6 = ax.plot(interval_temp, prop3_qH, color='#C0C0C0', linewidth=2.8, label='3'+monomero+'(qH)')
    fig.legend(loc='upper right', shadow=False, fontsize='large', bbox_to_anchor=(1.01, 0.90),
               frameon=False, title = "Monômeros", prop = {'size':15})
    plt.grid(False)

    fig.text(0.45,                     # Ordena Posição x
             0.92,                    # Ordena Posição y
             f'{templete} + {monomero} ({solvente})',
             ha='center',            # Alinha texto horizontalmente
             va='center',            # Alinha texto verticalmente
             fontsize = 'xx-large')


    fig.text(0.45,                      # Ordena Posição x
             0.05,                     # Ordena Posição y
             'Temperatura (K)',     # Texto A ser colocado
             ha='center',             # Alinha texto horizontalmente
             va='center',             # Alinha texto verticalmente
             fontsize = 'xx-large')

    if propriedade_geral == 'entalpia':
        fig.text(0.029,
                 0.5,
                 '$\Delta H$ ($kcal/mol$)',
                 ha='center',
                 va='center',
                 fontsize = 'xx-large',
                 rotation='vertical')      # Rotaciona o nome do eixo
    else:
        fig.text(0.029,
                 0.5,
                 '$\Delta G$ ($kcal/mol$)',
                 ha='center',
                 va='center',
                 fontsize = 'xx-large',
                 rotation='vertical')      # Rotaciona o nome do eixo

    plt.savefig(f'{templete}_{monomero}_{solvente}_{propriedade_geral}.png',
                dpi=300, orientation='portrait', transparent=True, format='png')
    plt.savefig(f'{templete}_{monomero}_{solvente}_{propriedade_geral}.pdf',
                dpi=300, orientation='portrait', transparent=True, format='pdf')
    plt.show()


if __name__ == '__main__':
    nome_template = slice(2, 10)
    nome_monomero = slice(2, 10)
    nome_complexo = slice(0, 23)
    temperatura = slice(47, 53)
    entalpia = slice(66, 79)
    entalpia_qH = slice(80, 92)
    interval_temp = np.arange(250, 501, 50)

    templete1 = 'CBZ'
    templete2 = 'DCF'
    templete3 = 'TMP'

    monomero1 = 'ACR'
    monomero2 = 'IA'
    monomero3 = 'MAA'
    monomero4 = 'VP'

    solvente1 = 'Acetonitrila'
    solvente2 = 'Diclorometano'
    solvente3 = 'Dimetilsulfóxido'
    solvente4 = 'Tetraidrofurano'

    propriedade_geral1 = 'entalpia'
    propriedade_geral2 = 'energia_gibbs'


    dados_templetes = dados_templetes('dados_templetes.dat')
    #print(dados_templetes)
    dados_monomeros = dados_monomeros('dados_monomeros.dat')
    #print(dados_monomeros)
    dados_complexos = dados_complexos('dados_complexos.dat')
    #print(dados_templestes_monos)

    # Templete = CBZ | Monomero = ACR
    entalp_CBZ_acet_1ACR = []
    entalp_qH_CBZ_acet_1ACR = []
    entalp_CBZ_acet_2ACR = []
    entalp_qH_CBZ_acet_2ACR = []
    entalp_CBZ_acet_3ACR = []
    entalp_qH_CBZ_acet_3ACR = []

    entalp_CBZ_diclo_1ACR = []
    entalp_qH_CBZ_diclo_1ACR = []
    entalp_CBZ_diclo_2ACR = []
    entalp_qH_CBZ_diclo_2ACR = []
    entalp_CBZ_diclo_3ACR = []
    entalp_qH_CBZ_diclo_3ACR = []

    entalp_CBZ_dime_1ACR = []
    entalp_qH_CBZ_dime_1ACR = []
    entalp_CBZ_dime_2ACR = []
    entalp_qH_CBZ_dime_2ACR = []
    entalp_CBZ_dime_3ACR = []
    entalp_qH_CBZ_dime_3ACR = []

    entalp_CBZ_tetr_1ACR = []
    entalp_qH_CBZ_tetr_1ACR = []
    entalp_CBZ_tetr_2ACR = []
    entalp_qH_CBZ_tetr_2ACR = []
    entalp_CBZ_tetr_3ACR = []
    entalp_qH_CBZ_tetr_3ACR = []

    # Templete = CBZ | Monomero = IA
    entalp_CBZ_acet_1IA = []
    entalp_qH_CBZ_acet_1IA = []
    entalp_CBZ_acet_2IA = []
    entalp_qH_CBZ_acet_2IA = []
    entalp_CBZ_acet_3IA = []
    entalp_qH_CBZ_acet_3IA = []

    entalp_CBZ_diclo_1IA = []
    entalp_qH_CBZ_diclo_1IA = []
    entalp_CBZ_diclo_2IA = []
    entalp_qH_CBZ_diclo_2IA = []
    entalp_CBZ_diclo_3IA = []
    entalp_qH_CBZ_diclo_3IA = []

    entalp_CBZ_dime_1IA = []
    entalp_qH_CBZ_dime_1IA = []
    entalp_CBZ_dime_2IA = []
    entalp_qH_CBZ_dime_2IA = []
    entalp_CBZ_dime_3IA = []
    entalp_qH_CBZ_dime_3IA = []

    entalp_CBZ_tetr_1IA = []
    entalp_qH_CBZ_tetr_1IA = []
    entalp_CBZ_tetr_2IA = []
    entalp_qH_CBZ_tetr_2IA = []
    entalp_CBZ_tetr_3IA = []
    entalp_qH_CBZ_tetr_3IA = []



    # Templete = CBZ | Monomero = MAA
    entalp_CBZ_acet_1MAA = []
    entalp_qH_CBZ_acet_1MAA = []
    entalp_CBZ_acet_2MAA = []
    entalp_qH_CBZ_acet_2MAA = []
    entalp_CBZ_acet_3MAA = []
    entalp_qH_CBZ_acet_3MAA = []

    entalp_CBZ_diclo_1MAA = []
    entalp_qH_CBZ_diclo_1MAA = []
    entalp_CBZ_diclo_2MAA = []
    entalp_qH_CBZ_diclo_2MAA = []
    entalp_CBZ_diclo_3MAA = []
    entalp_qH_CBZ_diclo_3MAA = []

    entalp_CBZ_dime_1MAA = []
    entalp_qH_CBZ_dime_1MAA = []
    entalp_CBZ_dime_2MAA = []
    entalp_qH_CBZ_dime_2MAA = []
    entalp_CBZ_dime_3MAA = []
    entalp_qH_CBZ_dime_3MAA = []

    entalp_CBZ_tetr_1MAA = []
    entalp_qH_CBZ_tetr_1MAA = []
    entalp_CBZ_tetr_2MAA = []
    entalp_qH_CBZ_tetr_2MAA = []
    entalp_CBZ_tetr_3MAA = []
    entalp_qH_CBZ_tetr_3MAA = []


    # Templete = CBZ | Monomero = VP
    entalp_CBZ_acet_1VP = []
    entalp_qH_CBZ_acet_1VP = []
    entalp_CBZ_acet_2VP = []
    entalp_qH_CBZ_acet_2VP = []
    entalp_CBZ_acet_3VP = []
    entalp_qH_CBZ_acet_3VP = []

    entalp_CBZ_diclo_1VP = []
    entalp_qH_CBZ_diclo_1VP = []
    entalp_CBZ_diclo_2VP = []
    entalp_qH_CBZ_diclo_2VP = []
    entalp_CBZ_diclo_3VP = []
    entalp_qH_CBZ_diclo_3VP = []

    entalp_CBZ_dime_1VP = []
    entalp_qH_CBZ_dime_1VP = []
    entalp_CBZ_dime_2VP = []
    entalp_qH_CBZ_dime_2VP = []
    entalp_CBZ_dime_3VP = []
    entalp_qH_CBZ_dime_3VP = []

    entalp_CBZ_tetr_1VP = []
    entalp_qH_CBZ_tetr_1VP = []
    entalp_CBZ_tetr_2VP = []
    entalp_qH_CBZ_tetr_2VP = []
    entalp_CBZ_tetr_3VP = []
    entalp_qH_CBZ_tetr_3VP = []


    for templetes in dados_templetes:
        for monomeros in dados_monomeros:
            for complexos in dados_complexos:
                for templete, monomero, complexo in zip(templetes, monomeros, complexos):
                    #print(f'{templete[nome_template]}  |  {monomero[nome_monomero]}  |  {complexo[nome_complexo]}')

                    '''
                    # Bloco1: Templete = CBZ, Monomero = ACR, Solvente = Acetonitrila
                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'ACR_acet' and complexo[nome_complexo] == 'CBZ_one_ACR_acetonitril':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_1ACR.append(v_entalpia)
                        entalp_qH_CBZ_acet_1ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'ACR_acet' and complexo[nome_complexo] == 'CBZ_two_ACR_acetonitril':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_2ACR.append(v_entalpia)
                        entalp_qH_CBZ_acet_2ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'ACR_acet' and complexo[nome_complexo] == 'CBZ_three_ACR_acetonitr':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_3ACR.append(v_entalpia)
                        entalp_qH_CBZ_acet_3ACR.append(v_entalpia_qH)
                    # fim Bloco1

                    # Bloco2: Templete = CBZ, Monomero = IA, Solvente = Acetonitrila
                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'IA_aceto' and complexo[nome_complexo] == 'CBZ_one_IA_acetonitrile':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_1IA.append(v_entalpia)
                        entalp_qH_CBZ_acet_1IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'IA_aceto' and complexo[nome_complexo] == 'CBZ_two_IA_acetonitrile':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_2IA.append(v_entalpia)
                        entalp_qH_CBZ_acet_2IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'IA_aceto' and complexo[nome_complexo] == 'CBZ_three_IA_acetonitri':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_3IA.append(v_entalpia)
                        entalp_qH_CBZ_acet_3IA.append(v_entalpia_qH)
                    # fim Bloco2

                    # Bloco3: Templete = CBZ, Monomero = MAA, Solvente = Acetonitrila
                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'MAA_acet' and complexo[nome_complexo] == 'CBZ_one_MAA_acetonitril':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_1MAA.append(v_entalpia)
                        entalp_qH_CBZ_acet_1MAA.append(v_entalpia_qH)


                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'MAA_acet' and complexo[nome_complexo] == 'CBZ_two_MAA_acetonitril':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_2MAA.append(v_entalpia)
                        entalp_qH_CBZ_acet_2MAA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'MAA_acet' and complexo[nome_complexo] == 'CBZ_three_MAA_acetonitr':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_3MAA.append(v_entalpia)
                        entalp_qH_CBZ_acet_3MAA.append(v_entalpia_qH)
                    # fim Bloco3

                    # Bloco4: Templete = CBZ, Monomero = VP, Solvente = Acetonitrila
                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'VP_aceto' and complexo[nome_complexo] == 'CBZ_one_VP_acetonitrile':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_1VP.append(v_entalpia)
                        entalp_qH_CBZ_acet_1VP.append(v_entalpia_qH)


                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'VP_aceto' and complexo[nome_complexo] == 'CBZ_two_VP_acetonitrile':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_2VP.append(v_entalpia)
                        entalp_qH_CBZ_acet_2VP.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'VP_aceto' and complexo[nome_complexo] == 'CBZ_three_VP_acetonitri':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_acet_3VP.append(v_entalpia)
                        entalp_qH_CBZ_acet_3VP.append(v_entalpia_qH)
                    # fim Bloco4


                    # Bloco1: Templete = CBZ, Monomero = ACR, Solvente = Diclorometano
                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'ACR_dich' and complexo[nome_complexo] == 'CBZ_one_ACR_dichloromet':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_1ACR.append(v_entalpia)
                        entalp_qH_CBZ_diclo_1ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'ACR_dich' and complexo[nome_complexo] == 'CBZ_two_ACR_dichloromet':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_2ACR.append(v_entalpia)
                        entalp_qH_CBZ_diclo_2ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'ACR_dich' and complexo[nome_complexo] == 'CBZ_three_ACR_dichlorom':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_3ACR.append(v_entalpia)
                        entalp_qH_CBZ_diclo_3ACR.append(v_entalpia_qH)
                    # fim Bloco1

                    # Bloco2: Templete = CBZ, Monomero = IA, Solvente = Diclorometano
                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'IA_dichl' and complexo[nome_complexo] == 'CBZ_one_IA_dichlorometh':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_1IA.append(v_entalpia)
                        entalp_qH_CBZ_diclo_1IA.append(v_entalpia_qH)


                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'IA_dichl' and complexo[nome_complexo] == 'CBZ_two_IA_dichlorometh':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_2IA.append(v_entalpia)
                        entalp_qH_CBZ_diclo_2IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'IA_dichl' and complexo[nome_complexo] == 'CBZ_three_IA_dichlorome':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_3IA.append(v_entalpia)
                        entalp_qH_CBZ_diclo_3IA.append(v_entalpia_qH)
                    # fim Bloco2

                    # Bloco3: Templete = CBZ, Monomero = MAA, Solvente = Diclorometano
                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'MAA_dich' and complexo[nome_complexo] == 'CBZ_one_MAA_dichloromet':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_1MAA.append(v_entalpia)
                        entalp_qH_CBZ_diclo_1MAA.append(v_entalpia_qH)


                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'MAA_dich' and complexo[nome_complexo] == 'CBZ_two_MAA_dichloromet':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_2MAA.append(v_entalpia)
                        entalp_qH_CBZ_diclo_2MAA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'MAA_dich' and complexo[nome_complexo] == 'CBZ_three_MAA_dichlorom':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_3MAA.append(v_entalpia)
                        entalp_qH_CBZ_diclo_3MAA.append(v_entalpia_qH)
                    # fim Bloco3

                    # Bloco4: Templete = CBZ, Monomero = VP, Solvente = Diclorometano
                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'VP_dichl' and complexo[nome_complexo] == 'CBZ_one_VP_dichlorometh':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_1VP.append(v_entalpia)
                        entalp_qH_CBZ_diclo_1VP.append(v_entalpia_qH)


                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'VP_dichl' and complexo[nome_complexo] == 'CBZ_two_VP_dichlorometh':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_2VP.append(v_entalpia)
                        entalp_qH_CBZ_diclo_2VP.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'VP_dichl' and complexo[nome_complexo] == 'CBZ_three_VP_dichlorome':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_diclo_3VP.append(v_entalpia)
                        entalp_qH_CBZ_diclo_3VP.append(v_entalpia_qH)
                    # fim Bloco4

                    # Bloco1: Templete = CBZ, Monomero = ACR, Solvente = Dimetilsufoxido
                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'ACR_dime' and complexo[nome_complexo] == 'CBZ_one_ACR_dimethylsul':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_1ACR.append(v_entalpia)
                        entalp_qH_CBZ_dime_1ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'ACR_dime' and complexo[nome_complexo] == 'CBZ_two_ACR_dimethylsul':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_2ACR.append(v_entalpia)
                        entalp_qH_CBZ_dime_2ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'ACR_dime' and complexo[nome_complexo] == 'CBZ_three_ACR_dimethyls':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_3ACR.append(v_entalpia)
                        entalp_qH_CBZ_dime_3ACR.append(v_entalpia_qH)
                    # fim Bloco1

                    # Bloco2: Templete = CBZ, Monomero = IA, Solvente = Dimetilsufoxido
                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'IA_dimet' and complexo[nome_complexo] == 'CBZ_one_IA_dimethylsulf':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_1IA.append(v_entalpia)
                        entalp_qH_CBZ_dime_1IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'IA_dimet' and complexo[nome_complexo] == 'CBZ_two_IA_dimethylsulf':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_2IA.append(v_entalpia)
                        entalp_qH_CBZ_dime_2IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'IA_dimet' and complexo[nome_complexo] == 'CBZ_three_IA_dimethylsu':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_3IA.append(v_entalpia)
                        entalp_qH_CBZ_dime_3IA.append(v_entalpia_qH)
                    # fim Bloco2

                    # Bloco3: Templete = CBZ, Monomero = MAA, Solvente = Dimetilsufoxido
                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'MAA_dime' and complexo[nome_complexo] == 'CBZ_one_MAA_dimethylsul':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_1MAA.append(v_entalpia)
                        entalp_qH_CBZ_dime_1MAA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'MAA_dime' and complexo[nome_complexo] == 'CBZ_two_MAA_dimethylsul':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_2MAA.append(v_entalpia)
                        entalp_qH_CBZ_dime_2MAA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'MAA_dime' and complexo[nome_complexo] == 'CBZ_three_MAA_dimethyls':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_3MAA.append(v_entalpia)
                        entalp_qH_CBZ_dime_3MAA.append(v_entalpia_qH)
                    # fim Bloco3

                    # Bloco4: Templete = CBZ, Monomero = VP, Solvente = Dimetilsufoxido
                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'VP_dimet' and complexo[nome_complexo] == 'CBZ_one_VP_dimethylsulf':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_1VP.append(v_entalpia)
                        entalp_qH_CBZ_dime_1VP.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'VP_dimet' and complexo[nome_complexo] == 'CBZ_two_VP_dimethylsulf':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_2VP.append(v_entalpia)
                        entalp_qH_CBZ_dime_2VP.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'VP_dimet' and complexo[nome_complexo] == 'CBZ_three_VP_dimethylsu':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_dime_3VP.append(v_entalpia)
                        entalp_qH_CBZ_dime_3VP.append(v_entalpia_qH)
                    # fim Bloco4
                    '''
                    # Bloco1: Templete = CBZ, Monomero = ACR, Solvente = Tetraidrofurano
                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'ACR_tetr' and complexo[nome_complexo] == 'CBZ_one_ACR_tetrahydrof':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_1ACR.append(v_entalpia)
                        entalp_qH_CBZ_tetr_1ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'ACR_tetr' and complexo[nome_complexo] == 'CBZ_two_ACR_tetrahydrof':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_2ACR.append(v_entalpia)
                        entalp_qH_CBZ_tetr_2ACR.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'ACR_tetr' and complexo[nome_complexo] == 'CBZ_three_ACR_tetrahydr':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_3ACR.append(v_entalpia)
                        entalp_qH_CBZ_tetr_3ACR.append(v_entalpia_qH)
                    # fim Bloco1

                    # Bloco2: Templete = CBZ, Monomero = IA, Solvente = Tetraidrofurano
                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'IA_tetra' and complexo[nome_complexo] == 'CBZ_one_IA_tetrahydrofu':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_1IA.append(v_entalpia)
                        entalp_qH_CBZ_tetr_1IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'IA_tetra' and complexo[nome_complexo] == 'CBZ_two_IA_tetrahydrofu':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_2IA.append(v_entalpia)
                        entalp_qH_CBZ_tetr_2IA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'IA_tetra' and complexo[nome_complexo] == 'CBZ_three_IA_tetrahydro':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_3IA.append(v_entalpia)
                        entalp_qH_CBZ_tetr_3IA.append(v_entalpia_qH)
                    # fim Bloco2

                    # Bloco3: Templete = CBZ, Monomero = MAA, Solvente = Tetraidrofurano
                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'MAA_tetr' and complexo[nome_complexo] == 'CBZ_one_MAA_tetrahydrof':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_1MAA.append(v_entalpia)
                        entalp_qH_CBZ_tetr_1MAA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'MAA_tetr' and complexo[nome_complexo] == 'CBZ_two_MAA_tetrahydrof':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_2MAA.append(v_entalpia)
                        entalp_qH_CBZ_tetr_2MAA.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'MAA_tetr' and complexo[nome_complexo] == 'CBZ_three_MAA_tetrahydr':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_3MAA.append(v_entalpia)
                        entalp_qH_CBZ_tetr_3MAA.append(v_entalpia_qH)
                    # fim Bloco3

                    # Bloco4: Templete = CBZ, Monomero = VP, Solvente = Tetraidrofurano
                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'VP_tetra' and complexo[nome_complexo] == 'CBZ_one_VP_tetrahydrofu':
                        v_entalpia = prop_fisicas(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_1VP.append(v_entalpia)
                        entalp_qH_CBZ_tetr_1VP.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'VP_tetra' and complexo[nome_complexo] == 'CBZ_two_VP_tetrahydrofu':
                        v_entalpia = prop_fisicas2mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas2mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_2VP.append(v_entalpia)
                        entalp_qH_CBZ_tetr_2VP.append(v_entalpia_qH)

                    if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'VP_tetra' and complexo[nome_complexo] == 'CBZ_three_VP_tetrahydro':
                        v_entalpia = prop_fisicas3mono(monomero[entalpia], templete[entalpia], complexo[entalpia])
                        v_entalpia_qH = prop_fisicas3mono(monomero[entalpia_qH], templete[entalpia_qH], complexo[entalpia_qH])
                        entalp_CBZ_tetr_3VP.append(v_entalpia)
                        entalp_qH_CBZ_tetr_3VP.append(v_entalpia_qH)
                    # fim Bloco4




            '''
            # Graficos Acetonitrila
            if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'ACR_acet' \
               and monomero1 == 'ACR' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_acet_1ACR, entalp_qH_CBZ_acet_1ACR,
                                       entalp_CBZ_acet_2ACR, entalp_qH_CBZ_acet_2ACR,
                                       entalp_CBZ_acet_3ACR, entalp_qH_CBZ_acet_3ACR,
                                       monomero1, solvente1, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'IA_aceto' \
              and monomero2 == 'IA' and propriedade_geral1 == 'entalpia':
              graficando_propriedades(interval_temp,
                                      entalp_CBZ_acet_1IA, entalp_qH_CBZ_acet_1IA,
                                      entalp_CBZ_acet_2IA, entalp_qH_CBZ_acet_2IA,
                                      entalp_CBZ_acet_3IA, entalp_qH_CBZ_acet_3IA,
                                      monomero2, solvente1, templete1, propriedade_geral1)

            if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'MAA_acet' \
              and monomero3 == 'MAA' and propriedade_geral1 == 'entalpia':
              graficando_propriedades(interval_temp,
                                      entalp_CBZ_acet_1MAA, entalp_qH_CBZ_acet_1MAA,
                                      entalp_CBZ_acet_2MAA, entalp_qH_CBZ_acet_2MAA,
                                      entalp_CBZ_acet_3MAA, entalp_qH_CBZ_acet_3MAA,
                                      monomero3, solvente1, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'VP_aceto' \
              and monomero4 == 'VP' and propriedade_geral1 == 'entalpia':
              graficando_propriedades(interval_temp,
                                      entalp_CBZ_acet_1VP, entalp_qH_CBZ_acet_1VP,
                                      entalp_CBZ_acet_2VP, entalp_qH_CBZ_acet_2VP,
                                      entalp_CBZ_acet_3VP, entalp_qH_CBZ_acet_3VP,
                                      monomero4, solvente1, templete1, propriedade_geral1)

            # Graficos  CBZ Diclorometano
            if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'ACR_dich' \
               and monomero1 == 'ACR' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_diclo_1ACR, entalp_qH_CBZ_diclo_1ACR,
                                       entalp_CBZ_diclo_2ACR, entalp_qH_CBZ_diclo_2ACR,
                                       entalp_CBZ_diclo_3ACR, entalp_qH_CBZ_diclo_3ACR,
                                       monomero1, solvente2, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'IA_dichl' \
               and monomero2 == 'IA' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_diclo_1IA, entalp_qH_CBZ_diclo_1IA,
                                       entalp_CBZ_diclo_2IA, entalp_qH_CBZ_diclo_2IA,
                                       entalp_CBZ_diclo_3IA, entalp_qH_CBZ_diclo_3IA,
                                       monomero2, solvente2, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'MAA_dich' \
               and monomero3 == 'MAA' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_diclo_1MAA, entalp_qH_CBZ_diclo_1MAA,
                                       entalp_CBZ_diclo_2MAA, entalp_qH_CBZ_diclo_2MAA,
                                       entalp_CBZ_diclo_3MAA, entalp_qH_CBZ_diclo_3MAA,
                                       monomero3, solvente2, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_dich' and monomero[nome_monomero] == 'VP_dichl' \
               and monomero4 == 'VP' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_diclo_1MAA, entalp_qH_CBZ_diclo_1MAA,
                                       entalp_CBZ_diclo_2MAA, entalp_qH_CBZ_diclo_2MAA,
                                       entalp_CBZ_diclo_3MAA, entalp_qH_CBZ_diclo_3MAA,
                                       monomero4, solvente2, templete1, propriedade_geral1)

            # Graficos  CBZ Dimetilsufoxido
            if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'ACR_dime' \
               and monomero1 == 'ACR' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_dime_1ACR, entalp_qH_CBZ_dime_1ACR,
                                       entalp_CBZ_dime_2ACR, entalp_qH_CBZ_dime_2ACR,
                                       entalp_CBZ_dime_3ACR, entalp_qH_CBZ_dime_3ACR,
                                       monomero1, solvente3, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'IA_dimet' \
               and monomero2 == 'IA' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_dime_1IA, entalp_qH_CBZ_dime_1IA,
                                       entalp_CBZ_dime_2IA, entalp_qH_CBZ_dime_2IA,
                                       entalp_CBZ_dime_3IA, entalp_qH_CBZ_dime_3IA,
                                       monomero2, solvente3, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'MAA_dime' \
               and monomero3 == 'MAA' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_dime_1MAA, entalp_qH_CBZ_dime_1MAA,
                                       entalp_CBZ_dime_2MAA, entalp_qH_CBZ_dime_2MAA,
                                       entalp_CBZ_dime_3MAA, entalp_qH_CBZ_dime_3MAA,
                                       monomero3, solvente3, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_dime' and monomero[nome_monomero] == 'VP_dimet' \
               and monomero4 == 'VP' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_dime_1VP, entalp_qH_CBZ_dime_1VP,
                                       entalp_CBZ_dime_2VP, entalp_qH_CBZ_dime_2VP,
                                       entalp_CBZ_dime_3VP, entalp_qH_CBZ_dime_3VP,
                                       monomero4, solvente3, templete1, propriedade_geral1)
            '''
            # Graficos  CBZ Tetraidrofurano
            if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'ACR_tetr' \
               and monomero1 == 'ACR' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_tetr_1ACR, entalp_qH_CBZ_tetr_1ACR,
                                       entalp_CBZ_tetr_2ACR, entalp_qH_CBZ_tetr_2ACR,
                                       entalp_CBZ_tetr_3ACR, entalp_qH_CBZ_tetr_3ACR,
                                       monomero1, solvente4, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'IA_tetra' \
               and monomero2 == 'IA' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_tetr_1IA, entalp_qH_CBZ_tetr_1IA,
                                       entalp_CBZ_tetr_2IA, entalp_qH_CBZ_tetr_2IA,
                                       entalp_CBZ_tetr_3IA, entalp_qH_CBZ_tetr_3IA,
                                       monomero2, solvente4, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'MAA_tetr' \
               and monomero3 == 'MAA' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_tetr_1MAA, entalp_qH_CBZ_tetr_1MAA,
                                       entalp_CBZ_tetr_2MAA, entalp_qH_CBZ_tetr_2MAA,
                                       entalp_CBZ_tetr_3MAA, entalp_qH_CBZ_tetr_3MAA,
                                       monomero3, solvente4, templete1, propriedade_geral1)
            if templete[nome_template] == 'CBZ_tetr' and monomero[nome_monomero] == 'VP_tetra' \
               and monomero4 == 'VP' and propriedade_geral1 == 'entalpia':
               graficando_propriedades(interval_temp,
                                       entalp_CBZ_tetr_1VP, entalp_qH_CBZ_tetr_1VP,
                                       entalp_CBZ_tetr_2VP, entalp_qH_CBZ_tetr_2VP,
                                       entalp_CBZ_tetr_3VP, entalp_qH_CBZ_tetr_3VP,
                                       monomero4, solvente4, templete1, propriedade_geral1)

    #print(entalp_CBZ_acet_1MAA)
    #print(entalp_qH_CBZ_acet_1MAA)
    #print(entalp_CBZ_acet_2MAA)
    #print(entalp_qH_CBZ_acet_2MAA)
    #print(entalp_CBZ_acet_3MAA)
    #print(entalp_qH_CBZ_acet_3MAA)
    #interval_temp = np.arange(250, 501, 50)
    #print(interval_temp)
    #print(entalp_CBZ_acet_1VP)
    #print(entalp_CBZ_acet_2VP)
    #print(entalp_CBZ_acet_3VP)
    #print(entalp_qH_CBZ_acet_1VP)
    #print(entalp_qH_CBZ_acet_2VP)
    #print(entalp_qH_CBZ_acet_3VP)
    '''
    graficando_propriedades(interval_temp,
                            entalp_CBZ_acet_1VP, entalp_qH_CBZ_acet_1MAA,
                            entalp_CBZ_acet_2VP, entalp_qH_CBZ_acet_2MAA,
                            entalp_CBZ_acet_3VP, entalp_qH_CBZ_acet_3MAA,
                            monomero3, solvente1, templete1, propriedade_geral1)
    '''
