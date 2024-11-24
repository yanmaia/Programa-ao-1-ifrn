import sys
num=int(input("Informe numero inteiro e positivo para verificarmos se e triangular: "))
contador=1
numerotri=0
if num<0:
    sys.exit("Informe um numero positivo para da certo o calculo")
while  True:
    numerotri=(contador/2) * (2*1+(contador-1)*1)                  #Calcula os numeros triangulares  pela formula
    contador+=1                                                    
    if numerotri == num:                                              #Checa se o numero informado pelo usuario corresponde a formula acima
        sys.exit(f"{'-'*10} {num} E um numero triangular{'-'*10}") 
    if numerotri> num:                                  
        sys.exit(f"{'-'*10} {num} Não e um numero triangular{'-'*10}")  
