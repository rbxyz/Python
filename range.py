#range()
#serve para criar sequencias de numeros que variam de um ponto de partida até  o final
range(0,10)
print(range(0,10))
#não aparace pois nnão solicitamos
list(range(0,10))
print(list(range(0,10)))
#outro ex
r = range(10,25)
#posso usar uma tupla caso queira
print(tuple(r))
print(list(range(10,25)))
#pode tambem especificar o tamanho do passo na seq. com um terceiro argumento
for i in range(0,10):
    print(i)
