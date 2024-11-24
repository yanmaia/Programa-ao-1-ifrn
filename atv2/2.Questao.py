import sys
n1=int(input('Informe algum numero inteiro positivo: '))
n2=int(input('Informe algum numero inteiro positivo: '))
dividendo=n1
divisor=n2
resto= n1%n2
if (n1 or n2) <= 0:                       
    sys.exit('informe um numero inteiro e positivo')                      #verifica se e inteiro positivo     
while resto != 0:                  
    dividendo=divisor
    divisor=resto                                                             #calculo dos mdc
    resto= dividendo%divisor                                
print(f"Os numeros {n1} e {n2}  possuem o mdc {divisor}")
