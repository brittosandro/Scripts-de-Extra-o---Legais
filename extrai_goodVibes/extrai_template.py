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

def graf_entalpia_um_mono(int_temp, entalp_CBZ_acet_1ACR, entalp_CBZ_acet_1IA,
                         entalp_CBZ_acet_1MAA, entalp_CBZ_acet_1VP):

    sns.set(style="ticks")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Ajusta subplots.
    fig.subplots_adjust(
                          left = 0.100,
                          right = 0.835,    # {Define as distâncias entre os extremos}
                          bottom = 0.14,
                          top = 0.890,
                          hspace = 0.24,   # Organiza espaçoes entre os subplots
                          wspace = 0.23    # Organiza espaçoes entre os subplots
                       )

    fig1 = ax.plot(interval_temp, entalp_CBZ_acet_1ACR, color='k', linewidth=2.8, label='ACR')
    fig2 = ax.plot(interval_temp, entalp_CBZ_acet_1IA, color='b', linewidth=2.8, label='IA')
    fig3 = ax.plot(interval_temp, entalp_CBZ_acet_1MAA, color='r', linewidth=2.8, label='MAA')
    fig4 = ax.plot(interval_temp, entalp_CBZ_acet_1VP, color='y', linewidth=2.8, label='VP')
    fig.legend(loc='upper right', shadow=False, fontsize='large', bbox_to_anchor=(1.01, 0.88),
               frameon=False, title = "Um Monômero", prop = {'size':15})
    plt.grid(False)

    fig.text(0.45,                     # Ordena Posição x
             0.92,                    # Ordena Posição y
             'CBZ em Acetonitrila',      # Texto A ser colocado
             ha='center',            # Alinha texto horizontalmente
             va='center',            # Alinha texto verticalmente
             fontsize = 'xx-large')


    fig.text(0.45,                      # Ordena Posição x
             0.05,                     # Ordena Posição y
             'Temperatura (K)',     # Texto A ser colocado
             ha='center',             # Alinha texto horizontalmente
             va='center',             # Alinha texto verticalmente
             fontsize = 'xx-large')

    fig.text(0.029,
             0.5,
             '$\Delta H$ ($kcal/mol$)',
             ha='center',
             va='center',
             fontsize = 'xx-large',
             rotation='vertical')      # Rotaciona o nome do eixo

    #plt.savefig('HN_nmove_NVT.png', dpi=300, orientation='portrait', transparent=True, format='png')
    plt.show()

def graf_entalpia_dois_mono(interval_temp, entalp_CBZ_acet_2ACR, entalp_CBZ_acet_21IA,
                            entalp_CBZ_acet_2MAA, entalp_CBZ_acet_2VP):

    sns.set(style="ticks")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Ajusta subplots.
    fig.subplots_adjust(
                          left = 0.105,
                          right = 0.820,    # {Define as distâncias entre os extremos}
                          bottom = 0.14,
                          top = 0.890,
                          hspace = 0.24,   # Organiza espaçoes entre os subplots
                          wspace = 0.23    # Organiza espaçoes entre os subplots
                       )

    fig1 = ax.plot(interval_temp, entalp_CBZ_acet_2ACR, color='k', linewidth=2.8, label='ACR')
    fig2 = ax.plot(interval_temp, entalp_CBZ_acet_2IA, color='b', linewidth=2.8, label='IA')
    fig3 = ax.plot(interval_temp, entalp_CBZ_acet_2MAA, color='r', linewidth=2.8, label='MAA')
    fig4 = ax.plot(interval_temp, entalp_CBZ_acet_2VP, color='y', linewidth=2.8, label='VP')
    fig.legend(loc='upper right', shadow=False, fontsize='large', bbox_to_anchor=(1.01, 0.88),
               frameon=False, title = "Dois Monômeros", prop = {'size':15})
    plt.grid(False)

    fig.text(0.45,                     # Ordena Posição x
             0.92,                    # Ordena Posição y
             'CBZ em Acetonitrila',      # Texto A ser colocado
             ha='center',            # Alinha texto horizontalmente
             va='center',            # Alinha texto verticalmente
             fontsize = 'xx-large')


    fig.text(0.45,                      # Ordena Posição x
             0.05,                     # Ordena Posição y
             'Temperatura (K)',     # Texto A ser colocado
             ha='center',             # Alinha texto horizontalmente
             va='center',             # Alinha texto verticalmente
             fontsize = 'xx-large')

    fig.text(0.029,
             0.5,
             '$\Delta H$ ($kcal/mol$)',
             ha='center',
             va='center',
             fontsize = 'xx-large',
             rotation='vertical')      # Rotaciona o nome do eixo

    #plt.savefig('HN_nmove_NVT.png', dpi=300, orientation='portrait', transparent=True, format='png')
    plt.show()



