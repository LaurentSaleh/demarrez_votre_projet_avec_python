# -*- coding: utf8 -*-

import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !","On doit pouvoir choisir entre s'écouter parler et se faire entendre.","Hooo le beau chapeau","Le problème avec les citations tirées d'internet, c'est que l'on est jamais sûr de leur authenticité 'Napoléon Bonaparte'"]

characters = ["alvin et les Chipmunks","Babar","betty boop","calimero","casper","le chat potté","Kirikou"]

def get_random_quote(my_list):
  #get a random number
  rand_numb = random.randint(0, len(my_list)-1)
  item = my_list[rand_numb] #get a quote in the list
  return item #return the item

user_answer = input("Bonjour, entrez B ou 'Enter' et voyez ce qui se passe")

while user_answer != "B":
  print (get_random_quote(quotes))
  user_answer = input("Bonjour, entrez B ou 'Enter' et voyez ce qui se passe")

for character in characters:
    n_character = character.capitalize()
    print(n_character)

print (get_random_quote(quotes))
  #show the quote in an interpreter print()
