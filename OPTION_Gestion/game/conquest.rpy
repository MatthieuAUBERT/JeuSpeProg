#Envoi de troupes :

#Fonction Regroupement : Création d'une armée d'attaque (via un bouton d'ajout et d'enlèvement de "soldats")

"buttonplus" pressé =>
    Tant que AjoutSoldat != maxSoldats :
        AjoutSoldat += 1

"buttonminus" pressé =>
    Tant que AjoutSoldat != 0 :
        AjoutSoldat -= 1

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
