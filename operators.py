import random
import math

# = affectation
foo = 123

# + addition
foo = 123 + 42
foo = foo + 42
# += opérateur d'incrémentation
foo += 42

# - soustraction 
foo = 123 - 42
foo = foo - 42
# -= opérateur de décrémentation
foo -= 42
print(foo)

# / division
foo = 123 / 42
print(foo)

# // division complète
foo = 123 // 42
print(foo)
print(type(foo))

# % modulo
foo = 4 % 3
foo = random.randint(1, 100)
print(foo % 2)

# * multiplication


# ** puissance
foo = 2 ** 4
foo = 5 ** 5
foo = 2 ** 7
print(foo)

# ^ puissance mais pas en python


# math.sqrt() racine carré
foo = math.sqrt(4)
foo = 4 ** 0.5
foo = 8 ** (1/3)
print(foo)

# transtypage
foo = "123"
foo = int(foo)
print(type(foo))

foo = "123"
foo = float(foo)
print(type(foo))

foo = 3.14
foo = int(foo)
print(foo)

foo = 3.14
foo = str(foo)
print(type(foo))

#
foo = 2.71
# récupérer la partie entière 
a = int(foo) 
# la partie après les virgules 
b = foo - a

print(a)
print(b)

# les opérateurs de comparaison
# à ne pas confondre avec l'identité === (qui n'existe pas en python)
result = 1 == 1
print(result)


# les grandeurs
result = 123 < 42
print(result)

# plus petit ou égal à
result = 123 <= 42

print(result)

# plus grand ou égal à
result = 123 >= 42
print(result)

# l'inégalité
result = 123 != 42
print(result) 

# les encadrements 
# <> <= >=
my_number = random.randint(0, 100)
print(my_number)
result = 0 <= my_number <= 50
print(result)

# operateur and (et)
result = True and False
print(result)
result = False and True
print(result)
result = True and True
print(result)
result = False and False
print(result)

a =random.randint(0, 1)
b = random.randint(0, 1)
result = bool(a) and bool(b)
print(a, b)
print(result)

# operateur not
result = not True
print(result)
result = not False
print(result)

# utilisations un peu spéciales des comparaisons de grandeur
result = "abc" > "bcd" # une lettre a un chiffre définie par rapport au ascii (voir sur internet)
print(result)

# transtypage == type casting == conversion d'un type de données

# 0 donne faux tandis que les autres nombres donnent vrai
my_number7 = 10
print(bool(my_number7))

# conversion implicit en booléen
if my_number7:
    print("L'utilisateur a mis autre chose que zéro")
else:
    print("L'utilisateur a mis zéro")    

# listes
fruits = ['grenade', 'mangue']

# opérateur d'inclusion
result = 'mangue' in fruits
print(result)
result = 'fraise' in fruits
print(result)

# conversion explicite en booléen
result = bool(fruits)
print(result)

# conversion implicit en booléen
if fruits:
    print("La liste contient des éléments")
else:
    print("La liste ne contient pas d'éléments")

# mais attention none peut être converti en int ou float
print(bool(None))    

# in 
fruits = ['abricot', 'baies', 'cerise']
result = 'ananas' in fruits
print(result)
result = 'cerise' in fruits
print(result)