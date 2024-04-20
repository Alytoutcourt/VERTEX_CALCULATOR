from tempfile import NamedTemporaryFile
import streamlit as st
from ifc_processor import process_ifc_file

def main():
    st.title("IFC Vertex Calculator")
    
    uploaded_file = st.file_uploader("Upload an IFC file", type="ifc")
    if uploaded_file is not None:
        with NamedTemporaryFile(dir='.', suffix='.ifc') as f:
            f.write(uploaded_file.getbuffer())
            num_vertex_occurrences = process_ifc_file(f.name)
            
            st.write("### Vertex Occurrences:")
            st.write("| Occurrence | Number of Vertex |")
            st.write("| --- | --- |")
            for occurrence, num_vertex in num_vertex_occurrences.items():
                st.write(f"| {occurrence} | {num_vertex} |")

if __name__ == "__main__":
    main()