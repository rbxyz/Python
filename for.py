l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
    print(num)

print('now, just impress num /2 ')
for num in l:
    if num % 2 == 0:
        print(num)
#with else
for num in l:
    if num %2==0:
        print(num)
    else:
        print('ímpar')
#com contagem durante o loop, vamos criar um for que resume a lista
list_sum=0
for num in l:
    list_sum = list_sum+num
    print(list_sum)

print('---------------------------------------------------')
list_sum=0
for num in l:
    list_sum += num
    print(list_sum)
    #with string
for letter in 'This is a string':
    print(letter)
    #with tupla
tup = (1,2,3,4,5)
for t in tup:
    print(t)
    l = [(2,4),(6,8),(10,12)]
for tup in l:
    print(tup)
#agora desembalando
for (t1,t2)in l:
    print(t1)
d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

for k,v in d.items():
    print(k)
    print(v)


