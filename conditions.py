import random

if True:
    print("La conditions est vraie")
    print("Ce code est exécutable")

if False:
    print("La conditions est fausse")
    print("Ce code n'est pas exécutable")

conditions_vente = False

if conditions_vente:
    print("L'utilisateur a accepté les conditions de vente")
else:
    print("L'utilisateur n'a accepté pas les conditions de vente")

if not conditions_vente:
    print("L'utilisateur n'a accepté pas les conditions de vente")    
else:
    print("L'utilisateur a accepté les condistions de vente")    

emails = random.randint(0, 100000)

if emails == 1:
    print("Vous avez un nouveau mails")
elif emails > 1:
    print(f"vous avez {emails} nouveaux mails")
else:
    print("vous n'avez pas de nouveaux mails")    


window_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))

print(f'{window_closed = }')
print(f"{electricity_off = }")

if window_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité est coupée")
    print("Les fenêtres sont fermées")
    print("L'électricté n'est pas coupée")
else:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité n'est pas coupée")    


bank_card = True
cash = True

print(f"{bank_card = }")
print(f"{cash = }")

if bank_card or cash:
    print("On a un moyen de paiement")
else:
    print("On a aucun moyen de paiement")    

ticket = True
vip = False
registration = False

print(f'{ticket = }')
print(f'{vip = }')
print(f'{registration = }')

if (ticket or vip) and registration:
    print("Access authorized")
else:
    print("Acces denied")    

product_count = random.randint(0, 50)

if product_count > 20:
    print("Il y a plus de 20 articles")
    print("RAS")
elif 5 < product_count <= 20:
    print("Il y a plus de 5 articles")
    print("RAS")
elif 0 < product_count <= 5:
    print("Il y a plus de 0 articles")
    print("Alerte rupture imminente")
else:
    print("Il n'y a plus d'article")
    print("Alerte Rupture")            


product_count = 6 

if product_count > 5:
    print("Il y a plus de 5 articles")

if product_count <= 20:
    print("Il y a 20 ou moins articles")
    