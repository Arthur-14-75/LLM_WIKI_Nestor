# Introduction

Le présent document présente une synthèse détaillée de la recherche "Cross_sector_generalization_of_accident_process_role_classification_in_occupational_accident_narratives.pdf". Ce document fournit un aperçu complet des définitions, théorèmes et formules clés du travail.

## Définitions & Objets

* **Unité factuelle** : Un segment de texte continu exprimant une principale facte pertinente à l'incident.
* **Classification des rôles du processus d'accident au niveau de la factuelle unité** : Une approche nécessaire pour extraire des informations structurées à partir des narratives d'incidents.

## Théorèmes & Propositions

1. Les accident-narratives contiennent des informations précieuses sur les situations de travail, les conditions défavorables, les événements d'accident et leurs conséquences.
2. La classification des rôles du processus d'accident au niveau de la factuelle unité est une approche nécessaire pour extraire des informations structurées à partir des narratives d'incidents.

## Formules

1. $$\text{UF} = \left( x, y \right)$$ où $x$ est le segment de texte continu exprimant la factuelle unité et $y$ est l'annotation correspondante du rôle.
2. $$L(y) = \sum_{i=1}^{n} w_i L_i (y_i)$$ où $w_i$ sont les poids des annotations, $L_i$ sont les fonctions de perte pour chaque annotation et $y_i$ est la valeur annotée du rôle.

## Méthodologie & Proofs

La construction de l'EPICEA corpus consiste à diviser les narratives d'accident en segments de texte continu exprimant une principale facte pertinente. Les modèles sont développés exclusivement sur le corpus de construction et évalués directement sur les corpora du métallurgie et de la chimie-plastique, sans adaptation ciblée ou rétro-ingénierie des paramètres.

## Exemples / Experiments

L'EPICEA corpus contient plus de 70 000 unités factuelles extraites de plus de 10 000 narratives d'accident. Les modèles sont évalués sur trois corpora ciblés : le corpus de construction, le corpus du métallurgie et un corpus anonymisé fourni par une entreprise privée.

## Benchmarks

Le tableau présenté dans la section "Exemples" montre les performances des différents classificateurs entraînés sur les TF-IDF representations. Les résultats suggèrent que l'adaptation spécifique à la tâche produit un avantage considérablement plus grand.

## Formulations Mathématiques

1. $$\kappa = \frac{P(OU)}{1 - P(UO)}$$
où $P(OU)$ est la probabilité d'accord et $P(UO)$ est la probabilité de discordance.
2. $$p_{i}(\theta, \phi) = \sum_{r=0}^{3} p_i(r|\theta,\phi)\mathbb{I}_{\{y_i=r\}}$$
où $p_i(r|\theta,\phi)$ est la probabilité que l'unité factuelle $u_i$ appartienne au rôle $r$, et $\mathbb{I}$ est une fonction d'indicateur.

## Limites de l'état de l'art

La recherche présente des limites dans le traitement des narratives d'accident, notamment la nécessité de prendre en compte les conditions défavorables explicitement signalées. Le travail propose une approche innovante pour traiter ces conditions et améliorer la performance du modèle.

## Perspectives et Problèmes ouverts

La recherche présente également des perspectives et problèmes ouverts, tels que l'amélioration de la représentation des événements d'accident et la prise en compte des conséquences reportées.