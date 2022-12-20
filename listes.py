fruits = ['banane', 'ananas', 'cerise']
print(fruits)

# accès lecture au 0ème élément de la liste
print(fruits[0])

un_fruit = fruits[0]
print(un_fruit)

# accès en écriture au 0ème élément de la liste
fruits[0] = 'abricot'
print(fruits)
print(fruits[0])

index = 0
print(fruits[index])
index += 1 
print(fruits[index])
index += 1 
print(fruits[index])
index += 1
print(f'{index = }')


my_count = len(fruits)

index = 0
if index < my_count:
    print(fruits[index])

index += 1 
if index < my_count:
    print('Première fois')
    print(fruits[index])    

index += 1 
if index < my_count:
    print('Deuxième fois')
    print(fruits[index])  

index += 1 
if index < my_count:
    print('Troisième fois')
    print(fruits[index])  

index += 1 
if index < my_count:
    print('Dernière fois')
    print(fruits[index])  