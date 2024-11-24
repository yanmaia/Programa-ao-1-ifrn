minutos=int(input('Digite quantos minutos ficou estacionado: '))

hora=minutos//60
valorpag=0

if minutos % 60 > 0:  #checa caso a tenha a  parte de uma hora
    hora = hora +1
if minutos <= 120:  # o valor e 8 reais
    valorpag= hora  * 8
if minutos <= 240:         # o valor e 5
    valorpag= 16+ (hora-2) * 5
if minutos <= 720: # o valor e 3 reais
    valorpag = 26 + (hora - 4) * 3

else:
    valorpag= 30
print (f"o valor para pagar no estacionamento : R$ {valorpag:.2f}  Reais")