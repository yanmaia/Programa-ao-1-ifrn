import sys
vinicial=int(input('Informe um valor inteiro inicial da PG: '))
razaopg=float(input('Informe a Razao da PG: '))
vquantidade=int(input('Informe a quantidade de elementos positivo de uma  PG: '))
valorpg=vinicial
soma=vinicial
if vquantidade<0:           #Verifica se e positivo 
    sys.exit('Informe quantidade de elementos positivos da PG')

elif razaopg == 1 or razaopg == 0:
    print(f"{'-'*10}A PG e  uma constante{'-'*10}")                    #vai verificar as classificações das PG
elif razaopg < 0 :
    print(f"{'-'*10}A PG e uma Oscilante{'-'*10}")
elif valorpg >= 1 < razaopg or 0<razaopg<1>valorpg<0:
    print(f"{'-'*10}A PG e uma crescente{'-'*10}")
elif 0<razaopg<1:
    print(f"{'-'*10}A PG e  uma decrescente{'-'*10}")
print(f'o valor da Pg({1})= {valorpg} ')    
for i in range (2,vquantidade+1):
    print(f'o valor da PG({i})={valorpg} * {razaopg} = {valorpg*razaopg}')                
    valorpg*=razaopg  
    soma+=valorpg
                                          #calculo para saber o valor da PG
print(f'A soma dos valores dessa PG são: {soma}')
num=int(input('informe um outro valor inteiro que corresponde  a enezima posição dessa PG: '))
if num < 0:                       #Verifica se e positivo
    sys.exit('Informe uma quantidade de elementos positivos da PG')           
termoene= vinicial *(razaopg**(num-1))      #Calcula o valor de uma PG em uma enezima posição
print(f'o valor da enezima posição  {num} Da pg acima e {termoene:,}')
