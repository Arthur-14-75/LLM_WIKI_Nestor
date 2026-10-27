# AD_WM_Action_Discriminative_World_Models_for_Counterfactual_Model_Predictive_Control

**Source originale** : `AD_WM_Action_Discriminative_World_Models_for_Counterfactual_Model_Predictive_Control.pdf`

## Contexte et Problématique
La rédaction de ce document a pour but de présenter les principaux résultats d'une étude sur l'apprentissage des modèles mondiaux latents (Latent World Models) pour le contrôle à contrefactuel. Les auteurs ont introduit une nouvelle architecture, appelée AD-WM (Action-Discriminative World Model), qui combine la prédiction de transitions factuelles avec un objectif d'action discriminatif pour améliorer les performances du contrôle à contrefactuel.

## Contributions Clés et Architecture
L'architecture AD-WM est basée sur une combinaison de deux objectifs principaux :
1.  La prédiction de transitions résiduelles, qui est supervisée par l'encodage des successeurs.
2.  L'action discriminative normalisée, qui encourage les transitions à conserver les informations d'action.

L'architecture AD-WM utilise également un objectif de régularisation basé sur la mutualité conditionnelle (MI) pour améliorer la qualité des prédictions.

## Fondements Théoriques et Formules Mathématiques ($$)
La formule mathématique qui décrit l'objectif d'action discriminatif normalisé est :

$$\mathcal{L}_{inv} = - \frac{1}{N}\sum_{i=1}^{N} \left[\log p(z_t | e_t) + \lambda ||e_t||_2^2\right]$$

Où $p(z_t | e_t)$ est la distribution de transition, $\mathcal{L}_{inv}$ est l'objectif d'action discriminatif normalisé et $\lambda$ est un hyperparamètre de régularisation.

## Limites et Perspectives
Les limites de cette étude incluent :
1.  La nécessité de collecter des données de qualité pour entraîner les modèles mondiaux latents.
2.  L'importance de choisir les bons hyperparamètres pour améliorer les performances du modèle.

Cependant, les résultats obtenus avec l'architecture AD-WM sont prometteurs et ouvrent la voie à des applications futures dans le domaine du contrôle à contrefactuel.