import random

""" Elemanları 1-9 arası rakamlar içeren 100 elemanlı bir random bir liste 
üreterek, bu liste üzerinde her bir rakamın kaç defa geçtiğini gösteren bir 
sözlük yapısı kurun. """

liste = []
for i in range(100):
    sayı = random.randint(1, 9)
    liste.append(sayı)
print(liste)

liste2 = []
sözlük = {}
for sayı in liste:
    if sayı in liste2:
        continue
    sayı_hesaplama = liste.count(sayı)
    sözlük.update({sayı: sayı_hesaplama})
    liste2.append(sayı)
print(sorted(sözlük.items()))
