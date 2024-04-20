import os  # Importation du module os pour manipuler les chemins de fichiers
import streamlit as st  # Importation du module streamlit pour créer l'interface utilisateur
from ifc_processor import process_ifc_file  # Importation de la fonction process_ifc_file du module ifc_processor

def main():
    # Titre de l'application
    st.title("IFC Vertex Calculator")
    
    # Champ de saisie de texte pour entrer le chemin du fichier IFC
    ifc_path = st.text_input("Enter the path of the IFC file:")
    
    # Vérifie si un chemin a été saisi
    if ifc_path:
        # Crée un bouton pour démarrer le calcul des vertex
        if st.button("Calculate Vertex"):
            # Vérifie si le fichier IFC existe à l'emplacement spécifié
            if os.path.exists("C:\Users\AliJA\Downloads\RIA-RIA.ifc"):
                # Appelle la fonction pour traiter le fichier IFC et obtenir les occurrences de vertex
                num_vertex_occurrences = process_ifc_file("C:\\Users\\AliJA\\Downloads\\RIA-RIA.ifc")
                
                # Affiche les résultats dans l'interface utilisateur
                st.write("### Vertex Occurrences:")
                st.write("| Occurrence | Number of Vertex |")
                st.write("| --- | --- |")
                for occurrence, num_vertex in num_vertex_occurrences.items():
                    st.write(f"| {occurrence} | {num_vertex} |")
            else:
                st.error("File not found. Please enter a valid path to the IFC file.")

if __name__ == "__main__":
    main()
