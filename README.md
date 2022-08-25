# helloFlask
Création d'une appli avec Flask

### Installation et utilisation Pyenv:
Installation des dépendances:
 
 $ sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

Installation Pyenv:

 $ curl https://pyenv.run | bash
 
#### (Ne pas oublier les lignes à ajouter et à commenter dans le .Bashrc)

Utilisation Pyenv:
pyenv versions -> liste les environnements créés
pyenv install --list -> liste les versions disponibles à installer
pyenv install [librairie à installée] -> installe la librairie voulue
pyenv activate [environnement] -> passer dans un environnement
pyenv virtualenv [version] [environnement] -> spécifier une version de python pour un environnement
pyenv global [version ou environnement] -> initialise une version python comme version par défaut globale
pyenv local [version ou environnement] -> initialise une version python comme version par défaut locale


### Installation et utilisation de Poetry:

commande installation:

$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

création package:

$ poetry new [project name] -> crée un nouveau projet
$ touch [pack name]/[script_name].py -> crée un fichier avec le script à exécuter
$ poetry add [packet name] -> ajouter un paquet (pandas, flask, ...)

$ poetry install -> installe le package avec poetry
$ poetry build -> crée les fichiers permettant d'exporter le package

$ poetry shell 
$ poetry run [python | count| ...)] -> lance la commande python demandée

