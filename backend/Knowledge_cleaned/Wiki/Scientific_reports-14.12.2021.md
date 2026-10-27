## Contexte et Problématique

La source originale `Scientific_reports-14.12.2021.pdf` présente un modèle d'apprentissage automatique (ALM) pour stratifier les couples infertiles avec l'infertilité idiopathique. Le but principal de ce travail est de développer une méthode discriminante efficace pour prédire le statut de fertilité des couples.

## Contributions Majeures et Démarche

Le modèle OPLS-DA (Orthogonal Partial Least Square-Discriminant Analysis) est présenté comme une nouvelle approche pour analyser les données liées à l'infertilité. Les contributions majeures incluent :

* La construction d'un modèle discriminant efficace pour prédire le statut de fertilité des couples.
* L'utilisation de variables anthropométriques, métaboliques et antioxidatives comme facteurs influents pour la stratification de l'infertilité idiopathique.

## Fondements Théoriques et Formulations Mathématiques

### Méthode OPLS-DA

$$
\begin{aligner}
R^2 &= \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}, \\
Q^2 &= 1 - R^2.
\fin{aligner}
$$

où $R^2$ est la mesure de la bonne fit, et $Q^2$ est une mesure de la capacité à prédire.

$$
\bar{x} = \frac{\sum_{i=1}^{n}x_i}{n}, \\
\sigma_x^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}.
$$

où $\bar{x}$ est la moyenne, et $\sigma_x^2$ est la variance.

### Variable Importance for the Projection (VIP)

Le modèle OPLS-DA utilise le VIP pour mesurer l'importance des variables dans la projection. Le VIP est calculé comme suit :

$$
w = \frac{\sum_{i} w_i x_i}{\sqrt{\sum_{i} w_i^2}}
$$

où $w$ est le poids du mécanisme d'attention.

## Exemples Concrets, Applications et Limites

### Échantillon de développement

* 73 couples infertiles et 63 couples fertiles recrutés à partir des centres de reproduction de JV, SE et PAU.
* Les résultats obtenus sur l'ensemble de développement sont utilisés pour évaluer la performance du modèle OPLS-DA.

### Ensemble de test

* 24 couples infertiles et 37 couples fertiles recrutés à partir du centre de reproduction CCH.
* Le modèle OPLS-DA est appliqué sur l'ensemble de test pour évaluer sa précision.

### Benchmarks

| Modèle | Précision |
| --- | --- |
| OPLS-DA (hommes) | 59,0% |
| OPLS-DA (femmes) | 57,4% |
| OPLS-DA (couples) | 68,8% |

Note : les valeurs de précision sont indiquées pour chaque modèle.

### Limites et Perspectives

Les auteurs reconnaissent que le modèle OPLS-DA présente certaines limites, notamment la nécessité d'une grande quantité de données pour entraîner le modèle. Cependant, ils suggèrent que les résultats obtenus sur l'ensemble de développement sont prometteurs et ouvrent une nouvelle perspective pour l'étude de l'infertilité idiopathique.