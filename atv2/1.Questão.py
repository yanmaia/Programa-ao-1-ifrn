ma=float(input('Informe quantas gramas tem o material radioativo:'))       
s=0
mf= ma 
while mf>0.5:         
    mf/=2
    s+= 50 
h= s // 3600                  #Conversão para Hora
res= s % 3600                 #Rest da divisão da hora
m= res // 60                     #conversao para minutos
seg= res % 60                  #Conversão para segundos
print(f'Massa inicial:{ma:.0f} gramas\nMassa final:{mf} gramas\nTempo de Decaimento: {h}:{m}:{seg}')
