# PROJET: JEU PYXEL
<b><i>Etat actuel du projet:</i></b>
<ul><li>Joueur (oiseau) qui saute a travers des tuyaux avec la barre ESPACE</li>
<li>La taille des tuyaux varient a chaque rotation</li>
<li>Un score s'affiche durant la partie qui se met a jour a chaque franchissement de tuyau</li>
<li>Un menu s'affiche lors du démarrage pour afficher le dernier score et le meilleur score</li>
<li>L'oiseau meurt lorsqu'il touche un tuyau ou touche la bordure de l'écran</li>
<li>Après une mort, le joueur retourne au menu de démarrage où le dernier score et le meilleur score se mettent à jour</li></ul>
<b><i>Difficultés:</i></b>
<ul>
  <li><s>Pas de mort pour le tuyau du bas</s> <a href="#tuyau_du_bas">(réparé le 07/05)</a></li>
<li>Score qui se met mal a jour a partir de 10</li>
<li><s>Tuyau n'est pas collé à la bordure</s> (réparé le 06/05)</li>
<li>Tuyau n'arrive pas à la fin de la fenêtre</li>
<li>L'oiseau passe à travers une partie du tuyau</li>
</ul>
<b><i>Comment nous avons réparés les bugs:</i></b>
<ul><li id="tuyau_du_bas"><i><u>"Pas de mort pour le tuyau du bas"</u></i></li>
  <p>Pour résoudre ce problème, nous avons créer un dictionnaire avec les coordonnées de chaques tuyaux, puis en utilisant une boucle nous avons créer des collisions pour chaques tuyaux dans le dictionnaire.</p>
</ul>
# ACTUALITES DU PROJET:
<b>07/05:</b>
<ul><li>Modification du système de collision pour les tuyaux (+ explication dans le code)</li>
<li>Modification du nom de certaines variables qui n'étaient pas claires</li>
<li>Ajout d'un système de HIGH SCORE</li>
</ul>
<b>23/04:</b>
<ul>
<li>Addition d'un menu principal</li>
<li>Changement du fonctionnement du code (répartition des fonctions parmis différents scripts)</li>
</ul>
<b>14/04:</b>
<ul><li>Continuité de la fonction mort (meurt lorsqu'on est hors écran + meurt lorsqu'on touche un tuyau)</li>
</ul>
<b>07/04:</b>
<ul><li>Modification total du code</li>
<li>Début de la fonction de mort</li>
</ul>
<b>22/03:</b>
<ul><li>Amélioration du système d'accélération</li>
<li>Integration d'images personalisées dans le jeu (oiseau, tuyaux)</li>
</ul>
<b>15/03:</b>
<ul><li>Démarrage du projet</li>
<li>Création d'un joueur qui peut sauter + fond qui avance</li>
</ul>
