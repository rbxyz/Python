#métodos especiais para utilizar
l = [1,2,3]
#use o método append() para adicionar permantentemente um item ao final de uma lista

l.append('append me!')
print(l)

#e use pop() para dropar um item da lista

l.pop(0)
print(l)

#e para ver qual item foi drop antes

popped_item=l.pop()
print(popped_item)

print(l)
print('------------------------------')
#podemos usar os métodos sort() e reverse() para alterar as listas

new_list=['a','e','x','b','c']
print(new_list)
#use reverse() para reverter a ordem, isso é permanente!!!!!!!
new_list.reverse()
print(new_list)
#use sort()para classficar a lista(nesse caso em ordem alfabética)
new_list.sort()
print(new_list)
