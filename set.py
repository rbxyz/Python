#aprender
#reforçar
#-------------------------------------
s=set()
#add()
#adiciona elementos a um set. lembre-se que um set não tomará elementos duplicados e apenas os apresentará uma vez.
s.add(1)
s.add(2)
print(s)
#clear()
#remove todos os elementos de um conjunto
s.clear()
print(s)
#copy()
#retorna um cópia dos sets, as mudanças do original não afetam a cópia.
s={1,2,3}
sc=s.copy()
print(sc)
print(s)
s.add(4)
print(s)
print(sc)
#difference_update()
#a sintaxe é
#set1.difference_update(set2)
#o método retorna set1 depois de remover elementos encontrados no set2
s1={1,2,3}
s2={1,4,5}
s1.difference_update(s2)
print(s2)
#discard()
#remove um elemento do conjunto se for um membro. Se o elemento não for um membro, não faz nada.
print(s)
s.discard()
print(s)


#intersection() e intersection_update()
#retorna a intersecção de dois ou mais sets como um novo set.
#isto é, elementos comuns a todoss os sets
s1={1,2,3}
s2={1,2,4}
s1.intersection(s2)
print(s1)
s1.intersection_update(s2)
#atualiza um set com a intersecção de outro
print(s1)
print("--------------------------------------")
#isdisjoint()
#esse método retornará true se dois conjuntos tiverem uma intersecção nula.
s4={1,2}
s5={1,2,4}
s6={5}
s4.isdisjoint(s5)#não funga assim
print(s4)#
print(s4.isdisjoint(s5))#assim, sim
print(s4.isdisjoint(s6))
print("--------------------------------------")
#issubset()
#esse método informa se outro conjunto contém este conjunto.
print(s1)
print(s2)
print(s1.issubset(s2))
print("--------------------------------------")

#issuperset()
#esse informa se este set contém outro set
print(s1.issuperset(s2))
print("--------------------------------------")
#symmetric_difference()
#isso retorna a diferença simetrica dos dois sets, como um novo, 
#oou seja, os que estão exatamente em apenas de um dos sets
print(s1)
print(s2)
print(s1.symmetric_difference(s2))
print("--------------------------------------")
#union()
#retorna a união de dois sets, ou seja, todos os elementos que estao nos sets.
print(s1.union(s2))
print("--------------------------------------")
#update()
#atualiza um set com a uniao de outro
print(s1.update(s2))


#os conjuntos(sets) são uma coleção não ordenada de elementos únicos. podemos construi-los usando a função set()
x=set()
x.add(1)
print(x)

x.add(2)
print(x)
x.add(1)
print(x)
#ele não põe mais 1 lá, pq umcset apenas se ocupa de elementos exclusivos! pode se criar uma lista destes, mas não atri
#builos separadamente
l=[1,2,3,4,1,2,3,4,5,1,2,3,4]
set(l)
print(set)
#usar quando não quiser repetir elementos.

