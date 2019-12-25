kalan=[]
sayi = int(input("sayi giriniz:"))
i = 2
while i <= sayi:
    if sayi % i ==0:
        kalan.append(i)
        sayi = sayi / i
    i += 1
print(kalan)
