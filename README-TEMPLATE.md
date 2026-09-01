# <Titre du livrable — ex. « Provisioning Ansible du serveur web »>

## 1. Objectif
En deux ou trois phrases : ce que fait cette configuration et dans quel but.

## 2. Prérequis
Outils et versions (ex. `ansible >= 2.15`, `kubectl >= 1.28`, `Vagrant + VirtualBox`,
`docker`), et accès nécessaires (cluster, registre…).

## 3. Arborescence
La liste des fichiers livrés, avec une ligne expliquant le rôle de chacun.

## 4. Installation / mise en route
Les étapes EXACTES pour partir de zéro, commandes copiables-collables. Quelqu'un
qui ne connaît pas votre travail doit pouvoir suivre sans vous poser de question.

## 5. Configuration
Les variables à renseigner et où ; la gestion des secrets (jamais en clair —
précisez le mécanisme : ansible-vault, Secret K8s, variable CI protégée,
credentials Jenkins…).

## 6. Vérification
Comment vérifier que tout fonctionne : commandes et résultat attendu
(ex. `curl http://.../health` → `{"status":"ok"}`).

## 7. Choix techniques & limites
Vos décisions et compromis, ce qui n'est pas géré, et les pistes d'amélioration.
