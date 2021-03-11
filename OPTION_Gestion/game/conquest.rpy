#Envoi de troupes :
label PréparationAttaque:
    "Vous allez attaquer ! Préparez vos troupes !"

#Fonction Regroupement : Création d'une armée d'attaque (via un bouton d'ajout et d'enlèvement de "soldats")
label Regroupement:
    $ nbrSoldats = 100
    $ maxSoldats = 550
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

label DeleteSoldat:
    python :
        if nbrSoldats > 0 :
            nbrSoldats -= 10
        else :
            "Vous ne pouvez pas enlever plus de soldats !"


label PrêtAttaque:
    $ puissance = nbrSoldats * 10
    jump TerritoireAtta

#Fonction Choix du territoire à attaquer (via Carte)
label TerritoireAtta :
    call screen CarteMondeAtt

label Pays1:
    $ paysAtt = "Pays1"
    menu :
        "Je veux attaquer [paysAtt!q] !":
            $ puissanceDef = 900
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
