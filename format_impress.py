s= 'STRING'
print('Place another string with a umod and s: %s' %(s))
#numeros de ponto flutuante
#%n1.n2f onde n1 é o numero minimo de numeros que a cadeia deve conter, e n2
# são quantos numeros para mostrar após o ponto decimal
print('---------------\n')
print('floating point number: %1.2f' %(13.4444))
print('---------------\n')
print('floating point number: %1.0f' %(13.4444))
print('---------------\n')
print('floating point number: %1.5f' %(13.4444))
print('---------------\n')
print('floating point number: %10.2f' %(13.4444))
print('---------------\n')
print('floating point number: %25.2f' %(13.4444))

print('---------------\n')
print('Métodos de formato de conversão')
print('here is a number: %s. here is a string: %s' %(123.1,'hi'))
print('here is a number: %r. here is a string: %r' %(123.1,'hi'))
print('---------------\n')
print('Formatação multipla')
print('first: %s, second %1.2f, third: %r'%('hi', 3.14,22))
print('---------------\n')
print('Usando o método string.metod()')
#a melhor maneira de inttroduzir uma string para isntruções de impressão é usar
#este.
#sintaxe: 
#'string aqui {var1} e tabmbém {var2}'.format(var1 = 'alguma coisa 1', var2 = 'alguma coisa')
print('this is a string with an {p}'.format(p='insert'))
print('---------------\n')
print('oone: {p}, two: {p}, three: {p}'.format(p='hi!'))
print('---------------\n')
print('this is a string with an {p}'.format(p='insert'))
print('---------------\n')
print('object 1: {a}, object 2:: {b}, object 3:{c}'.format(a=1,b='two',c=12.3))
print('---------------\n')
print('ex1: ')
planeta='terra'
diametro=12742
print('o diametro da {a} é de {b} kilômetros.'.format(a=planeta,b=diametro))
#também fungava assim
#print('o diametro da {a} é de {b} kilômetros.'.format(planeta,diametro))
