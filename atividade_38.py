#atividade 38
# Aluno : Camila Thome 
# Data: 18/03
###
print('Preencha os campos abaixo com o horário atual')
h = int(input('Hora: '))
m = int(input('Minuto: '))
s = int(input('Segundo: '))
d = int(input('\nDuração do evento (segundos): '))
s_final = (s + d) % 60
m_final = ( m + (s+d)//60 ) % 60
h_final = ( h + ( m + (s+d)//60 )//60 ) % 24
print(f'O fim do evento se dará às {h_final}h {m_final}min e {s_final} segundos')