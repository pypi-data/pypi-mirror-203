"""
-- Papa Séga WADE 14/03/2023 --
"""
import numpy as np
from nomic import atlas

# Exemple de données de texte 

"""
    Remarque: il faut au moins 20 points de données
    pour que la visualisation puisse avoir lieu.
    C'est également possible de faire cet exemple 
    avec la librairie click. 
"""
sentences = [
"Le chat mange une souris",
"Le chien court après une balle",
"Le lion rugit dans la savane",
"La voiture roule sur l'autoroute",
"Le poisson nage dans l'eau",
"L'oiseau vole dans le ciel",
"Le bébé pleure dans son berceau",
"Le vent souffle dans les arbres",
"Le soleil brille dans le ciel",
"La pluie tombe sur la ville",
"Le nuage est blanc et moelleux",
"La neige tombe sur le sol",
"Le bateau flotte sur l'eau",
"Le café est chaud et fort",
"Le thé est doux et parfumé",
"Le lait est frais et crémeux",
"Le gâteau est moelleux et sucré",
"Le pain est frais et croustillant",
"Le fromage est crémeux et salé",
"La salade est fraîche et croquante",
"Le poulet est grillé et juteux",
"Le poisson est cuit à la perfection",
"Les frites sont croustillantes et salées",
"La pizza est chaude et délicieuse",
"Le hamburger est savoureux et consistant",
"Le hot-dog est délicieux et grillé",
"Les réseaux de neurones profonds sont un type de modèle d'apprentissage automatique utilisé en intelligence artificielle.",
"Les mathématiques sont une discipline essentielle pour la compréhension et le développement de l'intelligence artificielle.",
"Le traitement automatique du langage naturel est une branche de l'intelligence artificielle qui vise à permettre aux machines de comprendre le langage humain.",
"Le wolof est la langue la plus parlée au Sénégal, avec environ 40 % de la population sénégalaise qui le parle comme langue maternelle.",
"La traduction automatique est un domaine de l'intelligence artificielle qui peut aider à faciliter la communication entre personnes parlant différentes langues, comme entre le wolof et le français par exemple.",
"Les mathématiques sont également à la base de nombreux algorithmes utilisés en intelligence artificielle, tels que les algorithmes d'apprentissage automatique.",
"L'apprentissage par renforcement est une méthode d'apprentissage automatique dans laquelle une machine apprend à travers des essais et erreurs, en prenant des décisions pour atteindre un objectif donné.",
"L'intelligence artificielle peut être utilisée pour améliorer la qualité de vie des personnes dans différents domaines, tels que la santé, l'agriculture et l'éducation.",
]

# Transformer chaque phrase en un vecteur d'embedding
embeddings = np.zeros((len(sentences), 256))
for i, sentence in enumerate(sentences):
    # Ici, nous utilisons un modèle d'embedding de phrase pré-entrainé
    embeddings[i] = np.random.rand(256)

# Mapper les vecteurs d'embedding sur une carte 2D
project = atlas.map_embeddings(embeddings=embeddings)
