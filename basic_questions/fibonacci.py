# Fibonacci dizisi bir sayı dizisidir.
# İlk iki terim 0 ve 1'dir. Diğer tüm terimler, önceki iki terim toplanarak elde edilir.
# {1, 1, 2, 3, 5, 8, 13, 21, …} şeklinde devam eden sonsuz sayılardan oluşur
# Fibonacci sayısını hesaplayan bir program yazalım


def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(n) for n in range(15)])
