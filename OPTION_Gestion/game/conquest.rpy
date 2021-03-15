#Envoi de troupes :
label PréparationAttaque:
    "Vous allez attaquer ! Préparez vos troupes !"
    $ nbrSoldats = 100
    $ maxSoldats = 550

#Fonction Regroupement : Création d'une armée d'attaque (via un bouton d'ajout et d'enlèvement de "soldats")
label Regroupement:
    show screen PlusButton
    show screen MinusButton
    show screen validation
    call screen NombreSoldats


label AjoutSoldat:
    python :
        if nbrSoldats < maxSoldats :
            nbrSoldats += 10
        else :
            "Vous ne pouvez pas ajouter plus de soldats !"

    jump Regroupement

label DeleteSoldat:
    python :
        if nbrSoldats > 0 :
            nbrSoldats -= 10
        else :
            "Vous ne pouvez pas enlever plus de soldats !"

    jump Regroupement


label PrêtAttaque:
    $ puissance = nbrSoldats * 10
    jump TerritoireAtta

#Fonction Choix du territoire à attaquer (via Carte)
label TerritoireAtta :
    call screen CarteMondeAtt

label Eternia:
    $ paysAtt = "Eternia"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 900
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]."
            jump TerritoireAtta

label Eisenberg:
    $ paysAtt = "Eisenberg"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 900
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]."
            jump TerritoireAtta


label Caldisla:
    $ paysAtt = "Caldisla"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 600
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]."
            jump TerritoireAtta

label GrandNavire:
    $ paysAtt = "GrandNavire"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 300
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]."
            jump TerritoireAtta

label Florem:
    $ paysAtt = "Florem"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 1200
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]."
            jump TerritoireAtta

label Ancheim:
    $ paysAtt = "Ancheim"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 15000
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]."
            jump TerritoireAtta

#Fonction d'attaque (comparaison des deux forces et victoire du plus fort)
label Attaque:
    if puissance < puissanceDef :
        "Votre armée a échoué !"
        "Vous revenez les mains vides, cette défaite vous coûte chère."
        $ maxSoldats -= nbrSoldats

    else :
        "Votre armée a réussi !"
        "Vous revenez plein d'or et souverain d'un nouveau territoire !"
        $ maxSoldats -= (nbrSoldats/4)

#Si présence d'un allié, attaque commune "FACUL."
