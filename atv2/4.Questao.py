print('esses são os numeros menores que  1 milhão, múltipos de 2 ou 5 que podem ser escritos pela soma das potencias de 5 e de seus digitos')
for i in range(1, 1000000):
    if i % 2 == 0 or i % 5 == 0:   #Comparação multp de 2 e 5
        somapotencia = 0
        num = i
        while num > 0:               #Decompõe o numero para  poder efetuar a soma 
            digito = num % 10                      
            somapotencia += digito ** 5        #soma da potencia 5
            num //= 10           
        if somapotencia == i:                #Verifica se a soma da pot dos digitos e igual ao num
            print(i)
