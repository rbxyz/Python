#serve como 'mapeamento de python' 
#são coleções de obetos armazenados por uma key, não armazena em psições relativas
#consiste em uma key e depois um valor associado
#construindo...
#cria um dic com {} e: que significa uma key e um valor
my_dic = {'key1':'value','key2':'value2'}
print(my_dic['key2'])
#armazenam ddados vairados
my_dict = {'key1':123,'key2':[12,23,33], 'key3': ['item0','item1','item2']}
print(my_dict['key3'])
#ou
print(my_dict['key3'][0])
#pode tbm
print(my_dict['key3'][0].upper)
#pode-se alterar valores de chaves
print(my_dict['key1'])
my_dict['key1']=my_dict['key1']-123
print(my_dict['key1'])
#outro método próprio do python, é a adição, subtração divisão ou mult. automática usando +=, -=, /=, *=
my_dict['key1'] -=123
print(my_dict['key1'])
#pode-se tambem criar atribuição num dic.
d = {}
d={'animal':'dog'}
d={'answer':42}
print(d)
#ANINHAMENTO DE DIC.
d = {'key1': {'nestkey': {'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])
#MÉTODOOS DE DICIONÁRIO
a={'key1':1,'key2':2,'key3':3}
print(a.keys())
#RETORNA TODAS AS KEYS
print(d.values)
#PEGA TODOS OS VALORES
print(d.items())
#RETORNA TUPLAS DE TODOS OS ITENS







