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