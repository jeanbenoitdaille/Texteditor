# Roadmap de Texteditor

Cette roadmap décrit une évolution possible du mini-éditeur historique sans prétendre que les étapes sont déjà implémentées.

## Phase 1 — Stabiliser le comportement actuel

- corriger la connexion de la scrollbar ;
- distinguer contenu présent et document réellement modifié ;
- empêcher la perte de contenu lors d’une annulation de dialogue ;
- gérer proprement l’annulation de `askopenfilename()` et `asksaveasfilename()` ;
- utiliser un encodage explicite lors des lectures/écritures ;
- remplacer les captures générales `Exception` par des erreurs plus ciblées lorsque pertinent.

## Phase 2 — Fiabiliser la gestion de document

- introduire un état `modified` / `dirty` ;
- mémoriser le chemin courant de façon centralisée ;
- afficher un marqueur de modification dans le titre ;
- mutualiser la logique « proposer de sauvegarder avant de continuer » ;
- gérer correctement Nouveau, Ouvrir et Fermer lorsqu’un document possède des changements non sauvegardés.

## Phase 3 — Enrichir les fonctions d’édition

- Annuler / Rétablir ;
- Rechercher ;
- Remplacer ;
- Aller à une ligne ;
- compteur de lignes et caractères ;
- gestion du presse-papiers plus robuste ;
- éventuels raccourcis supplémentaires.

## Phase 4 — Améliorer l’interface

- barre d’état ;
- meilleure gestion du redimensionnement ;
- titre simplifié avec nom de fichier plutôt que chemin complet ;
- choix de police et taille ;
- thème clair/sombre ;
- menus et libellés harmonisés ;
- meilleure accessibilité clavier.

## Phase 5 — Modulariser le code

Séparer progressivement :

- le modèle de document ;
- les services de lecture/écriture ;
- la fenêtre Tkinter ;
- les menus ;
- les commandes d’édition.

L’objectif serait de rendre la logique plus testable sans dépendre directement de l’interface graphique.

## Phase 6 — Qualité

- tests unitaires sur les composants non graphiques ;
- tests de lecture/écriture avec fichiers temporaires ;
- formatage et linting ;
- documentation d’installation ;
- gestion multiplateforme Windows/macOS/Linux ;
- packaging éventuel en application de bureau.

## Positionnement

`Texteditor` doit rester présenté comme un projet d’apprentissage historique. Une éventuelle version modernisée pourrait devenir un projet distinct ou une évolution explicitement versionnée, plutôt que de réécrire silencieusement le code original.
