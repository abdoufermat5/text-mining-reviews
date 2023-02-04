import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import os

from fermat_helpers.utils import show_sidebar_footer

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def explore_notebooks():
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # config
    st.set_page_config(
        page_title="Modeles",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.markdown("""## Exploration des notebooks""")
    st.sidebar.markdown("---")
    st.sidebar.markdown("""Dans cette section, vous pouvez voir les notebooks jupyter qui ont été utilisés durant le 
    projet""")
    show_sidebar_footer()

    st.header("Exploration des notebooks")
    # petite description avec des images de l'objectif de cette page
    st.markdown("""Dans cette section, vous pouvez voir les notebooks jupyter qui ont été utilisés durant le projet""")
    st.markdown("""Les notebooks sont des fichiers qui contiennent du code python et des commentaires. Ils sont très
    utiles pour faire de la data science car ils permettent de documenter le code et de le rendre plus lisible. Ils sont
    aussi très utiles pour faire des présentations car ils permettent de faire des slides avec du code et des commentaires
    """)
    st.markdown("""<div style="text-align: center"><img src="http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1508152648/Jupyter-notebook-Definitive-Guide_ul01sa.png"
    width="800" height="400" /></div>""", unsafe_allow_html=True)
    st.markdown("""---""")

    # get current path
    current_path = os.path.dirname(os.path.abspath(__file__))
    assets = '../../data/assets'

    # liste des chemins des notebooks
    notebooks = [
        os.path.join(current_path, assets, "stats_on_other_features.html"),
        os.path.join(current_path, assets, "preprocessing.html"),
        os.path.join(current_path, assets, "model.html")
    ]

    # button for other features visualization notebook
    with st.expander("Notebook de visualisation des autres features"):
        # Afficher le fichier html
        html(open(notebooks[0], "rb").read(), height=1000, scrolling=True)

    # centered button for preprocessing notebook
    with st.expander("Notebook de preprocessing"):
        # Afficher le fichier html
        html(open(notebooks[1], "rb").read(), height=1000, scrolling=True)

    with st.expander("Notebook de modélisation"):
        # Afficher le fichier html
        html(open(notebooks[2], "rb").read(), height=1000, scrolling=True)


if __name__ == '__main__':
    explore_notebooks()
