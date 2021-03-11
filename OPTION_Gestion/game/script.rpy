$ nombre_alliers_max = 5;
$ nombre_alliers = 0;
$ nombre_territoires_max = 15;
$ nombre_territoires = 1;

label start:

label new_turn:

label diplomatie:

label developpement:

label conquete:

if (nombre_territoires == nombre_territoires_max || nombre_alliers == nombre_alliers_max):
    jump end
else:
    jump new_turn

label end:
