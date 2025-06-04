# SIG DevOps Deployment

Ce dépôt contient l'infrastructure DevOps pour un projet SIG fullstack (React + Flask + Flutter).

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
