#Envoi de troupes :
label PreparationAttaque:
    hide screen Map
    hide screen Relations
    hide screen City
    hide screen Money
    hide screen Attaque
    "Vous allez attaquer ! Préparez vos troupes !"

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


label PretAttaque:
    $ puissance = nbrSoldats * 10
    jump TerritoireAtta

#Fonction Choix du territoire à attaquer (via Carte)
label TerritoireAtta :
    hide screen PlusButton
    hide screen MinusButton
    hide screen validation
    call screen CarteMondeAtt

label Eternia:
    $ paysAtt = "Eternia"
    menu :
        "Je veux attaquer [paysAtt!q] !" if EterniaConquis == False :
            $ puissanceDef = 900
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q]." :
            jump TerritoireAtta

label Eisenberg:
    $ paysAtt = "Eisenberg"
    menu :
        "Je veux attaquer [paysAtt!q] !" if EisenbergConquis == False:
            $ puissanceDef = 900
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q].":
            jump TerritoireAtta


label Caldisla:
    $ paysAtt = "Caldisla"
    menu :
        "Je veux attaquer [paysAtt!q] !" if CaldislaConquis == False:
            $ puissanceDef = 600
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q].":
            jump TerritoireAtta

label GrandNavire:
    $ paysAtt = "GrandNavire"
    menu :
        "Je veux attaquer [paysAtt!q] !" if GrandNavireConquis == False:
            $ puissanceDef = 300
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q].":
            jump TerritoireAtta

label Florem:
    $ paysAtt = "Florem"
    menu :
        "Je veux attaquer [paysAtt!q] !" if FloremConquis == False:
            $ puissanceDef = 1200
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q].":
            jump TerritoireAtta

label Ancheim:
    $ paysAtt = "Ancheim"
    menu :
        "Je veux attaquer [paysAtt!q] !" if AncheimConquis == False:
            $ puissanceDef = 15000
            jump Attaque
        "Je ne veux pas attaquer [paysAtt!q].":
            jump TerritoireAtta

#Fonction d'attaque (comparaison des deux forces et victoire du plus fort)
label Attaque:
    if puissance < puissanceDef :
        "Votre armée a échoué !"
        "Vous revenez les mains vides, cette défaite vous coûte cher."
        $ maxSoldats -= nbrSoldats
        $ gold -= 400
        if (gold <= 0):
            jump endB

        elif territoireConquis == 6:
            jump endA
        else :
            $ jour += 1
            jump Interface2

    else :
        "Votre armée a réussi !"
        "Vous revenez plein d'or et souverain d'un nouveau territoire !"
        $ maxSoldats -= (nbrSoldats/4)
        $ jour += 1
        $ gold += 500
        $ territoireConquis += 1
        if paysAtt == "Eternia":
            $ EterniaConquis = True
        if paysAtt == "Eisenberg":
            $ EisenbergConquis = True
        if paysAtt == "Caldisla":
            $ CaldislaConquis = True
        if paysAtt == "GrandNavire":
            $ GrandNavireConquis = True
        if paysAtt == "Florem":
            $ FloremConquis = True
        if paysAtt == "Ancheim":
            $ AncheimConquis = True
        jump Interface2

#Si présence d'un allié, attaque commune "FACUL."
