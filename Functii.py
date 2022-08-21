#se urmeaza  exemplele din java

def printGreeating():
    print('buna ziua ')

printGreeating()

def printGreatingByName(nume,prenume):
    print(f'buna ziua coiosule {nume}' + ' ' + f'buna ziua libidinosule {prenume}')

printGreatingByName('pula','pizda')

def mediaNumerelor(a,b,c):
    return a+b+c

print(mediaNumerelor(3,3.3,5))

def valoarePi():
    return 3.14

print(valoarePi())

#exercitiu:daca pers e majora,alfel fals
def verificareMajor(varsta):
    if(varsta>=18):
        return True
    else:
        return False
print(verificareMajor(18))

def razaUnuiCerc():
    return 3

def sumaNumerelor(a , b):
    s = a + b
    return s

def cateCaractereAreNumeleTau():
    nume = "Turlea Mihai"
    return len(nume)
def careEsteNumarulCelMaiMare(a,b,c):
    # a=2
    # b=5
    # c=3
    if a>b>c:
        return a
    elif a<b>c:
        return b
    elif a<b<c:
        return c
    elif a>b<c & a>c:
        return a
    elif a>b<c & a<c:
        return c
    else:
        ("Toate numere sunt egale")
#aria cercului
print(valoarePi()* (razaUnuiCerc()*2))

#suma a doua numere
print(sumaNumerelor(12, 9))
#cate caractere are numele tau
print(cateCaractereAreNumeleTau())
# afiseaza numarul cel mai mare
numar1 = int(input(f'introduceti numerele' ))
numar2 = int(input(f'introduceti numerele' ))
numar3= int(input(f'introduceti numerele' ))
print(careEsteNumarulCelMaiMare(numar1,numar2,numar3))
#verificare si implementare de la utilizator
# age = int(input('introduceti varsta dvs'))
# if(verificareMajor(age)):
#     print('bine ai venit in aplicatie')
# else:
#     print('nu poti intra')