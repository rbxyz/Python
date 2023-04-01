#servem para agilizar inumeras ações
s='hello world'
#mudando a caixa
#Letras maiusculas no inicio
maiusc_ini=s.capitalize()
print(maiusc_ini)
maiuscula=s.upper()
print(maiuscula)
#caixa alta
minuscula=s.lower()
#caixa baixa
print(minuscula)
print('---------------')
#localização e contagem
count=s.count('o')
print(count)
loc=s.find('o')
print(loc)
print('---------------')
#formatação
#o metodo center() permite que voce coloque sua string 'centrada' entre uma string fornecida com um certo comprimento
center=s.center(20, 'z')
print(center)
#expandtabs() irá converter \t para tabulações
expand='hello\thi'.expandtabs()
print(expand)


