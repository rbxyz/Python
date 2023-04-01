#uma ótima caracteristicas das estruturas de dados de python é que suportam aninhamentos, isso é
#ter estruturass de dados dentro de estruturas de dados, tipo uma lista dentro de outra
#exemplo
#começamos com 3 listas
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
#faça uma lista para formar uma matriz
matrix=[lst_1, lst_2, lst_3]
print(matrix)
#agora dá pra usar a idexação pra pegar elementos, mas agr existem dois níveis para o índice. Os 
#itens n oobjeto matriz e, em seguida, os itens dentro dessa lista

#agora pegamos o primeiro item no objeto da matriz
print(matrix[0])
#agora, o primeiro item do primeiro item no objeto da matriz
print(matrix[0][0])
#agora vou tentar o segundo
print(matrix[0][2])
print('-----------------')
print('exercicios\nOrdene a lista:\nl=[5,3,4,6,1] para [1,3,4,5,6]')
l=[5,3,4,6,1]
l.sort()
print(l)
