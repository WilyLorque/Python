# heredoc string
my_text = """texte test
multiligne
abd
fgy
oui"""

print(my_text)

my_number1 = 123
# interpolation avec une f-string
my_text3 = f"nombre = {my_number1}"
print(my_text3)

# interpolation avec une heredoc string
my_text4 = f"""louis
aofna
amlzenflk
{my_number1}
"""
print(my_text4)

# afficher des acolades dans une heredoc f-string
my_text5 = f"""
{{
  foo  
}}
{{bar}}
"""
print(my_text5)

my_number2 = 3.14
# concaténation de chaînes de caractères
my_text6 = "le nombre Pi est " + str(my_number2)
print(my_text6)

# tronquer un float dans une interpolation
my_number3 = 1 / 3
my_text7 = f"1 / 3 -= {my_number3:.4f}"
print(my_text7)

# les interpolations acceptent les expressions
my_text8 = f"1 + 1 = {1 + 1}"
print(my_text8)

# l'écriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dis bonjour a une personne 

    name str indique de la personne a saluer 
    return None 
    """
    print(f"Salut {name}")

# appel d'une fonction
hello('Toto')

# affiche la doc dans une fonction
# help(hello)

my_text9 = "Lorem ipsum dolor, sit amet consectetur adipisicing elit."
# longueur d'une str
my_number4 = len(my_text9)
print(my_number4)

# trouve la position dans une str
my_number5 = my_text9.find('dolor')
print(my_number5)

my_number6 = my_text9.count('lorem')
print(my_number6)