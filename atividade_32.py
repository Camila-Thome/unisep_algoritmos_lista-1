### 
#atividade 32
# Aluno : Camila Thome 
# Data: 18/03
###
produto = float(input('digite o valor do produto: '))
proddesc = ((10*100) / produto) 
proddesc2 = produto - proddesc
parc = produto / 3 
comvis = (5/100) * proddesc2
compar = produto * (5/100)
print("o valor do produto com desconto eh R$: ", proddesc2)
print("o valor de cada parcela do produto eh de R$: ", parc)
print("a comissao da venda a vista eh de R$: ", comvis)
print("a comissao para a venda a prazo eh de R$: ", compar)
