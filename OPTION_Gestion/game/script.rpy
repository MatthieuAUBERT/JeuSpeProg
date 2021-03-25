
#Variables de début de jeu
default gold = 1000
default jour = 0
default water = 200
default food = 200

#Variables pour les bâtiments
default lvlcaserne = 1
default upcaserne=[0,100,200,500,1500,2000]
default prixupcaserne = 0

default lvlhabitation = 1
default uphabitation=[0,100,200,500,1500,2000]
default prixuphabitation = 0

default lvlmine = 1
default upmine=[0,100,200,500,1500,2000]
default prixupmine = 0

default lvlbatimentadmin = 1
default upbatimentadmin=[0,100,200,500,1500,2000]
default prixupbatimentadmin = 0

default lvlterrainagri = 1
default upterrainagri=[0,100,200,500,1500,2000]
default prixupterrainagri = 0

default lvlpuit = 1
default uppuit=[0,100,200,500,1500,2000]
default prixuppuit = 0


#Variables Guerre
default nbrSoldats = 100
default maxSoldats = 550
default territoireConquis = 0
default paysAtt = " "
default AncheimConquis = False
default EterniaConquis = False
default EisenbergConquis = False
default CaldislaConquis = False
default GrandNavireConquis = False
default FloremConquis = False

#Pour définir les bâtiments
define Caserne = Character("Caserne")
define Habitation = Character("Habitation")
define Mine = Character("Mine")
define BatimentAdmin = Character("BatimentAdmin")
define TerrainAgri = Character("TerrainAgri")
define Puit = Character("Puit")

#Diplomatie
default nombre_alliers_max = 5
default nombre_alliers = 0
default nombre_territoires_max = 15
default nombre_territoires = 1

default liste_noms_ressources = ["kg d'or","soldats","litres d'eau potable","tonnes de nourriture"]
default liste_noms_ressources_bis = ["d'or"," de soldats","d'eau potable","de nourriture"]
default liste_valeurs_ressources = [gold,nbrSoldats,water,food]
default liste_chefs = ["Le duché d'Éternia","Eisenberg","Grandnavire","Ancheim","Florem","Caldisla"]
default liste_requetes = []

default flag = True

label start:

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


    scene bg with fade

    "Bienvenue dans ce jeu"
    "Votre but : Conquérir tous les territoires !"
    jump Interface


label Interface :
    show screen Map
    show screen Relations
    show screen City
    show screen Money
    call screen Attaque

label Interface2 :
    "Jour [jour!q]"
    $ flag = True
    $ nbrSoldats += 100 * lvlcaserne
    $ maxSoldats = 550 + (lvlhabitation * 100)
    $ gold += lvlmine * 100
    $ food += lvlterrainagri * 10
    $ water += lvlpuit * 10
    show screen Map
    show screen Relations
    show screen City
    show screen Money
    call screen Attaque


label endA:
    "Félicitations ! Vous avez fini le jeu !"
    return

label endB:
    "Dommage... Vous avez fini en ruine. Le peuple veut votre destitution ! Vous aurez tenu seulement [jour!q] jour(s)."
    return
