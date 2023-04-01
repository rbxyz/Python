my_list = ['one', 'two', 'three', 4, 5]
print(my_list)
print(my_list[0])
print(my_list[1:])
print(my_list[:3])
#a partir daq descons
#conc=my_list[0:]+'new'
#print(conc)
#não consegui concatenar
#isso não adiciona permanentemente, só quando atribui a concatenação na vairavel
#-------------------------
#pode-se duplicar uma string
print(my_list*2)
print('exercicio:\n Dada a lista abaixo, faça com qu só seja printado "olá"')
lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]
print(lst[3][1][2][0])
