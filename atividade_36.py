#atividade 36
# Aluno : Camila Thome 
# Data: 18/03
###
def verificar_numero (numero):
    return 1000 <= numero <= 9999

while True:
    try:
        numero = int(input('digite um numero inteiro de quatro digitos (de 1000 a 9999): '))
        if verificar_numero(numero):
            break
        else:
            print('por favor, insira um numero dentro do intervalo especificado.')
    except ValueError:
            print('por favor, digite um numero valido.')
        
numero_srt = str(numero)

for digito in numero_srt:
            print(digito)