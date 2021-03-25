default nombre_alliers_max = 5
default nombre_alliers = 0
default nombre_territoires_max = 15
default nombre_territoires = 1

default gold = 150
default nbrSoldats = 20
default water = 5000
default food = 10

default liste_noms_ressources = ["kg d'or","soldats","litres d'eau potable","tonnes de nourriture"]
default liste_noms_ressources_bis = ["d'or"," de soldats","d'eau potable","de nourriture"]
default liste_valeurs_ressources = [gold,nbrSoldats,water,food]
default liste_chefs = ["Le duché d'Éternia","Eisenberg","Grandnavire","Ancheim","Florem","Caldisla"]
default liste_requetes = []

label start :

    $ liste_requetes.append("Je vous propose cet échange :")
    $ liste_requetes.append("J'aurai besoin de certaines ressources :")
    $ liste_requetes.append("Bonjour, que diriez-vous de commercer ?")
    $ liste_requetes.append("Suite à des problèmes de logistique, j'aurai besoin de ceci :")
    $ liste_requetes.append("Seriez-vous disposé à échanger ces ressources ?")
    $ liste_requetes.append("C'est l'heure du troc !")

    default mat_diplomatie = [ [0]*(nombre_alliers_max+1) for i in range(nombre_alliers_max+1)]
    
    python :
        for i in range(nombre_alliers_max+1):
            mat_diplomatie[i][i] = 1

label new_turn :
    
    jump diplomatie

label fin_diplomatie:

label fin_conquete:

    if (nombre_territoires == nombre_territoires_max or nombre_alliers == nombre_alliers_max):
        jump end
    else:
        jump new_turn

label end:

    "Félicitation, vous avez gagné !"