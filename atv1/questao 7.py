import math
import sys
l1=float(input('Informe o comprimento  do lado 1: '))
l2=float(input('Informe o comprimento  do lado 2: '))
l3=float(input('Informe o comprimento  do lado 3: '))
if l1 + l2 <= l3 or l1 + l3 <= l2  or l2 + l3 <= l1:  #checagem para saber se e um triangulo
    print (  'Não e possivel formar  um triângulo com esses lados')
    sys.exit()

print(f"{'-'*25}Classificação  do triângulo por lado {'-'*25}")
 
 #verificação por lado do triangulo
if (l1 == l2 ==l3):    #Equilatero
        print('E um triângulo Equilatero')
elif (l1 == l2 != l3) or  (l1 == l3 != l2)   or  (l2 == l3 !=l1):  # isóceles
    print ('E um triângulo isóceles')
else:   #triangulo escaleno
    print ('E um triângulo escaleno')

    #calculo coseno

rad_a = math.acos((l2 ** 2 + l3 ** 2 - l1 ** 2) / (2 * l2 * l3))
rad_b = math.acos((l1 ** 2 + l3 ** 2 - l2 ** 2) / (2 * l1 * l3))
rad_c = math.acos((l2 ** 2 + l1 ** 2 - l3 ** 2) / (2 * l1 * l2))

#converter para graus
graus_a = math.degrees(rad_a)
graus_b = math.degrees(rad_b)
graus_c = math.degrees(rad_c)

print(f"{'-'*25}Classificação do triângulo pelos angulos {'-'*25}")
 
#verificaçao graus
if graus_a < 90  and graus_b < 90 and  graus_c < 90: #acutangulo
    print('E um triângulo Acutângulo')
elif graus_a == 90 or graus_b == 90 or graus_c == 90: #retangulo
    print('E um triângulo Retângulo')
else:  #obtusangulo
    print( 'E um triâgulo obtusângulo') 
