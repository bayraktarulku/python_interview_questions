### Python mülakatlarında karşımıza çıkabilecek sorular

#### Python’un ana özellikleri nelerdir?
- Python, programlama dili olarak kullanılır ama gerektiğinde scripting işlevi de görür.
- Python, yorumlanabilir derlenmeye ihtiyaç duymaz.
- Değişkenleri belirtilmesine ihtiyaç duymaz. ( “x=123”, x=”iyi günler”)
- Python, nesne yönelimli bir programlama dilidir. Class, composition ve inheritance tanımlamalarına olanak sağlar.
- Fonksiyonları birinci sınıf nesnelerdir. Değişkenlere atanabilir, geri alınabilir ve diğer fonksiyonlara aktarılabilir.

** Otomasyonda, web uygulamalarında, bilimsel modellemede, büyük veri uygulamaları alanlarında kullanılabilir. Diğer dillerin ve bileşenlerin birlikte çalıştırılmasına olanak sağlayan birleştirici bir öğe olarak kullanılabilir.

#### Desteklenen standart veri türleri:
- Number (Sayılar): Sayı veri türleri: Integer, Float, Long Integer ve Complex olarak sıralanabilir.
- str: Harf ya da rakam ve ya kombinasyonlarından oluşur.
- bool: True/False 
- list: Liste’nin içinde; tamsayı, ondalıklı sayı, metin ve Tuple veri türleri yer alabilir.
- tuple: Farklı veri türlerinin bir araya gelerek oluşturduğu veri türüdür. İçerisinde tamsayı, ondalıklı sayı, metin ve hatta iç içe Tuple bile olabilir.
- dict: Dictionary veri türü de Tuple ve List gibi içerisinde farklı veri türlerinin bulunmasına imkan sağlar. {‘one’: 1, ‘two’: 2}

| Tuple | List | 
| ------------- | ------------- |
| Tuple, bir listeye benzer fakat listeden farklı olarak parantez içine alınırlar. | Liste, bir dizi oluşturmak için kullanılır. |
| Eleman ve boyut değiştirilebilir. | Öğe ve boyut değiştirilemez. |
| Güncellenemezler. | Güncellenebilirler |
| Salt okunur listeler olarak hareket ederler. | Değişken bir liste görevi görürler. |
| Tuple Kodu Örneği, tup = (1, “a”, “string”, 1 + 2) | Tuple Kodu Örneği, tup = (1, “a”, “string”, 1 + 2)	Liste Kodu Örneği, L = [1, “a”, “string”, 1 + 2]|

** dict: key:value ilişkisine dayanan haritalamadır. Anahtarlar ve değerler arasında bire bir ilişki tanımlamaya yardımcı olur. Anahtarlar tarafından indekslenen tipik bir sözlük, 
```
>>> thisdict =  {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```
#### Python'ın diğer dillerle karşılaştırılması:
- Açık kaynak.
- Öğrenmesi kolay, kodlaması hızlı
- Python, Windows MFC, Macintosh ve Unix’in X Window sistemi gibi birçok sistem çağrısı, kütüphane ve pencere sistemine yaratılabilir ve taşınabilir GUI uygulamalarını destekler
- Alt düzey modülleri Python yorumlayıcısına eklenerek daha verimli şekilde özelleştirilebilir.
- C ve C ++ veya Java ile karşılaştırıldığında daha yavaştır.
- Mobil işlemlerde verimsizdir.

#### Python’da en çok karşılaşılan hatalar:
- SyntaxError: Yanlış veya eksik noktalama işaretleri, parantez kullanımı, noktalama işaretleri, geçersiz komutlar, geçersiz değişken veya fonksiyon isimleri.
- KeyboardInterrupt: Döngü sonsuz döngüye girmiştir.
- TypeError: mantıksız işlemler yapıldığında oluşur
- NameError: Python’da daha önce tanımlanan değişkenler kullanılması.
- ValueError: Kullanıcıdan int bir input isteyerek yazılan kodda, kullanıcı int dışında bir şey girdiğinde hata verir.
- IndentationError: Boşluk olması gereken yere boşluk konulmazsa, fazla boşluk konulursa bu hata ile karşılaşılır.
- IndexError: IndexError, listelerde index kullanarak eleman çağırırken karşımıza çıkar.

#### Python’da bir listeyi tersine çevirme:
```code
>>> def my_function(x):
...     return x[::-1]
... 
>>> mytxt = my_function("bu metin tersten yazılacak")
>>> print(mytxt)
kacalızay netsret nitem ub
```

