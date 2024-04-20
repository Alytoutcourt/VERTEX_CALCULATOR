import ifcopenshell  # Importation du module ifcopenshell pour le traitement des fichiers IFC

def process_ifc_file(ifc_file_path):
    """
    Fonction pour traiter un fichier IFC et compter le nombre de vertex par occurrence.
    
    Args:
        ifc_file_path (str): Chemin du fichier IFC à traiter.
    
    Returns:
        dict: Dictionnaire contenant le nombre de vertex par occurrence.
    """
    # Ouvre le fichier IFC et charge son contenu
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    # Initialise un dictionnaire pour stocker le nombre de vertex par occurrence
    num_vertex_occurrences = {}
    
    # Parcourt tous les produits dans le fichier IFC
    for product in ifc_file.by_type("IfcProduct"):
        # Récupère le nombre de vertex du produit
        num_vertex = len(product.Representation.Representations[0].Items[0].Coordinates)
        
        # Stocke le nombre de vertex dans le dictionnaire avec le nom du produit comme clé
        num_vertex_occurrences[product.Name] = num_vertex
    
    # Retourne le dictionnaire contenant le nombre de vertex par occurrence
    return num_vertex_occurrences