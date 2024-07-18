from glob import glob
import os
import sys
import subprocess


def filtra_diretorios(caminho, itens):
    '''Essa fução recebe um caminho e um conjunto de elementos que estão no
    caminho desejado e devolve uma lista diretórios. Por exemplo:
    O diretório corrente ./ apresenta os seguintes itens ['a.py', 'A', 'B'], a
    função irá retornar ['A', 'B']. '''

    d = [item for item in itens if os.path.isdir(os.path.join(caminho, item))
              and not item.startswith('.')]
    return d

def le_arquivos_e_pega_geo(caminho):
    '''
    Essa função recebe um caminho e trata o conteudo de um arquivo.xyz devolvendo
    somente a geometria desse arquivo.
    '''
    with open(caminho_arquivos, 'r') as f:
        conteudo_em_lista = f.readlines()[2:]
        conteudo_em_string = ''.join(conteudo_em_lista)
        #print(conteudo_em_string)

    return conteudo_em_string


if __name__ == '__main__':

    caminho = '.'
    try:
        itens = os.listdir(caminho)
        #print(itens)
        diretorios = filtra_diretorios(caminho, itens)
        print(f"Existem {len(diretorios)} diretorios em '{caminho}'.")
        print(f"Os diretórios em '{caminho}' são':\n")

        print(60*'-')
        for diretorio in diretorios:
            print(diretorio)
        print(60*'-')


        # Entrar em cada diretório e listar seu conteúdo
        for diretorio in diretorios:
            caminho_dir_correte = os.path.join(caminho, diretorio)
            #print(caminho_dir_correte)
            #print(f"\nEntrando no diretório: {caminho_dir_correte}")

            sub_itens = os.listdir(caminho_dir_correte)
            #print(sub_itens)

            sub_diretorios = filtra_diretorios(caminho_dir_correte, sub_itens)
            #print(f"Os {sub_diretorios} são subdiretorios de {caminho_dir_correte}")

            for sub_diretorio in sub_diretorios:
                caminho_sub_itens = os.path.join(caminho_dir_correte, sub_diretorio)
                print(caminho_sub_itens)
                new_sub_itens = os.listdir(caminho_sub_itens)
                #print(f"O diretorio {sub_diretorio} apresenta os itens: ")
                arquivos = [item for item in new_sub_itens if not item.startswith('.')]

                novo_diretorio = caminho_sub_itens + '/Calcs_Orca'
                subprocess.run(['mkdir', '-p', novo_diretorio], check=True)
                print(novo_diretorio)

                for arquivo in arquivos:
                    #print(arquivo)
                    caminho_arquivos = os.path.join(caminho_sub_itens, arquivo)
                    geometria = le_arquivos_e_pega_geo(caminho_arquivos)

                    nome = arquivo.replace('.xyz', '.inp')
                    #print(nome)
                    arq_calculo = novo_diretorio + f'/{nome}'

                    metodo = "B3LYP"
                    base = "def2-SVP"
                    tipo_calculo = "Opt"
                    carga = 0
                    multiplicidade = 1

                    #print(arq_calculo)
                    with open(arq_calculo, 'w') as f:
                        print(f"! {metodo} {base} {tipo_calculo}\n", end='\n', file=f)
                        print(f"* xyz {carga} {multiplicidade}", end='\n', file=f)
                        print(geometria, end='', file=f)
                        print(f"*\n", end='\n', file=f)

                    #Para cada arquivo .inp gerado deve ser executado um cálculo do ORCA.
                    #Portanto esse programa deve exercutar os arquivos .inp na pasta
                    #Calcs_Orca. Os passos que ainda devem serem realizados são:
                    # 1) No diretorio Calcs_Orca executar os cálculos e não lembro o resto das tarefas.    

    except Exception as e:
        print(f"Erro ao listar diretórios: {e}")
