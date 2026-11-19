import synapseclient
import os

syn = synapseclient.Synapse()
syn.login(authToken=os.getenv("TOKEN_SYNAPSE"))

# Dossier cible où tu veux enregistrer les fichiers
download_dir_train = "train_set"
download_dir_val = "val_set"

# Création du dossier s'il n'existe pas
os.makedirs(download_dir_train, exist_ok=True)
os.makedirs(download_dir_val, exist_ok=True)

# Télécharger le fichier dans ton dossier personnalisé
entity_train = syn.get('syn51514132', downloadLocation=download_dir_train)
entity_val = syn.get('syn51514110', downloadLocation=download_dir_val)

# Path local final
filepath_train = entity_train.path
print("Fichier téléchargé dans :", filepath_train)

filepath_val = entity_val.path
print("Fichier téléchargé dans :", filepath_val)