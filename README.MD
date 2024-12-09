# **Application de Gestion de Tâches**

Une application web de gestion de tâches basée sur une architecture microservices. Ce projet utilise Docker pour l’orchestration des services, MongoDB pour la base de données, et FastAPI pour le backend.

---

## **Table des matières**
- [Introduction](#introduction)
- [Technologies utilisées](#technologies-utilisées)
- [Architecture](#architecture)
- [Installation et Lancement](#installation-et-lancement)
- [Fonctionnalités](#fonctionnalités)
- [Exemples d'Appels API](#exemples-dappels-api)
- [Tests](#tests)
- [Problèmes Courants](#problèmes-courants)
- [Crédits](#crédits)

---

## **Introduction**
Ce projet vise à fournir une application permettant de gérer une liste de tâches avec des fonctionnalités CRUD (Créer, Lire, Mettre à jour, Supprimer). L'application est divisée en plusieurs services déployés à l'aide de Docker.

---

## **Technologies utilisées**
- **Frontend** : HTML, CSS, JavaScript
- **Backend** : FastAPI
- **Base de données** : MongoDB
- **Conteneurisation** : Docker, Docker Compose

---

## **Architecture**
L'application suit une architecture microservices :
- **Frontend** : Sert l'interface utilisateur.
- **Backend** : Fournit une API REST pour interagir avec MongoDB.
- **Base de données** : MongoDB pour le stockage des tâches.

**Diagramme d'architecture** : *(Ajoutez un diagramme si nécessaire.)*

---

## **Installation et Lancement**

### **Prérequis**
- Docker et Docker Compose doivent être installés.

### **Étapes d'installation**
1. Clonez ce dépôt :
    ```bash
    git clone <url-du-repo>
    cd <nom-du-repertoire>
    ```
2. Lancez les conteneurs :
    ```bash
    docker-compose up --build
    ```
3. Accédez aux services :
   - **Frontend** : [http://localhost:8080](http://localhost:8080)
   - **Backend** : [http://localhost:8000/tasks/](http://localhost:8000/tasks/)

---

## **Fonctionnalités**
- **Créer une tâche** : Ajoutez une nouvelle tâche via le frontend ou l'API.
- **Lire les tâches** : Listez toutes les tâches disponibles.
- **Mettre à jour une tâche** : Modifiez une tâche existante.
- **Supprimer une tâche** : Supprimez une tâche de la liste.

---

## **Exemples d'Appels API**
### **Créer une tâche**
- **Endpoint** : `POST /tasks/`
- **Exemple de payload** :
    ```json
    {
        "title": "Nouvelle tâche",
        "description": "Description de la tâche"
    }
    ```
- **Réponse** :
    ```json
    {
        "id": "64c1f68b1d2a64f6c892e8c7",
        "title": "Nouvelle tâche",
        "description": "Description de la tâche"
    }
    ```

### **Lire les tâches**
- **Endpoint** : `GET /tasks/`
- **Réponse** :
    ```json
    [
        {
            "id": "64c1f68b1d2a64f6c892e8c7",
            "title": "Nouvelle tâche",
            "description": "Description de la tâche"
        }
    ]
    ```

### **Supprimer une tâche**
- **Endpoint** : `DELETE /tasks/{id}`

---

## **Tests**
Les tests peuvent être exécutés via l'environnement local ou conteneurisé :
1. Configurez vos variables d'environnement.
2. Exécutez les tests avec :
    ```bash
    pytest
    ```

---

## **Problèmes Courants**
### **Erreur : MongoDB non accessible**
- Vérifiez que le conteneur MongoDB est en cours d'exécution.
- Assurez-vous que les ports exposés dans `docker-compose.yml` sont corrects.

### **Erreur : Duplicate Key**
- Vérifiez que chaque tâche a un identifiant unique.

---

## **Crédits**
- **Développement** : Nicolas SILINOU, Dimitri MIEYO, Brayane MBA ABESSOLO
- **Encadrement** : ESIEA
- **Technologies utilisées** : Docker, FastAPI, MongoDB

---

## **Licence**
Ce projet est sous licence [MIT](LICENSE).

---