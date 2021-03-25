
default nombre_alliers_max = 5
default nombre_alliers = 0
default nombre_territoires_max = 15
default nombre_territoires = 1

default liste_noms_ressources = ["kg d'or","soldats","litres d'eau potable","tonnes de nourriture"]
default liste_noms_ressources_bis = ["d'or"," de soldats","d'eau potable","de nourriture"]
default liste_valeurs_ressources = [gold,nbrSoldats,water,food]
default liste_chefs = ["Le duché d'Éternia","Eisenberg","Grandnavire","Ancheim","Florem","Caldisla"]
default liste_requetes = []

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



label start:

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
