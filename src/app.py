import streamlit as st
from ifc_processor import process_ifc_file

def main():
    st.title("IFC Vertex Calculator")
    
    uploaded_file = st.file_uploader("Upload le fichier IFC", type="ifc")
    
    if uploaded_file is not None:
        with st.spinner('Analyzing file...'):
            # Calcul des occurrences de vertex lorsque le fichier est téléchargé
            num_vertex_occurrences = process_ifc_file(uploaded_file)

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

def colorize(val):
    """
    Fonction pour colorer les cellules du DataFrame en fonction de la valeur.
    """
    if val >= 100:  # Changer la valeur selon vos besoins
        color = 'green'
    elif val >= 50:  # Changer la valeur selon vos besoins
        color = 'orange'
    else:
        color = 'red'
    return 'color: %s' % color

if __name__ == "__main__":
    main()
