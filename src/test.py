import pandas as pd
import streamlit as st
import ifcopenshell
import ifcopenshell.geom
import multiprocessing

from app import colorize






print(ifcopenshell.version)
model = ifcopenshell.open("C:\\Users\\AliJA\\Downloads\\RIA-RIA.ifc")
print(model.schema)

def process_ifc_file(ifc_file_path):
    ifc_file = ifcopenshell.open(ifc_file_path)
    settings = ifcopenshell.geom.settings()
    iterator = ifcopenshell.geom.iterator(settings, ifc_file, multiprocessing.cpu_count())
    if iterator.initialize():
        num_vertex_occurrences = {}
        while True:
            shape = iterator.get()
            if shape is None:
                break
            product_name = shape.__str__
            num_faces = len(shape.geometry.faces)
            num_edges = len(shape.geometry.edges)
            num_verts = len(shape.geometry.verts)
            num_vertex_occurrences[product_name] = {
                "num_faces": num_faces,
                "num_edges": num_edges,
                "num_verts": num_verts
            }
            if not iterator.next():
                break
        return num_vertex_occurrences
    
print(process_ifc_file("C:\\Users\\AliJA\\Downloads\\RIA-RIA.ifc"))
st.title("IFC Vertex Calculator")

uploaded_file = st.file_uploader("Upload le fichier IFC", type="ifc")
#bytes_data = uploaded_file.getvalue()

if uploaded_file is not None:
    with st.spinner('Analyzing file...'):
        # Calcul des occurrences de vertex lorsque le fichier est téléchargé
        num_vertex_occurrences = process_ifc_file("C:\\Users\\AliJA\\Downloads\\RIA-RIA.ifc")

    st.success("File analysis completed!")

    # Affichage des occurrences de vertex dans un DataFrame coloré
    st.write("### Vertex Occurrences:")
    df = pd.DataFrame.from_dict(num_vertex_occurrences, orient='index', columns=['Number of Vertex'])
    st.dataframe(df.style.applymap(colorize))

    # Bouton pour recalculer les vertex si nécessaire
    if st.button('Recalculate Vertex'):
        with st.spinner('Recalculating vertex...'):
            num_vertex_occurrences = process_ifc_file(uploaded_file)
            df = pd.DataFrame.from_dict(num_vertex_occurrences, orient='index', columns=['Number of Vertex'])
            st.write("### Updated Vertex Occurrences:")
            st.dataframe(df.style.applymap(colorize))
        st.success("Vertex recalculated successfully!")