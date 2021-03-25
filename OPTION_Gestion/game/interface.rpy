screen Map :
    imagebutton:
        xpos 0.01
        ypos 0.8
        idle "icons/map.png"
        at custom_zoom1
        action Jump("map")

screen WorldMap :
    imagebutton :
        xpos 0
        idle "worldmap.png"
        action Jump("cacher")

label map :
    call screen WorldMap

label cacher :
    hide screen WorldMap
    jump Interface

screen Relations :
    imagebutton:
        xpos 0.8
        ypos 0
        idle "icons/relations.png"
        at custom_zoom1
        action Jump("relations")

screen City :
    imagebutton:
        xpos 0.9
        ypos 0
        idle "icons/city.png"
        at custom_zoom1
        action Jump("developpement")

screen Money :
    text "Argent : [gold!q]":
        xpos 0.01
        ypos 0.01
        size 20

#Soldats à ajouter *
screen PlusButton :
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.90
        ypos 0.4
        idle "icons/plusbutton.png"
        at custom_zoom1
        action Jump("AjoutSoldat")

#Soldats à enlever *
screen MinusButton :
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.90
        ypos 0.6
        at custom_zoom1
        idle "icons/minusbutton.png"
        action Jump("DeleteSoldat")

#Validation de l'armée *
screen validation :
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.95
        ypos 0.9
        idle "icons/validate.png"
        at custom_zoom2
        action Jump("PretAttaque")

#Attaque sur un autre territoire *
screen Attaque :
    imagebutton:
        xpos 0.9
        ypos 0.8
        idle "icons/attaque.png"
        at custom_zoom1
        action Jump("PreparationAttaque")

#Affichage Temps Réel *
screen NombreSoldats:
    frame:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        text "Soldats prêts au combat : [nbrSoldats!q] / Soldats maximum : [maxSoldats!q]":
            size 30

screen CarteMondeAtt:
    imagemap:
        ground "worldmap.png"
        hotspot (89, 195, 281, 136) action Jump("Eternia")
        hotspot (226, 456, 186, 160) action Jump("Eisenberg")
        hotspot (469, 286, 146, 123) action Jump("Caldisla")
        hotspot (508, 533, 156, 96) action Jump("GrandNavire")
        hotspot (810, 305, 164, 163) action Jump("Florem")
        hotspot (835, 559, 156, 132) action Jump("Ancheim")


transform custom_zoom1 :
    zoom 0.5

transform custom_zoom2 :
    zoom 0.8
