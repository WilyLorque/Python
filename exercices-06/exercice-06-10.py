# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
   
accumulateur = 0

for item in my_list:
    accumulateur += item

print(round(accumulateur / 6, 2) ) 