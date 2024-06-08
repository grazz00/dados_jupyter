dia = int(input("digite o dia:\n"))
mes = int(input("Digite o mes:\n"))
ano = int(input("Digite o ano:\n"))

#28 --> 2
#30 --> 4,6,9,11
#31 --> 1,3,5,7,8,10,12

if(mes == 2): 
    if(dia < 28):
        dia = dia + 1
    elif(dia == 28):
        dia = 1
        mes = mes + 1
    print(dia, '/', mes, '/', ano)
elif(mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
    if(dia < 30):
        dia = dia + 1
    elif(dia == 30):
        dia = 1
        mes = mes + 1
    print(dia, '/', mes, '/', ano)
elif(mes ==1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10):
    if (dia < 31):
        dia = dia + 1
    elif(dia == 31):
        dia = 1 
        mes = mes + 1
    print(dia, '/', mes, '/', ano)
elif(mes == 12):
    if (dia < 31):
        dia = dia + 1
    elif(dia == 31):
        dia = 1 
        mes = 1
        ano = ano + 1 
    print(dia, '/', mes, '/', ano)