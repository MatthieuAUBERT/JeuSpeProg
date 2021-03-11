screen Map :
    imagebutton:
        xalign 0
        idle "icons/map.png"
        action Jump("map")


screen Relations :
    imagebutton:
        xalign 0
        idle "icons/relations.png"
        action Jump("relations")

screen City :
    imagebutton:
        xalign 0
        idle "icons/city.png"
        action Jump("city")

screen Money :
    text "Argent : [money!q]":
        xalign 0
        size 20

screen PlusButton :
    imagebutton:
        xalign 0
        idle "icons/plusbutton.png"
        action Jump("AjoutSoldat")

screen MinusButton :
    imagebutton:
        xalign 0
        idle "icons/minusbutton.png"
        action Jump("DeleteSoldat")

screen validation :
    imagebutton:
        xalign 0
        idle "icons/validate.png"
        action Jump("PrêtAttaque")

screen Attaque :
    imagebutton:
        xalign 0
        idle "icons/attaque.png"
        action Jump("PréparationAttaque")

screen NombreSoldats:
    text "Soldats prêts au combat : [nbrSoldats!q] / Soldats maximum : [maxSoldats!q]":
        xalign 0
        size 20

screen CarteMondeAtt:
    imagemap:
        ground "worldmap.png"
        hotspot (0,0,0,0) action Jump("Pays1")

        
