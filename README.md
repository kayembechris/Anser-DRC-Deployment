# SIG DevOps IA Deployment

Ce projet DevOps public automatise le déploiement d'une application SIG complète (front-end React, back-end Flask) sur un VPS Linux Ubuntu via Ansible, et génère automatiquement un changelog intelligent à chaque merge sur `main` en utilisant un modèle IA 

## Fonctionnalités

- Déploiement automatique frontend/backend via GitHub Actions + Ansible
- Déploiement sur un VPS Ubuntu 
- Publication mobile (via Fastlane - optionnel)
- Documentation claire pour mise en place

## Technologies

- GitHub Actions
- Ansible
- Nginx, Gunicorn
- Flutter, React, Flask (repos privés)

## Structure

- `ansible/` : tous les playbooks
- `.github/workflows/` : pipelines CI/CD
- `docs/` : architecture, variables, clés, etc.

## Déploiement

Déclenché automatiquement depuis les repos privés via GitHub Actions ou webhooks.
