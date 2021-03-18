screen Map :
    imagebutton:
        xalign 0
        idle "icons/map.png"
        action Jump("map")

label map :
    call screen WorldMap

screen WorldMap :
    imagebutton :
        xalign 0
        idle "worldmap.png"
        action Jump("hide")

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

#Soldats à ajouter *
screen PlusButton :
    imagebutton:
        xalign 0
        idle "icons/plusbutton.png"
        action Jump("AjoutSoldat")

#Soldats à enlever *
screen MinusButton :
    imagebutton:
        xalign 0
        idle "icons/minusbutton.png"
        action Jump("DeleteSoldat")

#Validation de l'armée *
screen validation :
    imagebutton:
        xalign 0
        idle "icons/validate.png"
        action Jump("PrêtAttaque")

#Attaque sur un autre territoire *
screen Attaque :
    imagebutton:
        xalign 0
        idle "icons/attaque.png"
        action Jump("PréparationAttaque")

#Affichage Temps Réel *
screen NombreSoldats:
    text "Soldats prêts au combat : [nbrSoldats!q] / Soldats maximum : [maxSoldats!q]":
        xalign 0
        size 20

screen CarteMondeAtt:
    imagemap:
        ground "worldmap.png"
        hotspot (89, 195, 281, 136) action Jump("Eternia")
        hotspot (226, 456, 186, 160) action Jump("Eisenberg")
        hotspot (469, 286, 146, 123) action Jump("Caldisla")
        hotspot (508, 533, 156, 96) action Jump("GrandNavire")
        hotspot (810, 305, 164, 163) action Jump("Florem")
        hotspot (835, 559, 156, 132) action Jump("Ancheim")
