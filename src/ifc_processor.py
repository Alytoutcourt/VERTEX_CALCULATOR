import ifcopenshell

def process_ifc_file(ifc_file_path):
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    return {ifc_file.schema : "TEST"}
    # num_vertex_occurrences = {}
    # for product in ifc_file.by_type("IfcProduct"):
    #     num_vertex = len(product.Representation.Representations[0].Items[0].Coordinates)
    #     num_vertex_occurrences[product.Name] = num_vertex
    
    # return num_vertex_occurrences
