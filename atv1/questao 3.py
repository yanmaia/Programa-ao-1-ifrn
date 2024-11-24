import sys
horapartida=int(input('Digite a hora de partida entre 0-23 hrs: '))
minutopartida=int(input('Digite os minutos de partida entre 0-59 minutos: '))
horachegada=int(input('Digite a hora de chegada entre 0-23 hrs: '))
minutochegada=int(input('Digite os minutos de chegada entre 0-59 minutos : '))
if horapartida == horachegada and minutopartida == minutochegada:  #checagem caso coloque os numeros iguais
    print("Digite um horario valido.")
    sys.exit()
descanso= int(input('Digite quantos segundos de descanso: '))
litros= float(input('Quantos litros de combustivel gastou na viagem: '))
valorlitro= float(input('Informe o preço do livtro de combustivel em reais: '))
distancia= float(input('Informe quantos km percorreu na viagem : '))

if horapartida > horachegada:                            #checagem caso a viagem vire 1 dia 
    tempototal = (24 - (horapartida + (minutopartida / 60))) + (horachegada + (minutochegada / 60))
else:
    tempototal = (horachegada + (minutochegada / 60)) - (horapartida + (minutopartida / 60))

tempototal= tempototal*3600      #converter hora em segundos


vel_media=   distancia / ((tempototal- descanso)/3600)
vel_mediaglobal= distancia / (tempototal/3600) 

#calcula custo viagem
custoviagem= float(litros * valorlitro)
#desempenho carro
desempenholitro= distancia/ litros
desempenhocusto= custoviagem / distancia

print(f"{'-'*25} DADOS DA VIAGEM {'-'*25}")
print(f'O tempo dessa viagem e {tempototal :.0f}  segundos')
print(f'A velocidade media global {vel_mediaglobal: .2f} km/h')
print(f'A velocidade media de movimento {vel_media: .1f} km/h ')
print(f'o custo da viagem com combusitel e {custoviagem: .1f} R$ reais')
print(f"{'-'*25} DESEMPENHO DO CARRO {'-'*25}")
print(f' o desempenho do carro  e {desempenholitro: .1f}km por litro de gasolina \n o  desempenho do carro em Reais por km rodado e {desempenhocusto: .2f} Reais')
