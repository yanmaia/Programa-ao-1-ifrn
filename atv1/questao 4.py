import sys
diainicial = int(input("Digite o dia inicial: "))
mesinicial = int(input("Digite o mês inicial: "))
diafinal = int(input("Digite o dia final: "))
mesfinal = int(input("Digite o mês final: "))

if mesinicial > mesfinal or (mesinicial == mesfinal and diainicial > diafinal): #checa se o mes inicial e maior que o mes final ou  se as datas sao iguais
    print("A data inicial não pode ser maior que data final. ")
    sys.exit()

# dias da data inicial
diasdatainicial = 0
if mesinicial > 1:
    diasdatainicial = 31 + diasdatainicial  #janeiro
if mesinicial > 2:
    diasdatainicial = 28 + diasdatainicial  #fevereiro
if mesinicial > 3:
    diasdatainicial = 31 + diasdatainicial  #março
if mesinicial > 4:
    diasdatainicial = 30 + diasdatainicial  #abril
if mesinicial > 5:
    diasdatainicial = 31 + diasdatainicial  #maio
if mesinicial > 6:
    diasdatainicial = 30 + diasdatainicial  #junho
if mesinicial > 7:
    diasdatainicial = 31 + diasdatainicial #julho
if mesinicial > 8:
    diasdatainicial = 31 + diasdatainicial  #agosto
if mesinicial > 9:
    diasdatainicial = 30 + diasdatainicial   #setembro
if mesinicial > 10:
    diasdatainicial = 31 + diasdatainicial  #outubro
if mesinicial > 11:
    diasdatainicial = 30 + diasdatainicial  #novembro

diasdatainicial = diainicial + diasdatainicial

# dias da data final
diasdatafinal = 0
if mesfinal > 1:
    diasdatafinal = 31 + diasdatafinal  #janeiro
if mesfinal > 2:
    diasdatafinal = 28 + diasdatafinal  #fevereiro
if mesfinal > 3:
    diasdatafinal = 31 + diasdatafinal  #março
if mesfinal > 4:
    diasdatafinal = 30 + diasdatafinal  #abril
if mesfinal > 5:
    diasdatafinal = 31 + diasdatafinal  #maio
if mesfinal > 6:
    diasdatafinal = 30 + diasdatafinal  #junho
if mesfinal > 7:
    diasdatafinal = 31 + diasdatafinal  #julho
if mesfinal > 8:
    diasdatafinal = 31 + diasdatafinal  #agosto
if mesfinal > 9:
    diasdatafinal = 30 + diasdatafinal  #setembro
if mesfinal > 10:
    diasdatafinal = 31 + diasdatafinal  #outubro
if mesfinal > 11:
    diasdatafinal = 30 + diasdatafinal  #novembro

diasdatafinal = diafinal + diasdatafinal

diferenca_dias = diasdatafinal - diasdatainicial

print(f" dia {diainicial:02} do Mês {mesinicial:02} até  dia {diafinal:02} do mês {mesfinal:02} - {diferenca_dias} dias de diferença.")