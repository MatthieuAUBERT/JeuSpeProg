screen village:
    frame:
        imagemap:
            ground "village.png"
            hotspot (861, 292, 399, 319) action Jump("Caserne")
            hotspot (396, 344, 424, 262) action Jump("Habitation")
            hotspot (212, 55, 231, 197) action Jump("Mine")
            hotspot (30, 280, 268, 266) action Jump("BatimentAdmin")
            hotspot (413, 209, 378, 134) action Jump("TerrainAgri")
            hotspot (784, 47, 190, 212)action Jump("Puit")

screen caserne:
    imagemap:
        ground "caserne.png"
        xpos 400
        ypos 100
        at custom_zoom3

screen habitation:
    imagemap:
        ground "habitation.png"
        xpos 400
        ypos 200
        at custom_zoom3

screen mine:
    imagemap:
        ground "Mine.png"
        xpos 400
        ypos 200
        at custom_zoom3

screen batimentadmin:
    imagemap:
        ground "batimentadmin.png"
        xpos 400
        ypos 50
        at custom_zoom3

screen terrainagri:
    imagemap:
        ground "terrainagri.png"
        xpos 400
        ypos 200
        at custom_zoom3
        
screen puit:
    imagemap:
        ground "Puit.png"
        xpos 400
        ypos 200
        at custom_zoom3


transform custom_zoom3:
    zoom 1
