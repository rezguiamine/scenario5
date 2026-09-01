# Consignes de rendu

- Le test contient six scénarios : Ansible, Kubernetes, Jenkinsfile, Vagrantfile, 
  GitLab CI et Observabilité.
- Traitez les scénarios dans l'ordre que vous voulez, selon le temps disponible.
- Rendez chaque scénario dans son propre dossier, avec son `README.md` à la
  racine du dossier (suivez `README-TEMPLATE.md`).
- Exemple d'arborescence de rendu :

  rendu/
    ansible/        ( + README.md )
    kubernetes/     ( + README.md )
    jenkins/        ( + README.md )
    vagrant/        ( + README.md )
    gitlab-ci/      ( + README.md )
    observabilite/  ( + README.md )

- Trois exigences pour tout livrable : ça doit fonctionner, être reproductible,
  et être documenté. Aucun secret en clair.
- Une application d'exemple est fournie dans `app/` (API Python, port 8080,
  endpoint `/health`).
- Pour le scénario Observabilité, considérez que l'application expose ses
  métriques Prometheus sur `/metrics` (port 8080).
