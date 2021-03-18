default nombre_alliers_max = 5
default nombre_alliers = 0
default nombre_territoires_max = 15
default nombre_territoires = 1

default gold = 200

default liste_chefs = ["Alfred","Bertrand","Cunégonde","Delphine","Eric"]
default liste_requetes = []

label start :

    $ liste_requetes.append("Je vous propose cet échange :")
    $ liste_requetes.append("J'aurai besoin de certaines ressources :")
    $ liste_requetes.append("Bonjour, que diriez-vous de commercer ?")
    $ liste_requetes.append("Suite à des problèmes de logistique, j'aurai besoin de ceci :")
    $ liste_requetes.append("Êtes-vous prêt à échanger ces ressources ?")

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