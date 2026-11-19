import os
from pathlib import Path
import nibabel as nib
import numpy as np

def generate_dataset_dict(root_directory):
    """
    Parcourt les dossiers et génère une liste de dictionnaires
    selon la structure demandée.
    """
    dataset = []
    
    # Définir le chemin racine
    root = Path(root_directory)
    
    # Vérifier si le dossier existe
    if not root.exists():
        print(f"Erreur : Le dossier {root_directory} n'existe pas.")
        return []

    # Liste des modalités à chercher (les suffixes avant .nii.gz)
    # Note : on map le nom du champ voulu -> au suffixe attendu dans le fichier
    modalities = {
        "seg": "seg",
        "t1c": "t1c",
        "t1n": "t1n",
        "t2f": "t2f",
        "t2w": "t2w"
    }

    # 1. On parcourt chaque dossier patient dans le dossier racine
    for patient_folder in sorted(root.iterdir()):

        if patient_folder.is_dir() and patient_folder.name.startswith('BraTS'):
            print (patient_folder.name)
            
            _, _ ,patient_id, volume_id = patient_folder.name.split('-')
            # Création du dictionnaire pour ce patient
            # On utilise le nom du dossier comme base pour le patient_number
            # (Vous pouvez ajouter un .split('_')[-1] si vous ne voulez que le numéro)
            patient_data = {
                "patient_id": patient_id,
                "volume_id": volume_id
            }
            
            # Récupérer tous les fichiers nii.gz du dossier
            files = list(patient_folder.glob("*.nii.gz"))
            
            # 2. Pour chaque modalité, on cherche le fichier correspondant
            for key, suffix in modalities.items():
                found_path = None
                
                for file_path in files:
                    # On vérifie si le fichier se termine par 'suffix.nii.gz'
                    # Ex: 'Patient01_t1c.nii.gz' termine par 't1c.nii.gz'
                    if file_path.name.endswith(f"{suffix}.nii.gz"):
                        found_path = str(file_path.absolute())
                        break
                
                # On ajoute le chemin (ou None si pas trouvé)
                patient_data[key] = found_path

            dataset.append(patient_data)

    return dataset