# Texteditor — PyEditor

Éditeur de texte de bureau développé en Python avec Tkinter.

Ce dépôt est un projet d’apprentissage historique plus complet que les micro-exercices présents sur ce compte. Il met en pratique la création d’une interface graphique, la manipulation de fichiers et l’organisation d’un petit programme orienté objet.

## Fonctionnalités présentes

- création d’un nouveau document ;
- ouverture de fichiers ;
- enregistrement et « Enregistrer sous » ;
- prise en charge proposée des fichiers `.txt`, `.py`, `.html`, `.js` et de tous types de fichiers ;
- zone de texte avec scrollbar ;
- menus **Fichier** et **Édition** ;
- copier, couper, coller et sélectionner tout ;
- raccourcis clavier pour les principales actions ;
- mise à jour du titre de la fenêtre selon le fichier ouvert.

## Technologies

- Python ;
- Tkinter ;
- `tkinter.messagebox` ;
- `tkinter.filedialog`.

## Architecture actuelle

L’application est regroupée dans la classe `PyEditor` de `main.py`.

Elle gère :

- la fenêtre principale ;
- la zone de texte ;
- les dialogues de fichiers ;
- les opérations d’édition ;
- les menus ;
- les raccourcis clavier ;
- le chemin du fichier courant via `self.filename`.

Voir [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) pour le détail.

## Exécution

Tkinter est généralement inclus avec les distributions standard de Python disposant du support graphique.

```bash
python main.py
```

L’application ouvre alors une fenêtre graphique intitulée initialement « Nouveau document - Editeur de texte ».

## Limites de la version historique

Le code est conservé comme exercice d’apprentissage et n’est pas présenté comme un éditeur de texte prêt pour la production.

Quelques points sont notamment à améliorer :

- la commande de la scrollbar appelle actuellement `yview()` lors de sa création au lieu de transmettre la méthode elle-même ;
- le programme ne suit pas explicitement l’état « modifié / non modifié » du document ;
- les confirmations avant remplacement ou fermeture reposent sur la présence de contenu plutôt que sur de vraies modifications ;
- certains scénarios d’annulation d’un dialogue peuvent conduire à la suppression du contenu courant ;
- les ouvertures et sauvegardes n’indiquent pas explicitement l’encodage texte ;
- les erreurs sont traitées de manière globale avec `Exception` ;
- aucune fonction d’annulation/rétablissement, recherche, remplacement ou gestion avancée de document n’est implémentée.

Ces points sont documentés sans modifier le comportement historique du code.

## Évolution possible

Une évolution progressive pourrait séparer interface, gestion des documents et services fichiers, ajouter le suivi des modifications, sécuriser les dialogues d’enregistrement et enrichir les fonctions d’édition.

Voir [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Statut

Projet d’apprentissage historique — mini-éditeur de texte Tkinter.

## Consolidation prévue

À conserver comme mini-projet autonome ou candidat à une future collection `learning-python/gui/tkinter-projects/`.
