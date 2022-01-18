# Finales nationales WorldSkills 2022
 Code de notre robot ayant gagné la fianle nationale des WorldSkills 2022
 
 *catkin_ws* est le workspace ros du projet, il contient un package qui contient le code du robot : *test* (initialement nommé ainsi car on découvrait ros mais on n'a jamais eu le temps de refaire un package propre pour la compétition). Outre le code source, on y a crée 4 messages ros custom pour simplifier les  communications avec la MegaPi. D'autres auraient pu être crée mais on a manqué de temps.
  
 Le dossier *arduino* contient le programme présent sur l'arduino (*programme_arduino*) et le dossier des librairies utilisées.
 On y retrouve la librairie *imu* écrite par nous mais grandement inspirée par la librairie de base Makeblock nommée *MeGyro* et le projet [ruediger](https://github.com/flochre/ruediger) de Florent Chrétien.
 La librairie *OneButton* est une librairie qu'on utilise pour simplifier la detection de l'appui sur le bouton (elle permet une détection simple d'appuis simple, double, long, etc)
