lista=[1, 2, 3]
print(*lista, sep= '4', end= '\n', )
print(*lista, end= '\n')
print('1 2 3')

def func(*asd, **kwargs):
    print(asd)
    print(asd[0])
    print(asd[2])
    asd= list(asd)
    print(asd)
    asd.append(4)
    print(asd)
    print(kwargs)
    print(type(kwargs))
    print(kwargs['nome'])
    print(kwargs['sobrenome'])
    print(kwargs['nome'], kwargs['sobrenome'])
    kwargs=list(kwargs)
    print(kwargs)
    kwargs.append('fruta')
    kwargs.append('abacate')
    print(kwargs)
    kwargs= tuple(kwargs)
    print(kwargs)

func(1, 2, 3, nome= 'vinicios', sobrenome= 'neves', idade= 19)
lista= {'post': ['a', 'b', 'c'], 'nome': 'vinicios'}
for c in range(100, -1, -1):
    print(c)

for c in lista:
    print(lista[c])
