x=float(input('Informe as cordenadas iniciais X do robo: '))
y=float(input('Informe as cordenadas iniciais Y do robo: '))
posicao=str(input('informe em forma de string como vai ser o deslocamento do robo: ').upper())
xf=0
yf=0
movimvalido='' 
for i in posicao:
    if i =='U':            #mover cima (U)
        yf= yf +1            
        movimvalido+=i
    elif i =='D':           #mover baixo(D)
        yf=yf -1              
        movimvalido+=i
    elif i =='R':           #mover direita(R)
        xf=xf+1
        movimvalido+=i
    elif i =='L':             #mover Esquerda(L)
        xf=xf-1
        movimvalido+=i      
    elif i =='O':            #mover noroeste/cima-esquerda(O)
        xf= xf-1
        yf= yf+1        
        movimvalido+=i
    elif i =='N':           #mover nordeste/cima-direita(N)
        xf=xf+1
        yf=yf+1
        movimvalido+=i
    elif i =='E':           #mover sudeste/baixo-direita (E)
        xf= xf+1
        yf=yf-1
        movimvalido+=i
    elif i =='W':           # mover sudoeste/baixo-esquerda (W)
        xf=xf-1
        yf=yf-1
        movimvalido+=i
corfinalX= x+xf                 #calcula posiçao final do eixo x
corfinalY= y+yf                  # calcula posiçao final do eixo y
print(f"{'-'*15}A POSIÇÃO INICIAL {'-'*15}\n   CORDENADA X: {x} CORDENADA Y: {y}")         
if  x >0 and y >0: print( "   O ROBÔ COMEÇOU NO 1 QUADRANTE")
elif  x <0 and y >0: print( "   O ROBÔ COMEÇOU NO 2 QUADRANTE")
elif  x <0 and y<0: print( "   O ROBÔ COMEÇOU NO 3 QUADRANTE")                              #Calcula o quadrante que o robô começou
elif  x > 0 and y < 0: print( "   O ROBÔ COMEÇOU NO 4 QUADRANTE")
elif  x == 0 and y == 0: print( "   O ROBÔ COMEÇOU NA ORIGEM")
elif  x == 0 : print( "   O ROBÔ INICIOU NO EIXO X ")
else : print( "   O ROBÔ INICIOU NO EIXO Y ")

print(f"{'-'*15}A POSIÇÃO FINAL {'-'*15}\n   CORDENADA X: {x+xf} CORDENADA Y: {y+yf}")  
if  corfinalX >0 and corfinalY >0: print( "   O ROBÔ TERMINOU NO 1 QUADRANTE")
elif  corfinalX <0 and corfinalY >0: print( "   O ROBÔ TERMINOU NO 2 QUADRANTE")                 #Calcula o Quadrante que o robô terminou
elif  corfinalX <0 and corfinalY <0: print( "   O ROBÔ TERMINOU NO 3 QUADRANTE")
elif  corfinalX > 0 and corfinalY < 0: print( "   O ROBÔ TERMINOU NO 4 QUADRANTE")
elif  corfinalX == 0 and corfinalY == 0: print( "   O ROBÔ ESTA NA ORIGEM")
elif  corfinalX == 0 : print( "   O ROBÔ ESTA NO EIXO X ")
else : print( "   O ROBÔ ESTA NO EIXO Y ")

print(f"{'-'*15} MOVIMENTOS DO ROBÔ {'-'*15}")                     #printa os movimentos do robo e calcula a quantidade
    
print(f"   TEVE {len(movimvalido)} MOVIMENTO EXECUTADOS AO TODO\n   ESSES FORAM OS MOVIMENTOS VALIDOS EXECUTADOS: {movimvalido}")