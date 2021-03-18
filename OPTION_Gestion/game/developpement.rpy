
label developpement :

    call screen village



label Caserne:
    show screen caserne

    jump developpement

label Habitation:
    call screen habitation

    jump developpement


label Mine:
    call screen mine

    jump developpement


label BatimentAdmin:
    call screen batimentadmin

    jump developpement


label TerrainAgri:
    call screen terrainagri

    jump developpement


label Puits:
    call screen puits

    jump developpement


   
    #$ lvlcaserne = 1 
   # $ upcaserne[6]={0,100,200,500,1500,2000}
   # texte  Niv: 
    #texte Info:    
   # if (lvlcaserne<6):
    #    texte Upgrade :
    #    if (gold>upcaserne[lvlcaserne]):
    #        bouton avec text + [upcaserne[lvlcaserne]]Gold 
    #        $ gold -= upcaserne[lvlcaserne]
    #        $ lvlcaserne +=1          
   # jump developpement
        
