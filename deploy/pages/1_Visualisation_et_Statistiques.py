import os

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def visualization_page():
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # config
    st.set_page_config(
        page_title="Visualisation et Statistiques",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.markdown("## Visualisation et Statistiques")
    st.sidebar.markdown("---")
    st.sidebar.markdown("""Dans cette section, vous pouvez voir les différentes visualisations et statistiques sur 
    les données""")
    st.header("Visualisation des donnees")
    # Load the data
    # get the path of the train_data.csv file in data folder which is two levels down from the current file using os
    file_path = os.path.join(data_path, "train_data.csv")
    data = pd.read_csv(file_path)
    tab1, tab3 = st.tabs(["Histogramme", "Distributions"])
    section = "Visualization"
    # Plot the distribution of the sentiment scores
    with tab1:
        st.subheader("Histogramme nombre de mots par critique")
        fig, ax = plt.subplots()
        bins = 25
        ax.hist(data['nombre-mots-reviews'], facecolor='green', alpha=1, bins=bins)
        ax.set_title('Distribution du nombre de mots dans un commentaires/avis')
        ax.set_xlabel('Nombre de mots')
        ax.set_ylabel('Nombre de reviews')
        ax.set_xlim(0, 80)
        ax.grid(True)
        st.pyplot(fig)

        st.subheader("Histogramme longueur critique")
        fig, ax = plt.subplots()
        bins = 50
        ax.hist(data['longueur-reviews'], facecolor='green', alpha=1, bins=bins)
        ax.set_title('Distribution de la longueur des commentaires/avis')
        ax.set_xlabel('Longueur des reviews')
        ax.set_ylabel('Nombre de reviews')
        ax.set_xlim(0, 300)
        ax.grid(True)
        st.pyplot(fig)

    with tab3:
        st.subheader("Statistiques")
        st.write(data.describe())


if __name__ == "__main__":
    visualization_page()