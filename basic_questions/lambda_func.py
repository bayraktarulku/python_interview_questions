# lambda, tek satırlık fonksiyonlardır. Bir ya da daha fazla parametre kabul ederler.
# ancak tek bir işlem yapabilirler. Lambda ifadesi, bir işlev nesnesi oluşturur ve
# ayrıca bir işlevi değeri olmayan bir adla birleştirir.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

total = reduce(lambda x, y: x + y, numbers)

print("Sum of list numbers elements is {}".format(total))