#### Python’da bir nesneyi kopyalama
Python’da nesneleri kopyalayabilirsiniz, ama hepsini değil.
```code
>>> import copy
>>> old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> new_list = copy.copy(old_list)
>>> print("Old list:", old_list)
Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> print("New list:", new_list)
New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
#### Python’da map () işlevi nedir?
map(func, iter1) şeklinde kullanılır. Bir fonksiyona, bir datanın elemanları sırasıyla gönderilir ve sonucu tek bir obje olarak geri döner.
```
>>> def myfunc(a, b):
...   return a + b
>>> x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
>>> print(x)
<map object at 0x7face0a2fb20>
>>> print(list(x))
['appleorange', 'bananalemon', 'cherrypineapple']
```

#### Break ve continue nedir?
- Break: döngüyü sonlandırır. Programın kontrolü döngüden hemen sonraki ifadeye geçer.
- Continue: döngü içindeki kodun geri kalanını atlamak için kullanılır. Döngü sona ermez, ancak bir sonraki iterasyona geçer.

#### args & kwargs nedir?
- *args: Sınırsız sayıda parametreli fonksiyon oluşturmak için parametremizin önüne tek yıldız (*) koyulur.
- **kwargs: fonksiyonu çağırırken anahtar değer ilişkisiyle çağırabilir.
- *args ve **kwargs beraber kullanılırken *args daha önce parametre olarak belirtilmeli.

#### Python’da range ve xrange arasında karşılaştırma:
İşlevsellik açısından ikisi aynıdır. (bir tamsayı listesi oluşturmaya izin verir) İkisi arasındaki temel fark, range’in bir Python liste nesnesi döndürürken, xrange’in bir xrange nesnesi döndürmesidir.
```
>>> a = range(1,10000)
>>> x = xrange(1,10000)>>> print (type(a))
>>> print (type(a))
<type 'list'>
>>> print (type(x))
<type 'xrange'>
```

#### Python `__new__` ve `__init__` kullanımı arasındaki farklar nelerdir?
##### `__new__`
- `__new__` metodu, bir sınıfın bir örneği (instance) oluşturulmadan önce çağrılır.
- `__new__` metodu, genellikle değiştirilmek istenen nesne oluşturma sürecini özelleştirmek için kullanılır.
- Bu metot, bir sınıfın örneğini oluşturmak için kullanılır ve __init__ metodundan önce çağrılır.
- Eğer __new__ metodu, `super().__new__(cls)` gibi bir çağrı ile temel sınıfın `__new__` metodunu çağırmazsa, hiçbir örnek oluşturulmaz ve `__init__` metodu hiç çağrılmaz.
- `__new__` metodu, genellikle sınıfın immutability (değiştirilemezlik) gerektiren durumlarında veya özelleştirilmiş bir veri yapısı kullanmak istediğimizde kullanılır.

##### `__init__`
- `__init__` metodu, bir sınıfın örneği oluşturulduktan hemen sonra çağrılır.
- Bu metot, örnek oluşturulduktan sonra örneğe başlangıç değerlerini atamak için kullanılır.
- `__init__` metodu, bir nesneye erişim elde edildikten sonra çalıştırılan ilk kod bloğudur.
- Genellikle nesneye özellikler atanması ve başlangıç durumunun ayarlanması için kullanılır.

```
class MyClass:
    def __new__(cls, *args, **kwargs):
        # Özelleştirilmiş nesne oluşturma işlemleri burada yapılabilir.
        instance = super().__new__(cls)
        # Gerekirse örneğe başlangıç değerleri atanabilir.
        return instance

    def __init__(self, *args, **kwargs):
        # Bu metot, örneğin başlatılması için kullanılabilir.
        pass
```
`__new__` nesnenin oluşturulma sürecini özelleştirmek için kullanılırken, `__init__` oluşturulan nesneye başlangıç değerleri atamak için kullanılır. 
Normal kullanım durumunda, `__init__` sıklıkla daha çok kullanılır, `__new__` ise nadiren ihtiyaç duyulur.

#### Thread (iş Parçacığı)
Bir işin eş zamanlı olarak işlenen her bir bölümü (Kodların sırayla satır satır işleme alındığı bölüm.)
Thread içindeki kodlar sırayla işleme girerler, bir önceki kod satırı çalıştırılmadan bir sonraki çalıştırılmaz. Satırlar birbirlerini beklerler.

#### MultiThread (çok iş parçacıklı)
Birden fazla iş parçacığının bulunduğu senaryodur. Çalışacak olan bir kod bloğunun yanında aynı anda ona paralel olarak çalışmasını istediğimiz kod blokları olabilir.
`Diyelim ki Main Thread’de programımız bir iş yapıyor fakat diğer taraftan da ağ üzerinden bilgi alması gerekiyor. Böyle bir durumda MultiThread ile Main Thread’i engellemeden paralel olarak iş yapabiliriz.`
```
>>> from threading import Thread
>>> def thread_function():
...     for i in range(5):
...             print("Thread ile Çağrıldı: " + str(i))
...             time.sleep(1)
>>> def function():
...     for i in range(5):
...             print(i)
...             time.sleep(3)
... 
>>> thread_fun = Thread(target = thread_function)
>>> thread_fun.start()
>>> function()

0 
Thread ile Çağrıldı: 0 
Thread ile Çağrıldı: 1 
Thread ile Çağrıldı: 2 
1 
Thread ile Çağrıldı: 3 
Thread ile Çağrıldı: 4
2 
3 
4
```
