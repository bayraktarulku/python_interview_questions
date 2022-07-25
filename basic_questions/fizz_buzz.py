# 1'den 15'e kadar sayıları basan bir program yazın.
# Ancak üçün katları için "Fizz”, beşin katları için ise "Buzz” yazdırın.
# Hem üç hem de beşin katı olan sayılar için "FizzBuzz” yazdırın.

for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    else:
        print(i)
