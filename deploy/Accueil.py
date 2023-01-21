import os

import streamlit as st
from PIL import Image

from fermat_helpers.utils import icon, remote_css, show_sidebar_footer

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def home_page():
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # config
    st.set_page_config(
        page_title="Accueil",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    remote_css("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap")
    # material icons
    remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")
    # load image
    image = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # display image with full width
    icon("home")
    st.sidebar.markdown("## Page d'accueil ")
    st.sidebar.markdown("---")
    show_sidebar_footer()
    st.image(image, use_column_width=True)
    st.markdown("## DATA MINING PROJECT")
    st.markdown("### Analyse de sentiments sur les critiques de produits")
    st.markdown("#### Auteur: [Abdoufermat](https://abdoufermat-5.netlify.app/) | [Moundji]("
                "https://abdoufermat-5.netlify.app/) | [Megne Valentine](https://abdoufermat-5.netlify.app/)")
    st.markdown("#### Année scolaire: 2022-2023")
    st.markdown("#### Description: ")
    st.markdown("> <div style='background-color: black;color:white;padding:1em;border:5px solid "
                "green;border-radius:5px'><b>Ce projet a pour but "
                "d'analyser le sentiment des critiques de produits sur Amazon. Nous allons utiliser les techniques de "
                "preprocessing et de visualisation pour traiter les donnees textuelles. Ensuite, nous allons "
                "utiliser les modeles de classification pour prédire le sentiment des critiques de produits.</b></div>",
                unsafe_allow_html=True)


if __name__ == "__main__":
    home_page()
