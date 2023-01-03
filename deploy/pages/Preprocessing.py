import os

import streamlit as st
from PIL import Image

from fermat_helpers.utils import preprocess

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def preprocessing_page():
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # config
    st.set_page_config(
        page_title="Preprocessing",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.markdown("## Preprocessing")
    st.sidebar.markdown("---")
    st.sidebar.markdown("""Dans cette section, vous pouvez voir les différentes étapes de preprocessing d'un texte""")
    st.header("Preprocessing du texte")
    st.markdown("Le preprocessing est une etape importante dans le traitement des donnees textuelles. ")

    # load image
    image = Image.open(os.path.join(data_path, "assets", "Natural_language_processing_pipeline_e3608ff95c.webp"))
    st.image(image, caption="Natural language processing pipeline", use_column_width=True)

    # Get the text to preprocess
    text = st.text_area("Saissisez votre texte", "Saisissez votre texte ici")
    # Tokenize and lemmatize the text
    if st.button("Preprocess"):
        preprocess(text)
        # add heart emoji
        st.success("PREPROCESSING DONE!" + " " + u"\U0001F499")


if __name__ == '__main__':
    preprocessing_page()
