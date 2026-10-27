# Définitions & Objets

* **GameHorizon-Annotator**: Un pipeline d'annotation automatique pour les instructions multi-horizons dans le jeu.
 + Formalisation : Le GameHorizon-Annotator est une fonction qui prend en entrée des données de jeu et produit automatiquement une pyramide d'instructions naturelles à trois horizons : opérations courtes, objectifs moyens et stratégies longues.

* **GameHorizon-Data**: Un grand ensemble de données de jeu avec 5 000 heures de recordings collectées par des joueurs experts humains sur 21 titres de jeux.
 + Formalisation : Le GameHorizon-Data est une base de données qui aligne les frames de jeu, les actions du joueur et les instructions à plusieurs horizons.

* **GameHorizon-Bench**: Un ensemble de tests pour évaluer la capacité des modèles à jouer au jeu sur différentes temporalités.
 + Formalisation : Le GameHorizon-Bench est une plateforme qui combine l'évaluation en ligne et offline, avec trois types de tâches principales : action unique, décomposition d'instructions à plusieurs horizons et cohérence croisée.

# Théorèmes & Propositions

* "Les jeux modernes offrent un testeur mesurable pour les modèles AI, combinant des capacités de compréhension visuelle, décomposition d'instructions, planification et contrôle précis des actions sur plusieurs temporalités."
 + Théorie : Les jeux modernes sont une source de données pour tester la capacité des modèles AI à comprendre le jeu et prendre des décisions.

* "Les datasets existants et les benchmarks manquent de flexibilité et de réplicabilité, car ils ne couvrent qu'un étroit éventail de jeux ou sont limités par une annotation coûteuse."
 + Hypothèse : Les datasets existants et les benchmarks ont des limites dans leur capacité à tester la capacité des modèles AI.

# Formules

Aucune formule n'est explicitement mentionnée dans le texte. Cependant, on peut déduire quelques informations :

* La fréquence d'échantillonnage des actions claviers-mécaniques est de 20 Hz.
* La fréquence moyenne des événements claviers est de 2,84 par seconde.

# Méthodologie & Proofs

La construction du GameHorizon-Annotator implique une étape de décomposition des instructions en niveaux plus abstraits, à partir des données de jeu.
 + Construction : La fonction GameHorizon-Annotator prend en entrée les données de jeu et produit automatiquement une pyramide d'instructions naturelles à trois horizons.

# Exemples / Exemples Computationnels

Aucun exemple spécifique n'est mentionné dans le texte.