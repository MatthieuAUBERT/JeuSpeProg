screen village:
    frame:
        imagemap:
            ground "village.png"
            hotspot (103, 40, 173, 264) action Jump("Caserne")
            hotspot (44, 516, 148, 191) action Jump("Habitation")
            hotspot (856, 150, 114, 154) action Jump("Mine")
            hotspot (958, 4, 55, 93) action Jump("BatimentAdmin")
            hotspot (692, 337, 46, 31) action Jump("TerrainAgri")
            hotspot (1123, 569, 144, 135) action Jump("Puits")
            hotspot (1123, 569, 144, 135) action Jump("fin_developpement")

screen caserne :
    frame:
        xpos 50
        ypos 50
        text "Niveau : [lvlcaserne]" :
            size 40
        text "Info : La caserne permet d'augmenter le nombre de troupe crée en debut de chaque journée !"
        if lvlcaserne<6 :
            text "Upgrade" :
                size 40   
            if gold>upcaserne[lvlcaserne]:
                #bouton
                text "[upcaserne[lvlcaserne]] Gold " :
                    size 40   
                $ gold -= upcaserne[lvlcaserne]
                $ lvlcaserne +=1

screen habitation :
    frame:
        xpos 50
        ypos 50
        text "Niveau : [lvlhabitation]" :
            size 40
        text "Info : Une habittion permet d'augmenter le nombre de troupe maximal que l'on peut stocker !"
        if lvlhabitation<6 :
            text "Upgrade" :
                size 40   
            if gold>uphabitation[lvlhabitation]:
                #bouton
                text "[uphabitation[lvlhabitation]] Gold " :
                    size 40   
                $ gold -= uphabitation[lvlhabitation]
                $ lvlhabitation +=1

screen mine :
    frame:
        xpos 50
        ypos 50
        text "Niveau : [lvlmine]" :
            size 40
        text "Info : La mine permet d'augmenter le nombre de d'or reçu en debut de chaque journée !"
        if lvlmine<6 :
            text "Upgrade" :
                size 40   
            if gold>upmine[lvlmine]:
                #bouton
                text "[upmine[lvlmine]] Gold " :
                    size 40   
                $ gold -= upmine[lvlmine]
                $ lvlmine +=1

screen batimentadmin :
    frame:
        xpos 50
        ypos 50
        text "Niveau : [lvlbatimentadmin]" :
            size 40
        text "Info : Le batiment administratif permet d'augmenter les relation avec les ambasadeur d'autre village !"
        if lvlbatimentadmin<6 :
            text "Upgrade" :
                size 40   
            if gold>upbatimentadmin[lvlbatimentadmin]:
                #bouton
                text "[upbatimentadmin[lvlbatimentadmin]] Gold " :
                    size 40   
                $ gold -= upbatimentadmin[lvlbatimentadmin]
                $ lvlbatimentadmin +=1

screen terrainagri :
    frame:
        xpos 50
        ypos 50
        text "Niveau : [lvlbterrainagri]" :
            size 40
        text "Info : Le terrain agricole permet d'augmenter les productions de nourritures reçu en debut de chaque journée !"
        if lvlterrainagri<6 :
            text "Upgrade" :
                size 40   
            if gold>upterrainagri[lvlterrainagri]:
                #bouton
                text "[upterrainagri[lvlterrainagri]] Gold " :
                    size 40   
                $ gold -= upterrainagri[lvlterrainagri]
                $ lvlterrainagri +=1

screen puits :
    frame:
        xpos 50
        ypos 50
        text "Niveau : [lvlpuits]" :
            size 40
        text "Info : Les puits  permet d'augmenter les productions d'eaux reçu en debut de chaque journée !"
        if lvlpuits<6 :
            text "Upgrade" :
                size 40   
            if gold>uppuits[lvlpuits]:
                #bouton
                text "[uppuits[lvlpuits]] Gold " :
                    size 40   
                $ gold -= uppuits[lvlpuits]
                $ lvlpuits +=1