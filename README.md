

## Présentation

Ce projet utilise le SDK Python de RodiumAi pour interagir avec différents modèles d'intelligence artificielle.

L'application permet de réaliser trois opérations :

* générer une réponse textuelle avec le modèle de chat ;
* générer une image à partir d'une description ;
* générer une vidéo à partir d'une description.

Le projet a été réalisé dans le cadre du Module 03 — Utiliser les API IA avec RodiumAi.

## Technologies utilisées

* Python 3.9+
* SDK RodiumAi `0.3.1`
* python-dotenv

## Structure du projet

```text
mon-projet-python/
│
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
└── main.py
```

## Installation

Cloner le dépôt puis accéder au dossier du projet :

```bash
git clone URL_DU_DEPOT
cd mon-projet-python
```

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement virtuel sous Windows :

```powershell
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` à la racine du projet.

Copier le contenu de `.env.example` :

```text
RODIUMAI_API_KEY=rd_sk_votre_cle
```

Puis remplacer `rd_sk_votre_cle` par sa propre clé API RodiumAi.

La clé API ne doit jamais être publiée sur GitHub.

Le fichier `.env` est exclu du dépôt grâce au fichier `.gitignore`.

## Utilisation

Lancer le programme avec :

```bash
python main.py
```

Le programme propose successivement trois étapes.

### 1. Chat

L'utilisateur saisit une question ou une instruction.

Le programme utilise le modèle :

```text
openai/gpt-4o
```

La réponse générée par le modèle est ensuite affichée dans le terminal.

### 2. Génération d'image

L'utilisateur fournit une description de l'image souhaitée.

Le programme utilise :

```text
openai/gpt-image-1
```

L'image générée est enregistrée localement sous :

```text
image.png
```

### 3. Génération de vidéo

L'utilisateur fournit une description de la vidéo souhaitée.

Le programme utilise :

```text
google/veo-3.1
```

La vidéo générée est enregistrée localement sous :

```text
video.mp4
```

## Navigation dans le programme

Après chaque étape, l'utilisateur peut choisir l'action à effectuer.

Pour le chat :

```text
r = répéter
s = passer à l'étape suivante
```

Pour l'image :

```text
b = revenir à l'étape précédente
r = répéter
s = passer à l'étape suivante
```

Pour la vidéo :

```text
b = revenir à l'étape précédente
r = répéter
q = quitter
```

## Sécurité

La clé API RodiumAi est stockée dans une variable d'environnement et n'est pas directement écrite dans le code source.

Le fichier `.env` est volontairement exclu du dépôt Git grâce au `.gitignore`.

Le fichier `.env.example` permet aux autres utilisateurs de connaître la variable nécessaire sans exposer une clé réelle.

## Auteur

Projet réalisé dans le cadre du Bootcamp IA — Module 03.
