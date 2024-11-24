valor=float(input('Digite o valor que deseja sacar: '))

nota100=int(valor/ 100)          
valor=valor -(nota100*100) 

nota50=int(valor/50)              
valor=valor - (nota50*50) 

nota20=int(valor/20)         
valor=valor -  (nota20*20) 

nota10=int(valor/10)  
valor= valor - (nota10*10)

nota5=int(valor/5)  
valor= valor -(nota5*5)

nota2=int(valor/2) 
valor=valor - (nota2*2) 

moeda1=int(valor/1) 
valor=valor -(moeda1*1)

moeda50=int(valor/0.50) 
valor=valor - (moeda50 * 0.5)

moeda25=int(valor/0.25) 
valor=valor - (moeda25*0.25)

moeda10=int(valor/0.10)  
valor=valor - (moeda10*0.10)

moeda05=int(valor/0.05)
valor=valor - (moeda05*0.05)

moeda01=round(valor/0.01)      #Usei o round para arredondar sobra de valor  calcula centavos o programa, evitando bug de faltar dinheiro.
        

print(f'  {nota100} cedulas  de 100R$ Reais' )       
print(f'  {nota50} cedulas  de 50R$ Reais' )                            
print(f'  {nota20} cedulas de 20R$ Reais ' ) 
print(f'  {nota10} cedulas de 10R$ Reais ' )
print(f'  {nota5} cedulas  de 5R$ Reais' )       
print(f'  {nota2} cedulas  de 2R$ Reais' )                            
print(f'  {moeda1} moedas de 1R$ Real ' ) 
print(f'  {moeda50} Moeda  de 50 centavos ' ) 
print(f'  {moeda25} Moeda  de 25 centavos ' ) 
print(f'  {moeda10} Moeda  de 10 centavos ' ) 
print(f'  {moeda05} Moeda  de  5 centavos ' ) 
print(f'  {moeda01} Moeda  de  1 centavos ' )