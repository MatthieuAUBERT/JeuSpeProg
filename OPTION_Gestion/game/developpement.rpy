label developpement :
    hide screen Map
    hide screen Relations
    hide screen City
    hide screen Money
    hide screen Attaque
    show screen village
    call screen returnbutton






label Caserne:
    hide screen village
    show screen caserne

    Caserne "Niveau : [lvlcaserne] {p=0.1}Info : La caserne permet d'augmenter le nombre de troupes créées en début de chaque journée !"

    menu:
        "Retour au village ":
            hide screen caserne
            jump developpement

        "Améliorer" if lvlcaserne<6 :
                jump labupcaserne

label labupcaserne:
    $ prixupcaserne = upcaserne[lvlcaserne]

    menu :
        Caserne "Amélioration de la caserne !"
        "Améliorer la caserne pour [prixupcaserne] Gold " if gold>prixupcaserne:
            $ gold -= prixupcaserne
            $ lvlcaserne += 1
            hide screen caserne
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixupcaserne:
            jump Caserne

        "Ne pas améliorer la caserne ":
            jump Caserne





label Habitation:
    hide screen village
    show screen habitation

    Habitation "Niveau : [lvlhabitation] {p=0.1}Info : Une habitation permet d'augmenter le nombre maximal de troupes que l'on peut stocker !"

    menu:
        "Retour au village ":
            hide screen habitation
            jump developpement

        "Améliorer" if lvlhabitation<6 :
                jump labuphabitation


label labuphabitation:
    $ prixuphabitation = uphabitation[lvlhabitation]

    menu :
        Habitation "Amélioration de l'habitation !"
        "Améliorer l'habitation pour [prixuphabitation] Gold " if gold>prixuphabitation:
            $ gold -= prixuphabitation
            $ lvlhabitation += 1
            hide screen habitation
            jump developpement


        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixuphabitation:
            jump Habitation

        "Ne pas améliorer l'habitation ":
            jump Habitation




label Mine:
    hide screen village
    show screen mine

    Mine "Niveau : [lvlmine] {p=0.1}Info : La mine permet d'augmenter le nombre de d'or reçu en début de chaque journée !"

    menu:
        "Retour au village ":
            hide screen mine
            jump developpement

        "Améliorer" if lvlmine<6 :
                jump labupmine


label labupmine:
    $ prixupmine = upmine[lvlmine]

    menu :
        Mine "Amélioration de la mine !"
        "Améliorer la mine pour [prixupmine] Gold " if gold>prixupmine:
            $ gold -= prixupmine
            $ lvlmine += 1
            hide screen mine
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixupmine:
            jump Mine

        "Ne pas améliorer la mine ":
            jump Mine



label BatimentAdmin:
    hide screen village
    show screen batimentadmin

    BatimentAdmin "Niveau : [lvlbatimentadmin] {p=0.1}Info : Le batiment administratif permet d'augmenter les relations avec les ambassadeurs d'autres villages !"

    menu:
        "Retour au village ":
            hide screen batimentadmin
            jump developpement

        "Améliorer" if lvlbatimentadmin<6 :
                jump labupbatimentadmin


label labupbatimentadmin:
    $ prixupbatimentadmin = upbatimentadmin[lvlbatimentadmin]

    menu :
        BatimentAdmin "Amélioration du bâtiment administratif !"
        "Améliorer le batiment administratif pour [prixupbatimentadmin] Gold " if gold>prixupbatimentadmin:
            $ gold -= prixupbatimentadmin
            $ lvlbatimentadmin += 1
            hide screen batimentadmin
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixupbatimentadmin:
            jump BatimentAdmin

        "Ne pas améliorer le batiment administratif ":
            jump BatimentAdmin



label TerrainAgri:
    hide screen village
    show screen terrainagri

    TerrainAgri "Niveau : [lvlterrainagri] {p=0.1}Info : Le terrain agricole permet d'augmenter les productions de nourritures reçus en début de chaque journée !"

    menu:
        "Retour au village ":
            hide screen terrainagri
            jump developpement

        "Upgrade" if lvlterrainagri<6 :
                jump labupterrainagri


label labupterrainagri:
    $ prixupterrainagri = upterrainagri[lvlterrainagri]

    menu :
        TerrainAgri "Amelioration du terrain agricole !"
        "Ameliorer le terrain agricole pour [prixupterrainagri] Gold " if gold>prixupterrainagri:
            $ gold -= prixupterrainagri
            $ lvlterrainagri += 1
            hide screen terrainagri
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixupterrainagri:
            jump TerrainAgri

        "Ne pas améliorer le terrain agricole ":
            jump TerrainAgri



label Puit:
    hide screen village
    show screen puit

    Puit "Niveau : [lvlpuit] {p=0.1}Info : Le puits permet d'augmenter les productions d'eau reçus en début de chaque journée !"

    menu:
        "Retour au village ":
            hide screen puit
            jump developpement

        "Améliorer" if lvlpuit<6 :
                jump labuppuit


label labuppuit:
    $ prixuppuit = uppuit[lvlpuit]

    menu :
        Puit "Amélioration du puits !"
        "Améliorer le puits pour [prixuppuit] Gold " if gold>prixuppuit:
            $ gold -= prixuppuit
            $ lvlpuit += 1
            hide screen puit
            jump puit

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixuppuit:
            jump Puit

        "Ne pas améliorer le puit":
            jump Puit
