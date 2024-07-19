from datetime import datetime

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")

dia_mes_ano = data_formatada.split('/')
datas = list(map(lambda x: int(x), dia_mes_ano))

dia_nascimento = int(input('Digite o dia do seu nascimento: '))
mes_nascimento = int(input('Digite o mês do seu nascimento: '))
ano_nascimento = int(input('Digite o ano do seu nascimento: '))

dia_atual = datas[0]
mes_atual = datas[1]
ano_atual = datas[2]

idade = ano_atual - ano_nascimento

if mes_atual < mes_nascimento or mes_atual == mes_nascimento and dia_atual < dia_nascimento:
	idade -= 1

print(f'\nHoje é dia {data_formatada}.')
print(f'Você tem {idade} anos de idade.')

input('\nAperte ENTER para sair...')
