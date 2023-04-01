#verifica se a strig é algum caso(????????????????????)
s='hello'
#retorna-rá true se todos os caracteres em uma string forem alfanuméricos
num=s.isalnum()
print(num)
#vai retornar true se todos os caracteres de uma string forem alfabéticos
alfa=s.isalpha()
print(alfa)
#vai retornar true se todos os caracteres de uma string forem minusculos, falso caso contrario
lower=s.islower()
print(lower)
#vai retornar true se todos os caracteres de uma string forem espaços em branco
spacce=s.isspace()
print(spacce)
#vai retornar true se todos os caraceres de uma string forem maiusculos, falso caso contrario
supp=s.issuper() 
print(supp)
#outro é o endswith que é essencialmente o mesmo qu uma verificação booleana em s[-1]
ends=s.endswith('o')
print(ends)



