import sys
vinicial=int(input('Informe um valor inteiro inicial da PA: '))
razaopa=float(input('Informe a Razao da PA: '))
vquantidade=int(input('Informe a quantidade de elementos positivo de uma  PA: '))
valorpa=vinicial
soma=vinicial 
if vquantidade<0:           #Verifica se e positivo 
    sys.exit('Informe quantidade de elementos positivos da PG')
elif razaopa == 0:
    print(f"{'-'*10}A PA e  uma constante{'-'*10}")
elif razaopa>0:                                                                # #vai verificar as classificações das PA
    print(f"{'-'*10}A PA e uma crescente{'-'*10}")
elif razaopa<0: 
    print(f"{'-'*10}A PA e  uma decrescente{'-'*10}")
print(f'o valor da PA({1})= {valorpa} ')
for i in range (2,vquantidade+1):     
    print(f'o valor da PA({i})={valorpa} + {razaopa} = {valorpa+razaopa}')
    valorpa=vinicial+(i-1)*razaopa                   #Formula do calculo da PA
    soma+=valorpa
print(f'A soma dos valores dessa PA são: {soma:} ')
num=int(input('informe um outro valor inteiro que corresponde  a enezima posição dessa PA: '))            
termoene= vinicial +(num-1)*razaopa      #Calcula o valor de uma Pa em uma enezima posição
print(f"o valor da enezima posição  {num} e {termoene:,}")
