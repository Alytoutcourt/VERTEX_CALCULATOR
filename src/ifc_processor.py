import ifcopenshell
import ifcopenshell.geom
import multiprocessing

def process_ifc_file(ifc_file_path):
    ifc_file = ifcopenshell.open(ifc_file_path)
    return {ifc_file.schema : "HEY"}
    # settings = ifcopenshell.geom.settings()
    # iterator = ifcopenshell.geom.iterator(settings, ifc_file, multiprocessing.cpu_count())
    # if iterator.initialize():
    #     num_vertex_occurrences = {}
    #     while True:
    #         shape = iterator.get()
    #         if shape is None:
    #             break
    #         product_name = shape.product.Name
    #         num_faces = len(shape.geometry.faces)
    #         num_edges = len(shape.geometry.edges)
    #         num_verts = len(shape.geometry.verts)
    #         num_vertex_occurrences[product_name] = {
    #             "num_faces": num_faces,
    #             "num_edges": num_edges,
    #             "num_verts": num_verts
    #         }
    #         if not iterator.next():
    #             break
    #     return num_vertex_occurrences
