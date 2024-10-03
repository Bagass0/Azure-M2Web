# Cloud funtion

### 1. Créer un groupe de ressources
* Dans le portail, clique sur le menu **"Groupes de ressources"** sur la gauche.
Clique sur **"Créer"**.

* Donne un nom à ton groupe de ressources et choisis une région (France Central).

### 2. Créer une Function App

* Dans le Portail Azure, utilise la barre de recherche pour rechercher **"Function App"** ou accède à **"Function App"** via le marketplace.

* Clique sur **"Créer"** pour lancer l'assistant de création, Remplis les informations requises :

* **Plan de consommation :** Sélectionne Plan de consommation (Consumption ou serverless). Ce plan te permet de payer uniquement pour l'exécution de tes fonctions.

* **Groupe de ressources :** Sélectionne celui que tu viens de créer (par exemple, myResourceGroup).

* **Nom de l'application :** Donne un nom unique à ton application de fonction (par exemple, myFunctionApp).

* **Runtime stack :** Choisis Python et la version de Python souhaitée (par exemple, Python 3.9).

* **Région :** Choisis la région où tu veux déployer l'application.

* **Système de stockage :** Un compte de stockage est requis pour sauvegarder les logs et d'autres données. Si tu n'en as pas, tu peux en créer un automatiquement ici.

* Clique sur **Créer** pour déployer la Function App.

### 3. Créer une nouvelle fonction HTTP-triggered

* Va à **Function App** dans le portail et sélectionne ton application (par exemple, myFunctionApp).

* Dans le panneau de gauche, clique sur **Fonctions** puis sur + Ajouter.