
default nbrSoldats = 100
default maxSoldats = 550
default money = 1000

label start:

    scene bg with fade

    "Welcome to this game !"
    "Conquer all territories and you will win !"
    jump Interface

label Interface :
    show screen Map
    show screen Relations
    show screen City
    show screen Money
    call screen Attaque

label end:


    return