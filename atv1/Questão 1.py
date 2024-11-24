import sys
num=int(input('Digite um numero de até 4 digitos de 0 a 9999: ')) 
if num>9999 or num<0:  #checa caso tenha um numero menor 0 ou maior 9999
    print('Esse numero não e valido,digite um numero entre 0 e 9999 ')
    sys.exit()
soma1= int(num % 10 +(num//10)%10 + (num//100)%10+ (num // 1000) % 10)     # calculo para pegar a unidade,dezena,centena e milhar.

print (f'A soma dos algarismos e: ',soma1) 