import random

"""Code a program that finds the closest 2 numbers among 100 randomly generated numbers and prints the difference between them."""
"""Rastgele oluşturulmuş 100 sayı arasından en yakın 2 sayıyı bulan ve aralarındaki farkı yazdıran bir program kodlayın."""

fark = 0
list1 = []
for i in range(100):
    x = random.randint(1, 100000)
    list1.append(x)

sozluk_2 = {}
for rakam1 in list1:
    for rakam2 in list1:

        if rakam1 == rakam2:
            continue

        if rakam1 > rakam2:
            fark = rakam1 - rakam2
            if fark < 0:
                fark = fark * -1
            sozluk_2.update({fark: [rakam1, rakam2]})

        elif rakam2 > rakam1:
            if fark < 0:
                fark = fark * -1
            fark = rakam2 - rakam1
            sozluk_2.update({fark: [rakam1, rakam2]})

sonuc = min(sozluk_2.items())
print(sonuc)
