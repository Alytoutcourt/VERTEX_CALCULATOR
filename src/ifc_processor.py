import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape

def process_ifc_file(ifc_file_path):
    ifc_file = ifcopenshell.open(ifc_file_path)
    settings = ifcopenshell.geom.settings()
    # return {ifc_file.schema : "TEST"}
    num_vertex_occurrences = {}
    for product in ifc_file.by_type("IfcProduct"):
        
        new_shape = ifcopenshell.geom.create_shape(settings, product)
        num_vertex = new_shape.geometry.verts
        num_vertex_occurrences[product.Name] = num_vertex
    
    return num_vertex_occurrences
