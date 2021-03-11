#Envoi de troupes :
label PréparationAttaque:
    "Vous allez attaquer ! Préparez vos troupes !"
#Fonction Regroupement : Création d'une armée d'attaque (via un bouton d'ajout et d'enlèvement de "soldats")

label Regroupement:
    $ nbrSoldats = 100
    show screen PlusButton
    show screen MinusButton
    show screen validation
    call screen NombreSoldats


label AjoutSoldat:
    python :
        maxSoldats = 550
        if nbrSoldats < maxSoldats :
            nbrSoldats += 10

"buttonminus" pressé =>
    Tant que AjoutSoldat != 0 :
        AjoutSoldat -= 10

if AjoutSoldat == 0 || AjoutSoldat == maxSoldats :
    display : "Vous ne pouvez pas faire ça."

"AjoutSoldat donne alors une certaine puissance"
#Fonction Choix du territoire à attaquer (via Carte)

display : Carte du monde

"Création des différents territoires"/"Chaque territoire aura un 'bouton' approprié. "
"PaysAppuyé" => PaysAttaqué

#Fonction d'attaque (comparaison des deux forces et victoire du plus fort)
if Puissance < Defense :
    "Afficher un échec de l'attaque"

else :
    "Afficher une victoire de l'attaque (On donne ici l'avantage à l'attaquant)"

#Si présence d'un allié, attaque commune "FACUL."
