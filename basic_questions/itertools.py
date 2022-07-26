# Klavyede birden fazla basılan harfi nasıl tamizleriz?
from itertools import groupby


def clean_string(noise):
    str = groupby(noise)
    return "".join(chr for chr, _ in str)


print(clean_string("muuuurphy"))


# tanımlanan grup üzerinde yineleme yapmak için de "groupby" kullanabiliriz.
things = [
    ("animal", "bear"),
    ("animal", "duck"),
    ("plant", "cactus"),
    ("vehicle", "school bus"),
]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A {} is a {}.".format(thing[1], key))
