label developpement :

    call screen village




label Caserne:

    show screen caserne
    
    Caserne "Niveau : [lvlcaserne] {p=0.1}Info : La caserne permet d'augmenter le nombre de troupe crée en debut de chaque journée !"

    menu:
        "Retour au village ":
            hide screen caserne
            jump developpement
        
        "Upgrade" if lvlcaserne<6 :
                jump labupcaserne
            
label labupcaserne:
    $ prixupcaserne = upcaserne[lvlcaserne]
    
    menu :
        Caserne "Amelioration de la caserne !"
        "Ameliorer la caserne pour [prixupcaserne] Gold " if gold>prixupcaserne:
            $ gold -= prixupcaserne
            $ lvlcaserne += 1
            hide screen caserne
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixupcaserne:
            jump Caserne

        "Ne pas ameliorer la caserne ":
            jump Caserne
            




label Habitation:

    show screen habitation
    
    Habitation "Niveau : [lvlhabitation] {p=0.1}Info : Une habitation permet d'augmenter le nombre de troupe maximal que l'on peut stocker !"

    menu:
        "Retour au village ":
            hide screen habitation
            jump developpement
        
        "Upgrade" if lvlhabitation<6 :
                jump labuphabitation
            

label labuphabitation:
    $ prixuphabitation = uphabitation[lvlhabitation]
    
    menu :
        Habitation "Amelioration de l'habitation !"
        "Ameliorer l'habitation pour [prixuphabitation] Gold " if gold>prixuphabitation:
            $ gold -= prixuphabitation
            $ lvlhabitation += 1
            hide screen habitation
            jump developpement


        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixuphabitation:
            jump Habitation

        "Ne pas ameliorer l'habitation ":
            jump Habitation
            



label Mine:

    show screen mine
    
    Mine "Niveau : [lvlmine] {p=0.1}Info : La mine permet d'augmenter le nombre de d'or reçu en debut de chaque journée !"

    menu:
        "Retour au village ":
            hide screen mine
            jump developpement
        
        "Upgrade" if lvlmine<6 :
                jump labupmine
            

label labupmine:
    $ prixupmine = upmine[lvlmine]
    
    menu :
        Mine "Amelioration de la mine !"
        "Ameliorer la mine pour [prixuphabitation] Gold " if gold>prixupmine:
            $ gold -= prixupmine
            $ lvlmine += 1
            hide screen mine
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixmine:
            jump Mine

        "Ne pas ameliorer la mine ":
            jump Mine



label BatimentAdmin:

    show screen batimentadmin
    
    BatimentAdmin "Niveau : [lvlbatimentadmin] {p=0.1}Info : Le batiment administratif permet d'augmenter les relation avec les ambasadeurs d'autre village !"

    menu:
        "Retour au village ":
            hide screen batimentadmin
            jump developpement
        
        "Upgrade" if lvlbatimentadmin<6 :
                jump labupbatimentadmin
            

label labupbatimentadmin:
    $ prixupmine = upmine[lvlbatimentadmin]
    
    menu :
        BatimentAdmin "Amelioration du batiment administratif !"
        "Ameliorer le batiment administratif pour [prixupbatimentadmin] Gold " if gold>prixupbatimentadmin:
            $ gold -= prixupbatimentadmin
            $ lvlbatimentadmin += 1
            hide screen batimentadmin
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixbatimentadmin:
            jump BatimentAdmin

        "Ne pas ameliorer le batiment administratif ":
            jump BatimentAdmin







label TerrainAgri:

    show screen terrainagri
    
    TerrainAgri "Niveau : [lvlterrainagri] {p=0.1}Info : Le terrain agricole permet d'augmenter les productions de nourritures reçu en debut de chaque journée !"

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
            $ lvlbatimentadmin += 1
            hide screen batimentadmin
            jump developpement

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixupterrainagri:
            jump TerrainAgri

        "Ne pas ameliorer le terrain agricole ":
            jump TerrainAgri



label Puit:
    show screen puit 
    
    Puit "Niveau : [lvlpuit] {p=0.1}Info : Le puit permet d'augmenter les productions d'eaux reçu en debut de chaque journée"

    menu:
        "Retour au village ":
            hide screen puit
            jump developpement
        
        "Upgrade" if lvlpuit<6 :
                jump puit
            

label labuppuit:
    $ prixuppuit = uppuit[lvlpuit]
    
    menu :
        Puit "Amelioration du puit !"
        "Ameliorer le puit pour [prixuppuit] Gold " if gold>prixuppuit:
            $ gold -= prixuppuit
            $ lvlpuit += 1
            hide screen puit
            jump puit

        "Vous n'avez pas encore assez de gold pour l'amélioration" if gold<prixuppuit:
            jump Puit

        "Ne pas ameliorer le puit":
            jump Puit




