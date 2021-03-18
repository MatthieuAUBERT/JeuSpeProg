screen village:
    frame:
        imagemap:
            ground "village.png"
            at custom_zoom3
            hotspot (133, 137, 69, 81) action Jump("Caserne")
            hotspot (321, 80, 88, 88) action Jump("Habitation")
            hotspot (323, 287, 77, 65) action Jump("Mine")
            hotspot (958, 4, 55, 93) action Jump("BatimentAdmin")
            hotspot (692, 337, 46, 31) action Jump("TerrainAgri")
            hotspot (1123, 569, 144, 135) action Jump("Puit")
            hotspot (1123, 569, 144, 135) action Jump("fin_developpement")

transform custom_zoom3:
    zoom 1.5