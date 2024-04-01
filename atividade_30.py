### 
#atividade 30
# Aluno : Camila Thome 
# Data: 18/03
###
horas = float(input('digite a quantidade de horas trabalhadas durante o mês: '))
valor = float(input('qual o valor pago para cada hora trabalhada?: '))
result = horas * valor
result2 = result + result * (10 / 100)
print("o funcionario recebe ao final do mes R$: ", result2)
