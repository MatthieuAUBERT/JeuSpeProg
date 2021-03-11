# JeuSpeProg

label d :
    screen village:
        imagemap:
            ground "village.png"
            hotspot (103, 40, 173, 264) action Jump("Caserne")
            hotspot (44, 516, 148, 191) action Jump("Habitation")
            hotspot (856, 150, 114, 154) action Jump("Mine")
            hotspot (958, 4, 55, 93) action Jump("BatimentAdmin")
            hotspot (692, 337, 46, 31) action Jump("TerrainAgri")
            hotspot (1123, 569, 144, 135) action Jump("Puits")
            hotspot (1123, 569, 144, 135) action Jump("retour")

label Caserne:
    jump developpement
label Habitation :
label Mine :
label BatimentAdmin :
label TerrainAgri :
label Puits :