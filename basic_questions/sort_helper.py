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

    # Bubble Sorting (Kabarcık Sıralama) algoritması  basit bir yapıya sahiptir.
    # karşılaştırma temelli bir algoritmadır; listenin en
    # başından başlayarak yanında bulunan (-1) sayıya göre kıyaslama yapar.
    # Zaman karmaşası: Tüm elemanları tek tek ve birden fazla kez gezdiği için O(n2)
    def bubble_sort(self, arry):
        for i in range(0, len(arry)):
            for j in range(0, len(arry) - 1):
                if arry[j] > arry[j + 1]:
                    arry[j], arry[j + 1] = arry[j + 1], arry[j]
        return arry


arry = [10, 7, 8, 9, 1, 5]
# print(SortHelper().quick_sort(arry))
print(SortHelper().bubble_sort(arry))
