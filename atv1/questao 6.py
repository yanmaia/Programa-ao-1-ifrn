import sys
from datetime import *

sex= input('Informe seu sexo masculino/feminino: ')
data_nascimento = input('Informe sua data de nascimento no formato DD/MM/AAAA: ')
inicio_contribuicao = input('Informe sua da data de inicio de contribuição no formato DD/MM/AAAA: ')
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
inicio_contribuicao = datetime.strptime(inicio_contribuicao, "%d/%m/%Y").date()

idadeaproximada = (datetime.today().date()- data_nascimento).days // 365
tempocontribuicao = (datetime.today().date() -  inicio_contribuicao).days // 365

if  sex == 'feminino' and tempocontribuicao >= 15 and idadeaproximada >= 62:
    print('Parabens você  já pode se aposentar, e vai se aposentar por idade pois tem {idadeaproximada} anos')
    sys.exit()
elif sex == 'masculino' and tempocontribuicao >= 15 and idadeaproximada >= 65:
    print(f'Parabens você já pode  se aposentar, e vai se aposentar por idade pois tem {idadeaproximada} anos')
    sys.exit()
if sex == 'masculino' and tempocontribuicao >= 35:
    print(f'Parabens você já pode se aposenta, e vai se aposentar por tempo de contribuição  pois tem {tempocontribuicao} anos de contribuição')
    sys.exit()
elif sex == 'feminino' and tempocontribuicao >= 30:
    print(f'Parabens você já pode se aposenta, e vai se aposentar por tempo de contribuição  pois tem {tempocontribuicao} anos de contribuição')
    sys.exit()
else:
    print(f' Sinto muito,você não pode se aposentar,pois possui apenas {tempocontribuicao} anos de contribuição e  {idadeaproximada} anos de idade')