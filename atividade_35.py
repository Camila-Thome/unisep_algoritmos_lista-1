#atividade 35
# Aluno : Camila Thome 
# Data: 18/03
###
numero= int(input("Digite um numero inteiro de 100 a 999: "))

if 100 <= numero <= 999:
    centena = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    num_inv = unidades * 100 + dezenas *10 + centena
    print("o numero formado pelos digitos invertidos é: ", num_inv)

else:

    print("Por favor insira um numero de 3 digitos.")
