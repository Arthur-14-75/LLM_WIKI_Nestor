# Rotating_Neutron_Star_Migrations_as_a_Standardized_Test_for_31_Numerical_Relativity
**Source originale** : `Rotating_Neutron_Star_Migrations_as_a_Standardized_Test_for_31_Numerical_Relativity.pdf`


## Contexte et Problématique
La migration des étoiles à neutrons en rotation est un phénomène complexe qui nécessite une compréhension approfondie pour valider les codes numériques de relativité générale. Les simulations de neutron étoiles instables en rotation sont utilisées comme benchmark pour tester les codes numériques.

## Contributions Clés et Architecture
La simulation des migrations des étoiles à neutrons en rotation est menée avec GRHayL, qui utilise une formulation conservatrice pour les équations d'hydrodynamique. Le code utilise également la variante robuste de la formule Valencia pour les équations d'hydrodynamique.

## Fondements Théoriques et Formules Mathématiques
La forme de la métrique spatiale est donnée par $$\sqrt{-g_{00} g_{11}} dx^0 \otimes dx^1 + \cdots$$.
L'équation d'hydrodynamique pour un fluide parfait est donné par $$(\rho u^\mu)_t = 0, (\rho u^\mu)_{,\nu} - T^{\mu\nu}_{;\nu} = 0.$$
La formulation BSSN de l'équation d'ADM est donnée par $$\frac{1}{2 \sqrt{-g}}(\partial_\tau g_{ij}) + \Gamma^{k}_{i j}\partial_k - \Gamma^k_{ij,k} = 0.$$

## Benchmarks et Résultats Expérimentaux
Les simulations sont effectuées sur des configurations de neutron évoluant dans trois dimensions. La simulation est menée pour isoler l'influence du choc thermoléonique sur les dynamiques de migration et le statut final.

### Problèmes spécifiques ou défauts de base mentionnés
- Le manque d'instabilité n'est pas un problème pour la migration.
- La comparaison entre les évolutions froides et hybrides révèle une dérive thermique systématique du point de terminaison de la migration.

### Algorithmes, architectures ou théorèmes introduits
$$\Delta \rho_c = 0.4 \times 10^{-3}$$
- La formule pour le changement de densité central.
- L'équation pour les fréquences du signal gravitationnel.

### Formulations mathématiques, fonctions de perte ou cibles d'optimisation
$$\frac{d^2 \psi}{dt^2} = \frac{\partial L}{\partial \dot{\psi}}$$
- Fonction de Lagrange pour les simulations numériques.
- Formulation du problème mathématique des étoiles à neutrons.

### Datasets, baselines expérimentaux ou résultats quantitatifs
- Données sur les étoiles à neutrons et leurs migrations observées.
- Résultats de simulations numériques comparés aux observations.
- Limitations des méthodes actuelles pour simuler ces systèmes.