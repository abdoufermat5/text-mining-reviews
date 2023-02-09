import os

import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

from fermat_helpers.utils import icon, remote_css, show_sidebar_footer, load_html, load_assets

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def home_page():

    remote_css("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap")
    # material icons
    remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")

    load_assets()
    # load image
    image = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # display image with full width
    st.sidebar.markdown("## Page d'accueil ")
    st.sidebar.markdown("---")
    show_sidebar_footer()
    st.image(image, use_column_width=True)
    st.markdown("## DATA MINING PROJECT")
    st.markdown("### Analyse de sentiments sur les critiques de produits")
    # st.markdown("#### Auteur: [Abdoufermat](https://abdoufermat-5.netlify.app/) | [Moundji]("
    #           "https://abdoufermat-5.netlify.app/) | [Megne Valentine](https://abdoufermat-5.netlify.app/)")
    # st.markdown("#### Année scolaire: 2022-2023")
    st.markdown("#### Description: ")
    st.markdown("""<div style='background-color: black;color:white;padding:1em;border:5px solid green;border-radius:5px'>
                <b>Ce projet a pour but d'analyser le sentiment des critiques de produits sur Amazon. 
                Nous allons utiliser les techniques de preprocessing et de visualisation pour traiter les donnees
                 textuelles. Ensuite, nous allons utiliser les modeles de classification pour prédire le sentiment des
                  critiques de produits.</b>
                  </div>""",
                unsafe_allow_html=True)
    architecture = Image.open(os.path.join(data_path, "assets", "architecture.png"))
    st.image(architecture, use_column_width=True)
    st.markdown("---")
    st.markdown("""<div class="row mt-3">""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <div class="col-11">
                    <div class="card">
                        <img src="https://cdn-icons-png.flaticon.com/512/236/236832.png" alt="Avatar de B" class="card-img-top rounded-circle">
                        <div class="card-body">
                            <h3 class="card-title">Moundji Belhannaci</h3>
                            <p class="card-text">Data Engineer</p>
                        </div>
                    </div>
                </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="col-11">
                    <div class="card">
                        <img src="https://cdn-icons-png.flaticon.com/512/4140/4140048.png" alt="Avatar de C" class="card-img-top rounded-circle">
                        <div class="card-body">
                            <h3 class="card-title">Abdou Yaya Sadiakhou</h3>
                            <p class="card-text">Data Engineer</p>
                        </div>
                    </div>
                </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="col-11">
                <div class="card">
                    <img src="https://cdn-icons-png.flaticon.com/512/4140/4140047.png" alt="Avatar de C" class="card-img-top rounded-circle">
                    <div class="card-body">
                        <h3 class="card-title">Megne Valentine</h3>
                        <p class="card-text">Data Engineer</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    st.set_page_config(
        page_title="Accueil",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    home_page()
