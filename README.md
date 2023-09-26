# Installation et Configuration du projet

Ce guide vous expliquera comment installer le projet, installer les dépendances nécessaires, effectuer les migrations de base de données et lancer le serveur de développement pour commencer à travailler sur le projet.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Python 3.9.2
- Pip (le gestionnaire de paquets Python)

## Configuration d'un environnement virtuel de développement

- Installer virtualenv :
    - Windows :
        ```bash
        pip install virtualenv
        ```
    - Linux :
        ```bash
        python3 -m pip3 install virtualenv
        ```
- Creer et activer un environnement virtuel de développement :
    - Windows :
        ```bash
        virtualenv venv
        ./venv/Scripts/activate
        ```
    - Linux :
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

## Récupérer le code source du projet

- Cloner le projet sur votre ordinateur :
    - Windows :
        ```bash
        git clone https://github.com/Dylan245-droid/djangi-cms-starter.git
        ```
    - Linux :
        ```bash
        git clone https://github.com/Dylan245-droid/djangi-cms-starter.git
        ```

## Installation des dépendances

- Windows :
    ```bash
    cd djangi-cms-starter
    pip install -r requirements.txt
    ```
- Linux :
    ```bash
    cd djangi-cms-starter
    pip3 install -r requirements.txt
    ```

## Migrations

- Windows :
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
- Linux :
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

## Lancement du serveur de développement

- Windows :
    ```bash
    python manage.py runserver
    ```
- Linux :
    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```

## Fin

Félicitations, vous pouvez maintenant commencer à travailler sur le projet. Acceder à votre projet depuis le navigateur de la manière suivante :

    - Windows : 
        http://127.0.0.1:8000
    - Linux :
        http://[votre_adresse_ip]:8000

***Consulter la documentation de Django-CMS : https://docs.django-cms.org/en/latest/ pour vous aider à prendre en main la technologies et ses fonctionnalités.***