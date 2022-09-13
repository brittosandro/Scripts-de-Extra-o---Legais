## Descrição do script ordena_dados_sapt

 - O script tem por objetivo extrair dados de um conjunto de cálculos
 realizados a partir do método SAPT. Neste caso em particular realizamos
 cálculos SAPT em diferentes níveis de perturbação como: SAPT0, SAPT2, 
 SAPT2+, SAPT2+(3) e SAPT2+3, considerando diferentes bases em 
 diferentes sítios de interação.
 
 - Como resultado surgem vários diretórios com a seguinte estrutura.
 
    simboloMolecula_metodoSAPT_base
 
 - Assim o script ordena_dados_sapt.py lê os arquivos dentro de cada
 diretório e ordena em um dicionário por ordem crescente de energia.
 
 - Em um estudo com 4 moléculas de gases nobres interagindo com uma
 molécula de amônia em três sítios distintos, usando os cinco métodos
 SAPT, o usuário teria que analisar cerca de 240 arquivos em um 
 conjunto de aproximadamente 30 valores de energia catalogando os
 dados das energias em ordem crescente. Esse script evita esse esforço.
