# karmaşık veri türlerini saklamak için kodlamak ve hata ayıklamakla
# uğraşmak yerine Python bu iş için "_pickle" adlı standart modulu kullanılır..
# herhangi bir Python nesnesini dizge ile ifade edilebilecek hale getirebilir ve
# bu halinden geri alabilir.

import _pickle as cPickle

example = ["hello", {"a": 23, "b": True}, (1, 2, 3), [["dogs", "cats"], None]]

# Pickle olarak kaydetme
with open("pickle_example.pkl", "wb") as f:
    cPickle.dump(example, f)

# Kaydedilen .pkl dosyasından okuma
with open("pickle_example.pkl", "rb") as f:
    reloaded = cPickle.load(f)

print(reloaded)
