# “The Big Bang Theory” s4b10
# what is the best number?
# “En iyi sayı 73’tür! Çünkü 21. asaldır ve bu da 7 ve 3 ün çarpımıdır.
# 73’ün tersten yazılı hali 37 sayısıdır. Bu da 12. asaldır ve 21’in
# tersten yazılı halidir. 73 aynı zamanda ikilik sistemde 1001001 biçiminde yazılmaktadır.
# 21 sayısı ise 10101 biçiminde olarak yazılır. Bu sayıların her ikisi de palindrom sayılardır.”
# - Dr. Sheldon Cooper

# Kurallar
# kendisi ve tersten yazılışı asal olmalı (73, 37)
# kendisinin rakamlarının çarpımı, sayının kendisi kaçıncı asal sayı ise buna eşit olmalı (73 -> 21. asal && 7*3 = 21)
# Sayının tersten yazılışı kaçıncı asal sayı ise bunun tersten yazılışı
# sayının kaçıncı asal çarpan olduğuna eşit olmalu (73 -> 21. asal && 37 -> 12. asal && 21 ile 12 polindrom)
# ikilik sistemde kendisi ve indexi palindrom olmalı (73 -> 1001001, 21->10101)


class PerfectNumber:
    def __init__(self):
        self.start = 2
        self.end = 100

    def prime(self):
        prime_list = []
        for i in range(self.start, self.end):
            if i == 0 or i == 1:
                continue
            else:
                for j in range(2, int(i / 2) + 1):
                    if i % j == 0:
                        break
                else:
                    prime_list.append(i)
        return prime_list

    def multiplication(self, num):
        resp = 1
        for n in str(num):
            resp *= int(n)

        return resp

    def binary(self, decimal):
        otherBase = ""
        while decimal != 0:
            otherBase = str(decimal % 2) + otherBase
            decimal //= 2
        return otherBase

    def is_palindrome(self, str):
        return str == str[::-1]


lst = PerfectNumber().prime()
perfec_number_list = []
for n in lst:
    reverse_num = int(str(n)[::-1])
    num_indx = lst.index(n) + 1
    if n > 9 and reverse_num in lst:
        reverse_num_indx = lst.index(reverse_num) + 1
        multiply = PerfectNumber().multiplication(str(n))
        if multiply == num_indx:
            if num_indx == int(str(reverse_num_indx)[::-1]):
                bin_num = str(PerfectNumber().binary(n))
                bin_num_indx = str(PerfectNumber().binary(num_indx))
                if PerfectNumber().is_palindrome(
                    bin_num
                ) and PerfectNumber().is_palindrome(bin_num_indx):
                    perfec_number_list.append(n)


print(perfec_number_list)
