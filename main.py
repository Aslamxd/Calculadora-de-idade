from datetime import datetime

ano_nasc = int(input('Em qual ano você nasceu? '))
mes_nasc = int(input('Qual mês vocês nasceu? '))
dia_mesc = int(input('Qual dia você nasceu? '))

data_nasc = datetime(ano_nasc, mes_nasc, dia_nasc)
data_atual = datetime.now

diff = data_atual - data_nasc

dias = diff.days
anos, dias = dias // 365, dias % 365
messes, dias = dias // 30, dias % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias!')          