if __name__ == '__main__':
    nome_template = slice(2, 10)
    nome_monomero = slice(2, 10)
    nome_complexo = slice(0, 16)
    temperatura = slice(47, 53)
    entalpia = slice(66, 79)


    dados_templetes = dados_templetes('dados_templetes_output.dat')
    #print(dados_templetes)
    dados_monomeros = dados_monomeros('dados_monomero.dat')
    #print(dados_monomeros)
    dados_complexos = dados_complexos('templete_monomero.dat')
    #print(dados_templestes_monos)

    entalp_CBZ_acet_1ACR = []
    entalp_CBZ_acet_2ACR = []
    entalp_CBZ_acet_3ACR = []

    entalp_CBZ_acet_1IA = []
    entalp_CBZ_acet_2IA = []
    entalp_CBZ_acet_3IA = []

    entalp_CBZ_acet_1MAA = []
    entalp_CBZ_acet_2MAA = []
    entalp_CBZ_acet_3MAA = []

    entalp_CBZ_acet_1VP = []
    entalp_CBZ_acet_2VP = []
    entalp_CBZ_acet_3VP = []


    for templetes in dados_templetes:
        for monomeros in dados_monomeros:
            for complexos in dados_complexos:
                for templete, monomero, complexo in zip(templetes, monomeros, complexos):
                    #print(f'{templete[nome_template]}  |  {monomero[nome_monomero]}  |  {complexo[nome_complexo]}')
                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'ACR_acet' and complexo[nome_complexo] == 'CBZ_one_ACR_acet':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_1ACR.append(entalpia_em_kcal_mol)
                        #entalp_CBZ_acet_2ACR.append(float(templete[entalpia]) + 2*float(monomero[entalpia]))
                        #entalp_CBZ_acet_3ACR.append(float(templete[entalpia]) + 3*float(monomero[entalpia]))

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'ACR_acet' and complexo[nome_complexo] == 'CBZ_two_ACR_acet':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + 2*float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_2ACR.append(entalpia_em_kcal_mol)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'IA_aceto' and complexo[nome_complexo] == 'CBZ_one_IA_aceto':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_1IA.append(entalpia_em_kcal_mol)

                    if templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'IA_aceto' and complexo[nome_complexo] == 'CBZ_two_IA_aceto':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + 2*float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_2IA.append(entalpia_em_kcal_mol)

                    if  templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'MAA_acet' and complexo[nome_complexo] == 'CBZ_one_MAA_acet':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_1MAA.append(entalpia_em_kcal_mol)

                    if  templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'MAA_acet' and complexo[nome_complexo] == 'CBZ_two_MAA_acet':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + 2*float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_2MAA.append(entalpia_em_kcal_mol)

                    if  templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'VP_aceto' and complexo[nome_complexo] == 'CBZ_one_VP_aceto':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_1VP.append(entalpia_em_kcal_mol)

                    if  templete[nome_template] == 'CBZ_acet' and monomero[nome_monomero] == 'VP_aceto' and complexo[nome_complexo] == 'CBZ_two_VP_aceto':
                        valor_entalpia = float(complexo[entalpia]) - (float(templete[entalpia]) + 2*float(monomero[entalpia]))
                        entalpia_em_kcal_mol = valor_entalpia * 627.51
                        entalp_CBZ_acet_2VP.append(entalpia_em_kcal_mol)



    interval_temp = np.arange(250, 501, 50)
    #print(interval_temp)
    #print(entalp_CBZ_acet_1ACR)
    #print(entalp_CBZ_acet_1IA)
    #print(entalp_CBZ_acet_1MAA)
    #print(entalp_CBZ_acet_1VP)

    graf_entalpia_um_mono(interval_temp, entalp_CBZ_acet_1ACR, entalp_CBZ_acet_1IA,
                          entalp_CBZ_acet_1MAA, entalp_CBZ_acet_1VP)

    graf_entalpia_dois_mono(interval_temp, entalp_CBZ_acet_2ACR, entalp_CBZ_acet_2IA,
                          entalp_CBZ_acet_2MAA, entalp_CBZ_acet_2VP)





    #print(s_entalp_CBZ_acet_2ACR)
    #print(s_entalp_CBZ_acet_3ACR)
    #print('-----')
    #print(s_entalp_CBZ_acet_1IA)
    #print(s_entalp_CBZ_acet_2IA)
    #print(s_entalp_CBZ_acet_3IA)


    #for monomeros in dados_monomeros:
    #    print(monomeros)

    #for d_templetes, d_monomeros in zip(dados_templetes('dados_templetes_output.dat'),
    #                                    dados_monomeros('dados_monomero_output.dat')):
        #print(d_templetes, d_monomeros)

        #for dado_temple, dado_mono in zip(d_templetes, d_monomeros):
        #    print(dado_temple[entalpia], dado_mono[entalpia])

        #l = np.concatenate((d_templetes, d_monomeros))
        #print(np.concatenate((d_templetes, d_monomeros)))
        #print(l)
        #for solv in l:
        #    print(solv)
    #print(l)
