# Generator Function


def myGen():
    yield 'A'
    yield 'B'
    yield 'C'

g=myGen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))