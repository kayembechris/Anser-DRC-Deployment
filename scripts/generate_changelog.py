import requests
import subprocess
import os

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# Récupère les derniers commits
commits = subprocess.getoutput("git log --pretty=format:'%s' -n 10")

# Prépare le prompt
prompt = f"""
Voici une liste de commits Git :

{commits}

Génère un changelog lisible et structuré, mettant en évidence les nouvelles fonctionnalités, corrections de bugs et améliorations.
"""

# Appel à l'API Hugging Face
headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

payload = {
    "inputs": prompt,
    "parameters": {"max_new_tokens": 300}
}

response = requests.post(
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
    headers=headers,
    json=payload
)

result = response.json()
changelog = result[0]["generated_text"] if isinstance(result, list) else "Erreur de génération"

# Sauvegarde
with open("CHANGELOG.md", "w") as f:
    f.write(changelog)
