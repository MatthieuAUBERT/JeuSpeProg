screen rel:
    imagebutton:
        xpos 0
        idle "relations.png"
        action Jump("Interface")

label relations :
    call screen rel

screen ville:
    imagebutton:
        xpos 0
        idle "ville.png"
        action Jump("Interface")

label city:
    call screen ville
