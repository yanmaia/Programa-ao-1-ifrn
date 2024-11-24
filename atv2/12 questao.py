mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave: ".lower())
chaveindex = 0
# Criptografia
mensagemcrpit = ""

for x in mensagem:
    if x.isalpha():                  #para aceitar apenas letras
        ordem = ord(chave[chaveindex % len(chave)]) - ord('a')
        if x.islower():
            mensagemcrpit+= chr((ord(x) - ord('a') + ordem) % 26 + ord('a'))                  #faz o calculo para transformar em numero as letras minusculas
        elif x.isupper():
            mensagemcrpit += chr((ord(x) - ord('A') + ordem) % 26 + ord('A'))               #faz o calculo para transformar em numero as letras miaiusculas
        chaveindex+= 1
    else:
        mensagemcrpit += x  

print("Mensagem criptografada:", mensagemcrpit)

# Descriptografia
mensagemdecripto = ""
chaveindex = 0

for i in mensagemcrpit:
    if i.isalpha():  
        ordem = ord(chave[chaveindex % len(chave)]) - ord('a')
        if i.islower():
            mensagemdecripto += chr((ord(i) - ord('a') - ordem) % 26 + ord('a'))
        elif i.isupper():
            mensagemdecripto += chr((ord(i) - ord('A') - ordem) % 26 + ord('A'))
        chaveindex += 1
    else:
        mensagemdecripto += i  
print("Mensagem descriptografada:", mensagemdecripto)