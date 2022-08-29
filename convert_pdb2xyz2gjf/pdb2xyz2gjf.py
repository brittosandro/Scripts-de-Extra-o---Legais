##############################################################################
#
#  O objetivo deste script é converter as geometrias de um conjunto de arquivos
# no formato pdb para um formato xyz e por fim criar inputs gjf para o programa
# Gaussian.
#
#  Os arquivos .pdb estão no diretório corrente e todos serão convertidos para
# um formato .xyz. Portanto utilizaremos um conjunto de parâmetros específicos
# para criar os arquivos .gjf como inputs para o programa Gaussian.
#
##############################################################################

from glob import glob
import subprocess


arquivos_pdb = glob('*.pdb')
for i, arq in enumerate(arquivos_pdb):
     arq_xyz = arq.replace('pdb', 'xyz')
     subprocess.run(['obabel', f'{arq}', '-O', f'{arq_xyz}'])

arquivos_xyz = glob('*.xyz')
for j, arq1 in enumerate(arquivos_xyz):
    with open(arq1, 'r') as f:
        s_arq = f.read()
        sim_e_xyz = s_arq.split('\n')
        arq_gjf = arq1.replace('xyz', 'gjf')
        nome_mol = arq_gjf.replace('.gjf', '')

        cabecalho_gaussian = f'''%nprocshared=10
%mem=48gb
%chk={nome_mol}
#p b3lyp/6-311g(d) opt'''

        with open(arq_gjf, 'w') as file:
            print(cabecalho_gaussian, end='\n', file=file)
            print(end='\n', file=file)
            print(f'{nome_mol}', end='\n', file=file)
            print(end='\n', file=file)
            print('0 1', end='\n', file=file)
            for linha in sim_e_xyz[2:]:
                print(linha, end='\n', file=file)
            print(end='\n', file=file)

arquivos_gjf = glob('*.gjf')
nova_str = str()
for arq in arquivos_gjf:
    with open(arq, 'r') as f:
        s_arq = f.read()
    nova_str += s_arq + '--link--' + '\n'

nova_str_sem_ultimo_link = nova_str[:len(nova_str)-(len('--link--')+len('\n'))]
print(nova_str_sem_ultimo_link)

todos_juntos = 'todos_juntos.gjf'
with open(todos_juntos, 'w') as file:
    print(nova_str_sem_ultimo_link, end='\n', file=file)
