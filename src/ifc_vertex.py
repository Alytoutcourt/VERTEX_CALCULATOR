import ifcopenshell

def process_ifc_file(uploaded_filepath):
    ifc_file = ifcopenshell.open(uploaded_filepath)
    
    num_vertex_occurrences = {}
    for product in ifc_file.by_type("IfcProduct"):
        num_vertex = len(product.Representation.Representations[0].Items[0].Coordinates)
        num_vertex_occurrences[product.Name] = num_vertex
    
    return num_vertex_occurrences
