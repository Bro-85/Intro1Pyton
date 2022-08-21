viteza = int(input("introdu viteza actuala : "))
if(viteza<0):
    print("viteza invalida")
elif(viteza <=50):
    print("mergi in localitate")
elif(viteza <= 90):
    print("mergi pe drum judetean")
elif(viteza<=130):
    print("mergi pe autostrada")
else:
    print("redu viteza , iti vei lua amenda")
