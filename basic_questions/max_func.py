# max() gömülü fonksiyonunun görevi, bir dizi içindeki en büyük öğeyi vermektir.
# Bu fonksiyon aldığı parametrelere göre değişken sonuçlar verebilir.

# En basit kullanımı ile listede yer alan en büyük sayıyı verir
numbers = [5, 6, 7, 1, 9, 1, 1, 5, 9, 1, 5, 7, 8, 4]
print(max(numbers))


# key parametresi ile en uzun ismi yazdırın.
names = ["James", "Mary", "Robert", "Patricia", "John", "Jens"]
print(max(names, key=len))


# key parametresi ile en üst rütbeyi yazdırın
staff = {
    "jen": "Junior",
    "james": "Mid-level",
    "Patricia": "Principal/Architect",
    "John": "Senior",
}


def get_levels(level):
    levels = {"Junior": 0, "Mid-level": 1, "Senior": 2, "Principal/Architect": 3}

    return levels[level]


print(max(staff.values(), key=get_levels))


# Dizide en çok tekrarlanan sayıyı yazdırın
numbers = [2, 7, 5, 6, 7, 1, 9, 1, 1, 5, 9, 1, 5, 7, 8, 4]

again_lot = max(numbers, key=numbers.count)
again_num = numbers.count(again_lot)
print(
    "The most frequent number is {} and it was {} times repeated.".format(
        again_lot, again_num
    )
)
