# Theme_4_clustering

**Source originale** : `Theme_4_clustering.pdf` (22830 caractères extraits)

## Synthèse détaillée du contenu

### Section 1
Voici les formules mathématiques en LaTeX ($ ou $$) extraites du passage :

* $$\text{WCSS} = \sum_{i=1}^{n} \sum_{j=1}^{n} |x_i - x_j|$$
* $$\text{Silhouette} = \frac{\text{similarity} - \text{average distance}}{\text{max distance}}$$
* $$\text{ARI} = \frac{\text{ARI}_{\text{within}} - \text{ARI}_{\text{between}}}{\text{ARI}_{\text{between}} + 1}$$
* $$\text{V-mesure} = \frac{\text{ARI}_{\text{within}} - \text{ARI}_{\text{between}}}{\text{ARI}_{\text{between}} + 1}$$
* $$\text{MI} = \frac{\text{ARI}_{\text{within}} - \text{ARI}_{\text{between}}}{\text{ARI}_{\text{between}} + 1}$$

Les autres formules mathématiques ne sont pas explicitement mentionnées dans le passage.

Les théorèmes, définitions et concepts clés extraites du passage sont :

* Théorème de clustering : un ensemble d'objets X est partitionné en sous-ensembles C = { C k | k ∈ { 1 , . . . , K }} tels que ⋃ K k =1 C k = X et ∀ k C k = ∅
* Définition de partition de X : une partition de X est une partition de l'ensemble X en sous-ensembles C = { C k | k = { 1 , . . . , K }} tels que ⋃ K k =1 C k = X et ∀ k C k = ∅
* Définition de partition dure ('hard') : une partition de X est dure si ∀ k , j , k = j , C k ⋂ C j = ∅
* Définition de partition fl oue ('fuzzy') : une partition de X est fl oue si ∃ k , j , k = j , C k ⋂ C j = ∅
* Concept de m´ etrique de performance de clustering : une fonction qui ´ evalue la qualit´ e des clusters
* Types de m´ etriques de performance : internes, externes et relatives
* Indices internes : inertie intra-cluster (WCSS), indice de Silhouette
* Indices externes : ARI, V-mesure, MI
* Indices relatifs : courbe d'Elbow

### Section 2
Voici les formules mathématiques en LaTeX ($ ou $$) extraites du passage :

* $$\Omega: \text{vérifé terrain}, H: \text{entropie}, TP: \text{vrai positif}, TN: \text{vrai négatif}$$
* $$U_{ik} = \begin{cases} 1 & \text{si } x_i \in C_k \\ 0 & \text{sinon} \end{cases}$$
* $$\text{RI} = \frac{TP + TN}{n(n-1)}$$
* $$\text{MI} = \sum_{i=1}^{n} \sum_{j=1}^{n} U_{ij} \log \frac{U_{ij}}{P_{ij}}$$
* $$\text{Silhouette Coefficient} = \frac{b - a}{max(a, b)}$$
* $$\text{Homogénéité, Complément de V-mesure} = \frac{TP + TN}{n(n-1)}$$

Les concepts clés extraits du passage sont :

* Indices internes et externes
* Partitions de l'espace de données
* Clustering par partition
* K-means
* Fuzzy clustering
* Soft clustering
* Clustering incomplet

Les théorèmes et définitions extraites du passage sont :

* Le théorème de la partition de l'espace de données
* La définition de la fonction objective de clustering
* La définition de la mesure de la qualité d'une partition de l'espace de données

### Section 3
Voici les formules mathématiques en LaTeX ($ ou $$) extraites du passage :

1. $$J_m(U, \mu) = \sum_{n=1}^n \sum_{K=1}^K u_{m,i,k} \Vert x_i - \mu_k \Vert^2$$
2. $$\sum_{n=1}^n \sum_{K=1}^K u_{m,i,k} \Vert x_i - \mu_k \Vert^2$$
3. $$\sum_{n=1}^n \sum_{K=1}^K u_{m,i,k} \Vert x_i - \mu_k \Vert^2$$
4. $$\sum_{n=1}^n \sum_{K=1}^K u_{m,i,k} \Vert x_i - \mu_k \Vert^2$$
5. $$\sum_{n=1}^n \sum_{K=1}^K u_{m,i,k} \Vert x_i - \mu_k \Vert^2$$

Les autres formules mathématiques ne sont pas explicitement mentionnées dans le passage.

### Section 4
Voici les formules mathématiques en LaTeX ($ ou $$) extraites du passage :

* $$N_{Eps}(x_i) = \{x_j \in X | dist(x_i, x_j) \leq Eps\}$$
* $$k-dist(x_i) = \{x_j \in X | dist(x_i, x_j) \leq k\}$$

Les théorèmes, définitions et concepts clés extraites du passage sont :

* Théorème : Le clustering vise à regrouper des objets similaires afin de maximiser la cohésion intra-cluster et la séparation inter-cluster.
* Définition : Un point central est un point qui appartient à une région dense, un point de bordure est un point qui appartient au voisinage d'un point central, un bruit est un point qui n'appartient pas à une région dense.
* Concept clé : La densité est une mesure de la proximité entre les points dans un espace.
* Technique de clustering : DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
* Facteurs à considérer :
 + Présence ou non de bruit (outliers)
 + Connaissance préalable du nombre de clusters
 + Forme et densité des regroupements