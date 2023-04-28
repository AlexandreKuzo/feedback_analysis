# Analyser des feebacks avec OpenAI et NLTK

Ici, nous avons deux fichiers Python qui font les actions suivantes :
- lire des fichiers .csv et des textes avec [Pandas](https://pandas.pydata.org/)
- émettre des scores en fonction du ton du texte, plus le feedback est considéré comme "positif", plus haut est le score 

## Contenu du dossier
- Deux scripts Python : da_vinci.py & nltk_analyse.py
- Le fichier de dépendances requirements.txt.

"da_vinci.py" s'appuie sur [le modèle DaVinci d'OpenAI](https://platform.openai.com/docs/models/gpt-3), qui est le modèle textuel le plus avancé parmi les modèles textuels GPT-3. On passe par l'API d'OpenAI pour générer un score unique entre -1 et 1.

"nltk_analyse.py" s'appuie sur la [Bibliothèque NLTK](https://www.nltk.org/) ; elle permet de réaliser un taitement automatique de données textuelles. On peut s'appuyer sur un corpus de mots pré-classifiés et générer un "polarity_score" ; une agrégation issue d'un calcul qui prend en compte les mots étiquetés, comme négatifs, neutres ou positifs. Ce polarity score donne quatre valeurs numériques pos, neu, neg et compound. Compound agrège l'ensemble des trois autres valeurs. 

Dans le dossier, le fichier faisant office de corpus est ``vader_lexicon.txt``.

### "Packages" et matériel requis

- Pour utiliser les scripts, le nécessaire est dans requirements.txt ; la commande ``pip install -r requirements.txt`` installera l'ensemble (voir ci-dessous).

### Installation et démarrage (consignes adaptées pour utilisateurs/utilisatrices de Mac)

Etape 1: clonez le projet.

Etape 2: naviguez dans le dossier avec la commande ``cd feedback_analysis`` puis installez dans le répertoire un environnement virtuel (avec [pipenv](https://docs.python-guide.org/dev/virtualenvs/), ou avec [venv et pip](https://docs.python.org/fr/3/library/venv.html)).

Etape 3: activez l'environnement virtuel avec la commande appropriée : ``source env/bin/activate`` 

Etape 4 : installez au projet les packages requis ; ceux-ci sont fournis dans le fichier ``requirements.txt`` La commande suivante le fera : ``pip install -r requirements.txt``.

NOTE : les dépendances (NLTK notamment sont très lourdes, attention à votre stockage)

## Lancer les scripts

Il vous suffit de taper les commandes ``python3 nom_du_fichier.py`` pour les éxécuter. Pensez bien à modifier les variables, noms de fichiers csv et dossiers pour adapter à vos besoins.

## Auteur
* **Alexandre Kuzo**  [@alexandrekuzo](https://github.com/AlexandreKuzo)
