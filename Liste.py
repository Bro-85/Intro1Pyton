# listele in pyton pot sa cuprinda eleme de tipuri diferite
# au dimensiune dinamica
fructe = ["mar", 125 ,True , "portocala", 125]
print(fructe)
# accesam un element in functie de index
print(fructe[3])
#adaugam un nou element
fructe.append('rosie')
#suprascriem
fructe[0] = 'para'
print(fructe)
#aflam dimensiunea
print((len(fructe)))
#scoate si ne da ultimul element
last = fructe.pop()
print(last)
print(fructe)
#de cate ori apare un elemnt in lista
print(fructe.count(125))
#extinderea listei actuale cu o alta lista
fructe_exotice = [ 'ananas', 'kivi']
fructe.extend(fructe_exotice)
print(fructe)