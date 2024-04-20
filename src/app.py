import os  # Importation du module os pour manipuler les chemins de fichiers
import tempfile  # Importation du module tempfile pour créer un répertoire temporaire
import streamlit as st  # Importation du module streamlit pour créer l'interface utilisateur
from ifc_processor import process_ifc_file  # Importation de la fonction process_ifc_file du module ifc_processor

def main():
    # Titre de l'application
    st.title("IFC Vertex Calculator")
    
    # Uploader pour télécharger un fichier IFC
    uploaded_file = st.file_uploader("Upload an IFC file", type="ifc")
    
    # Vérifie si un fichier a été téléchargé
    if uploaded_file is not None:
        # Crée un bouton pour démarrer le calcul des vertex
        if st.button("Calculate Vertex"):
            # Crée un répertoire temporaire pour stocker le fichier IFC
            temp_dir = tempfile.mkdtemp()
            
            # Obtient le chemin du fichier IFC dans le répertoire temporaire
            path = os.path.join(temp_dir, uploaded_file.name)
            
            # Écrit le contenu du fichier IFC dans le fichier temporaire
            with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            # Appelle la fonction pour traiter le fichier IFC et obtenir les occurrences de vertex
            num_vertex_occurrences = process_ifc_file(path)
            
            # Affiche les résultats dans l'interface utilisateur
            st.write("### Vertex Occurrences:")
            st.write("| Occurrence | Number of Vertex |")
            st.write("| --- | --- |")
            for occurrence, num_vertex in num_vertex_occurrences.items():
                st.write(f"| {occurrence} | {num_vertex} |")

if __name__ == "__main__":
    main()
