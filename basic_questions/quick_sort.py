class SortHelper:
    def __init__(self):
        pass

    # Quick Sort (Hızlı Sıralama) algoritması
    # "böl ve yönet" stratejisine dayanan basit ve hızlı bir sıralama yöntemi
    # Zaman karmaşası: O(nlogn) ve en kötü durumda ise O(n2)
    def quick_sort(self, arry):
        if len(arry) < 2:
            return arry

        pivot = arry[0]
        low = [i for i in arry[1:] if i <= pivot]
        high = [i for i in arry[1:] if i > pivot]

        return self.quick_sort(low) + [pivot] + self.quick_sort(high)


arry = [10, 7, 8, 9, 1, 5]
print(SortHelper().quick_sort(arry))
