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
