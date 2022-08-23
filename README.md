# helloFlask
Création d'une appli avec Flask

###Installation et utilisation Pyenv:
Installation des dépendances:
 
 $ sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

Installation Pyenv:

 $ curl https://pyenv.run | bash
 
####(Ne pas oublier les lignes à ajouter et à commenter dans le .Bashrc)

Utilisation Pyenv:
pyenv versions -> liste les environnements créés
pyenv install --list -> liste les versions disponibles à installer
pyenv install [librairie à installée] -> installe la librairie voulue
pyenv activate [environnement] -> passer dans un environnement
pyenv virtualenv [version] [environnement] -> spécifier une version de python pour un environnement
pyenv global [version] -> initialise une version python comme version par défaut globale
pyenv local [version] -> initialise une version python comme version par défaut locale
