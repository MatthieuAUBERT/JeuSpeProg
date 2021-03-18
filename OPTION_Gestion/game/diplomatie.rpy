label diplomatie:

    $ random_chef = liste_chefs[renpy.random.randint(0, len(liste_chefs)-1)]
    $ random_requete = liste_requetes[renpy.random.randint(0, len(liste_requetes)-1)]
    $ type_echange = renpy.random.randint(0,0)

    "Le chef [random_chef] vous propose un échange :"
    "[random_requete]"

    "Voulez-vous accepter cet échange ?"
python:

    switch (type_echange){

        case 0:     label menu_diplomatie:
                        menu:
                            "Oui" if gold >= 100:
                                $ gold -= 100
                                "Vous réalisez l'échange !"
                                jump fin_diplomatie
                            "{color=#dddddd} Vous n'avez pas assez d'or {/color}" if gold < 100:
                                jump menu_diplomatie
                            "Non":
                                "Vous refusez la transaction."
                                jump fin_diplomatie
    }