Voici la synthèse du document en figeant rigoureusement les notions clés et les formules LaTeX :

### Vue d'ensemble

L'examen Intra-IFT603/IFT712 d'automne 2025 est un examen intra de la matière IFT603/IFT712. Le document contient les consignes de l'examen, les questions posées et les formules de régression linéaire, de classification binaire et de classificateur de Bayes.

### Formules et Définitions mathématiques (LaTeX exact)

#### Partie I : QCM

1. [3 points] Afin d'appliquer la classification par la règle de Bayes, on peut prédire la classe de x en prenant :
\[ P ( C | x ) = \frac{ P ( x | C ) P ( C ) }{ P ( x ) } \]
2. [3 points] Un algorithme est qualifié de bon algorithme d'apprentissage si :
\[ P ( x | C ) \geq P ( x | C' ) \]
3. [3 points] Le nombre de faux positifs représente les exemples de classe négative dont la classe est prédite comme positive.

#### Partie II : Formulation Probabiliste

1. [10 points] Supposons que X1 et X2 soient des variables aléatoires indépendantes et que Xi ait une distribution de Poisson de moyenne λi (i = 1,2). Posons Y = X1 + X2. Pour une valeur fixe de k (k = 0,1,2,3…), calculons la probabilité conditionnelle :
\[ P ( Y = k | X_1 = x_1, X_2 = x_2 ) = \frac{ P ( Y = k, X_1 = x_1, X_2 = x_2 ) }{ P ( X_1 = x_1, X_2 = x_2 ) } \]
\[ P ( Y = k | X_1 = x_1, X_2 = x_2 ) = \frac{ P ( X_1 = x_1, X_2 = x_2 ) \binom{k}{x_1} \left( \frac{x_1}{\lambda_1} \right)^{x_1} \left( \frac{x_2}{\lambda_2} \right)^{x_2} }{ P ( X_1 = x_1, X_2 = x_2 ) } \]
\[ P ( Y = k | X_1 = x_1, X_2 = x_2 ) = \binom{k}{x_1} \left( \frac{x_1}{\lambda_1} \right)^{x_1} \left( \frac{x_2}{\lambda_2} \right)^{x_2} \]
2. [10 points] Etant donné X une variable aléatoire réelle de densité f, on appelle entropie de X la quantité suivante, si elle existe :
\[ H ( X ) = - \int_{-\infty}^{\infty} f(x) \log f(x) dx \]
3. [10 points] Supposons que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité :
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X ∼ N(m,σ2), dont on rappelle la densité:
\[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(x-m)^2}{2\sigma^2} \right) \]
On suppose que X suit une loi normale, d'espérance m et variance σ2, i.e. X