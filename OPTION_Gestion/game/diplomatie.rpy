label diplomatie:

    $ random_chef = liste_chefs[renpy.random.randint(0, len(liste_chefs)-1)]
    $ random_requete = liste_requetes[renpy.random.randint(0, len(liste_requetes)-1)]

python:

    res1_egal_res2 = True
    
    num_random_ressource_1 = renpy.random.randint(0,len(liste_noms_ressources)-1)

    while res1_egal_res2:
        num_random_ressource_2 = renpy.random.randint(0,len(liste_noms_ressources)-1)
        if num_random_ressource_1 != num_random_ressource_2:
            res1_egal_res2 = False

    nom_random_ressource_1 = liste_noms_ressources[num_random_ressource_1]
    nom_random_ressource_2 = liste_noms_ressources[num_random_ressource_2]
    nom_random_ressource_2_bis = liste_noms_ressources_bis[num_random_ressource_2]
    val_random_ressource_1 = liste_valeurs_ressources[num_random_ressource_1]
    val_random_ressource_2 = liste_valeurs_ressources[num_random_ressource_2]

    if num_random_ressource_1 == 0:
        random_ressource_1_requete = 100 + renpy.random.randint(0,100)
    elif num_random_ressource_1 == 1:
        random_ressource_1_requete = 25 + renpy.random.randint(0,50)
    elif num_random_ressource_1 == 2:
        random_ressource_1_requete = 2000 + renpy.random.randint(0,1000)
    elif num_random_ressource_1 == 3:
        random_ressource_1_requete = 4 + renpy.random.randint(0,4)

    """ switch (num_random_ressource_1){

        case 0: random_ressource_1_requete = 50 + renpy.random.randint(0,100)
        case 1: random_ressource_1_requete = 25 + renpy.random.randint(0,50)

    } """
    
    if num_random_ressource_2 == 0:
        random_ressource_2_requete = 50 + renpy.random.randint(0,100)
    elif num_random_ressource_2 == 1:
        random_ressource_2_requete = 25 + renpy.random.randint(0,50)

    """ switch (num_random_ressource_2){

        case 0:
            random_ressource_2_requete = 50 + renpy.random.randint(0,100)
        case 1:
            random_ressource_2_requete = 25 + renpy.random.randint(0,50)

    } """

"Le chef [random_chef] vous propose un échange :"
"[random_requete]"
"[random_ressource_1_requete] [nom_random_ressource_1] contre [random_ressource_2_requete] [nom_random_ressource_2]"

"Voulez-vous accepter cet échange ?"

label menu_diplomatie :

    menu:
        "Oui" if val_random_ressource_2 >= random_ressource_2_requete:
            $ val_random_ressource_2 -= random_ressource_2_requete
            $ val_random_ressource_1 += random_ressource_1_requete
            "Vous réalisez l'échange !"
            jump fin_diplomatie
        "{color=#dddddd} Vous n'avez pas assez [nom_random_ressource_2_bis] {/color}" if val_random_ressource_2 < random_ressource_2_requete:
            jump menu_diplomatie
        "Non":
            "Vous refusez la transaction."
            jump fin_diplomatie