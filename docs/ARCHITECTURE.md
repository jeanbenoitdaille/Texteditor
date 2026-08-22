# Architecture de Texteditor

## Vue d’ensemble

`Texteditor` est une application de bureau monofichier utilisant Tkinter. L’ensemble du comportement applicatif est aujourd’hui regroupé dans `main.py`, principalement dans la classe `PyEditor`.

## Point d’entrée

Le bloc `if __name__ == "__main__":` :

1. crée la fenêtre racine `Tk()` ;
2. instancie `PyEditor` ;
3. initialise la fenêtre ;
4. crée la zone de texte ;
5. construit les menus ;
6. démarre la boucle événementielle Tkinter avec `mainloop()`.

## Classe `PyEditor`

### État principal

- `self.master` : fenêtre Tkinter principale ;
- `self.filename` : chemin du fichier courant ou `None` ;
- `self.textaera` : widget `Text` utilisé comme zone d’édition ;
- `self.scroll` : scrollbar verticale.

### Initialisation de l’interface

`create_window()` configure le titre et la taille de la fenêtre.

`create_textaera()` crée la zone de texte, la scrollbar et installe les raccourcis clavier.

### Gestion des documents

`new_document()` propose éventuellement une sauvegarde puis vide la zone de texte et réinitialise le fichier courant.

`open_document()` propose éventuellement une sauvegarde du contenu courant, affiche un dialogue de sélection, lit le fichier choisi puis insère son contenu dans l’éditeur.

`save_as()` ouvre un dialogue « Enregistrer sous », écrit le contenu et mémorise le nouveau chemin.

`save()` écrit directement dans `self.filename` lorsque celui-ci existe, sinon délègue à `save_as()`.

`close_document()` demande éventuellement une sauvegarde avant de quitter l’éditeur.

### Édition

Les méthodes `copy()`, `cut()`, `paste()` et `selectAll()` s’appuient sur les événements virtuels Tkinter :

- `<<Copy>>` ;
- `<<Cut>>` ;
- `<<Paste>>` ;
- `<<SelectAll>>`.

### Menus et raccourcis

`add_menu()` construit les menus **Fichier** et **Édition**.

`raccourcis()` associe plusieurs combinaisons clavier aux méthodes de l’éditeur : nouveau document, ouvrir, sauvegarder, enregistrer sous, copier, couper, coller et tout sélectionner.

### Titre de fenêtre

`set_title_window()` affiche soit le chemin du fichier courant, soit un titre de nouveau document.

## Flux simplifié

```text
Tk()
  ↓
PyEditor
  ├── Fenêtre
  ├── Zone de texte
  ├── Menus
  ├── Raccourcis
  └── Gestion du document courant
         ├── Nouveau
         ├── Ouvrir
         ├── Sauvegarder
         └── Fermer
```

## Limites architecturales historiques

La classe `PyEditor` concentre actuellement interface graphique, logique de document, accès au système de fichiers et gestion de l’état. Cette organisation est acceptable pour un exercice pédagogique, mais elle limite l’évolutivité et la testabilité.

Les principaux points techniques à surveiller sont :

- absence d’un modèle explicite de document ;
- absence d’un indicateur `dirty`/modifié ;
- accès fichiers directement depuis les callbacks UI ;
- gestion très large des exceptions ;
- logique de confirmation répétée entre plusieurs méthodes ;
- forte dépendance des fonctions à des widgets Tkinter concrets.

## Architecture cible possible

Une évolution pédagogique naturelle serait :

```text
texteditor/
├── main.py
├── app.py
├── document.py
├── file_service.py
├── commands.py
└── ui/
    ├── editor_window.py
    └── menus.py
```

`Document` pourrait porter le texte, le chemin et l’état modifié. `FileService` pourrait centraliser lecture/écriture et encodage. L’interface Tkinter resterait responsable de l’affichage et des interactions utilisateur.

Cette architecture cible est une piste d’évolution ; elle n’est pas encore implémentée dans le dépôt historique.
