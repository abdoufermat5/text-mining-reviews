import pickle

import joblib
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import spacy
from PIL import Image
from matplotlib import pyplot as plt

from utils import load_css, remote_css, icon
from descriptions import naive_bayes_description, svm_description
from predict import predict_sentiment

import re

# load image
image = Image.open("../data/assets/social-data-mining.webp")
st.set_page_config(page_title="Data Mining", page_icon=image, layout="wide")


def style_button_row(clicked_button_ix, n_buttons):
    def get_button_indices(button_ix):
        return {
            'nth_child': button_ix,
            'nth_last_child': n_buttons - button_ix + 1
        }

    clicked_style = """
    div[data-testid*="stHorizontalBlock"] > div:nth-child(%(nth_child)s):nth-last-child(%(nth_last_child)s) button {
        border-color: rgb(255, 75, 75);
        color: rgb(255, 75, 75);
        box-shadow: rgba(255, 75, 75, 0.5) 0px 0px 0px 0.2rem;
        outline: currentcolor none medium;
    }
    """
    unclicked_style = """
    div[data-testid*="stHorizontalBlock"] > div:nth-child(%(nth_child)s):nth-last-child(%(nth_last_child)s) button {
        pointer-events: none;
        cursor: not-allowed;
        opacity: 0.65;
        filter: alpha(opacity=65);
        -webkit-box-shadow: none;
        box-shadow: none;
    }
    """
    style = ""
    for ix in range(n_buttons):
        ix += 1
        if ix == clicked_button_ix:
            style += clicked_style % get_button_indices(ix)
        else:
            style += unclicked_style % get_button_indices(ix)
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# Home page
def home_page():
    # load image
    image = Image.open("../data/assets/social-data-mining.webp")
    # display image with full width
    icon("home", st)
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
                "utiliser les modeles de classification pour predire le sentiment des critiques de produits.</b></div>",
                unsafe_allow_html=True)


stopwords = ['yourself', 'yourselves', 'herself', 'themselves',
             'himself', 'ourselves',
             'myself', 'between', 'whom', 'is', "she", 'here', 'your', 'each', 'we', 'he',
             'my', 'you', 'are', 'them', 'other', 'and', 'an', 'their', 'can', 'she', 'these',
             'ours', 'while', 'have', 'when', 'were', 'who', 'they', 'has', 'before', 'yours',
             "it", 'on', 'now', 'her', 'an', 'from', "would", 'how', 'the', 'or', 'doing',
             'his', 'was', 'through', 'own', 'theirs', 'me', 'him', 'be', 'same', 'it', 'its',
             'which', 'there', 'our', 'this', 'hers', 'being', 'did', 'those', 'i', 'does', 'will',
             'shall', 's', 't', 'n', 'd', 'e', 'u', 'x', 'am', 'get', 've']

# Load the English model
nlp = spacy.load("en_core_web_sm")


def preprocess(text):
    # streamlit spinner
    with st.spinner('Conversion en minuscule...'):
        # Convert to lowercase
        text = text.lower()

        st.write("#### Convertir en minuscule")
        st.write("Sortie: {}".format(text))

    st.markdown("---")

    with st.spinner('Suppression des caractères spéciaux...'):
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        st.write("#### Suppression des caractères spéciaux")
        st.write("Sortie: {}".format(text))

    st.markdown("---")

    with st.spinner("Tokenisation du texte..."):
        # Tokenize the text
        doc = nlp(text)

        st.markdown("#### Tokenization")
        st.write([token.text for token in doc])

    st.markdown("---")

    with st.spinner("Suppression des stopwords et lemmatisation..."):
        # Remove stopwords and lemmatize
        tokens = [token.lemma_ for token in doc if token.text not in stopwords]

        st.markdown("#### Suppression des stopwords et lemmatisation")
        st.write(tokens)

    return f"tokens:  {tokens}"


SENTIMENT = {1: "très mauvais", 2: "mauvais", 3: "neutre", 4: "bon", 5: "très bon"}


def description_section(section, chosen_model=None):
    if section == "Preprocessing":
        st.markdown("Le preprocessing est une etape importante dans le traitement des donnees textuelles. ")
        st.markdown("![preprocessing-image](https://miro.medium.com/max/580/1*VzhvZVKGVGynlsU0AZZQww.jpeg)")
    elif section == "Visualization":
        st.markdown("La visualisation des donnees est une etape importante dans le traitement des donnees textuelles. ")
        st.markdown("![visualization-image](https://miro.medium.com/max/580/1*VzhvZVKGVGynlsU0AZZQww.jpeg)")
    elif section == "Modele":
        st.markdown(
            "> <div style='background-color: black;color:white;padding:1em;border:5px solid green;border-radius:5px'><b>Dans cette etape nous allons "
            "predire le sentiment d'une critique sur les telephones "
            "portables. A partir de la description du produit, nous allons predire le sentiment de la "
            "critique.</b></div>",
            unsafe_allow_html=True)
        # description du modele choisi
        if chosen_model == "Naive Bayes":
            naive_bayes_description(st)
        elif chosen_model == "Random Forest":
            svm_description(st)
    elif section == "Explore notebooks":
        # choisir le notebook a ouvrir
        notebook = st.selectbox("Choisir le notebook", ["Pretraitement",
                                                        "Statistiques sur les autres variables",
                                                        "Modele tuning"])
        if notebook == "Pretraitement":
            # load html file
            with open("../data/assets/preprocessing.html", "r", encoding='utf-8') as f:
                html = f.read()
            # display html file
            components.html(html, height=500, width=1000, scrolling=True)
        elif notebook == "Statistiques sur les autres variables":
            # load html file
            with open("../data/assets/stats_on_other_features.html", "r", encoding='utf-8') as f:
                html = f.read()
            # display html file
            components.html(html, height=500, width=1000, scrolling=True)
        elif notebook == "Modele tuning":
            # load html file
            with open("../data/assets/model.html", "r", encoding='utf-8') as f:
                html = f.read()
            # display html file
            components.html(html, height=500, width=1000, scrolling=True)


# Create the main function
def main():
    load_css("style.css", st)
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons', st)

    st.sidebar.title("Menu")
    st.sidebar.markdown("---")

    if st.sidebar.button("Accueil",
                         key="home",
                         help="Retourner à l'accueil",
                         type="primary",
                         kwargs={
                             'clicked_button_ix': 1,
                             'n_buttons': 5
                         }
                         ):
        home_page()
    # Preprocessing section
    if st.sidebar.button("Preprocessing",
                         on_click=style_button_row,
                         key="preprocessing",
                         type="primary",
                         kwargs={
                             'clicked_button_ix': 2,
                             'n_buttons': 5
                         }):
        st.header("Preprocessing du texte")
        st.markdown("Le preprocessing est une etape importante dans le traitement des donnees textuelles. ")

        # load image
        image = Image.open("../data/assets/Natural_language_processing_pipeline_e3608ff95c.webp")
        st.image(image, caption="Natural language processing pipeline", use_column_width=True)

        # Get the text to preprocess
        text = st.text_area("Saissisez votre texte", "Saisissez votre texte ici")
        # Tokenize and lemmatize the text
        if st.button("Preprocess"):
            preprocessed_text = preprocess(text)
            # add heart emoji
            st.success("PREPROCESSING DONE!" + " " + u"\U0001F499")

    # Visualization section
    if st.sidebar.button("Visualization",
                         on_click=style_button_row,
                         key="visualization",
                         type="primary",
                         kwargs={
                             'clicked_button_ix': 3,
                             'n_buttons': 5
                         }):
        st.header("Visualisation des donnees")
        # Load the data
        data = pd.read_csv("../data/train_data.csv")
        tab1, tab2, tab3 = st.tabs(["Histogramme", "Histogramme2", "Statistiques"])
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
            ax.legend(loc='upper right')
            ax.set_xlim(0, 80)
            ax.grid(True)
            st.pyplot(fig)

        with tab2:
            st.subheader("Histogramme longueur critique")
            fig, ax = plt.subplots()
            bins = 50
            ax.hist(data['longueur-reviews'], facecolor='green', alpha=1, bins=bins)
            ax.set_title('Distribution de la longueur des commentaires/avis')
            ax.set_xlabel('Longueur des reviews')
            ax.set_ylabel('Nombre de reviews')
            ax.legend(loc='upper right')
            ax.set_xlim(0, 300)
            ax.grid(True)
            st.pyplot(fig)
        with tab3:
            st.subheader("Statistiques")
            st.write(data.describe())

    # Modeling section
    if st.sidebar.button("Modele",
                         on_click=style_button_row,
                         key="modele",
                         type="primary",
                         kwargs={
                             'clicked_button_ix': 4,
                             'n_buttons': 5,
                         }):
        st.session_state.more_stuff = False
        st.header("Modele de classification")
        # Get the model to use
        t1, t2 = st.tabs(["Naive Bayes", "Random Forest"])
        # load image
        sentimentJpg = Image.open("../data/assets/sentiment analysis.jpg")

        st.image(sentimentJpg, caption='Sentiment Analysis', use_column_width=True)

        # load the vectorizer with pickle
        vectorizer = pickle.load(open('../data/vectorizers/vectorizer75.pickle', 'rb'))

        with t1:
            model1 = joblib.load('../data/models/nb_model75.sav')
            description_section("Modele", "Naive Bayes")
            text1 = st.text_area("Saissisez le texte a classer", key="text1")
            sbt1 = st.button("Prédire le sentiment", key="sbt1")
            if sbt1:
                sentiment = predict_sentiment(model1, vectorizer, text1)
                # Show the sentiment
                st.write('Le sentiment de la critique est **{}**.'.format(SENTIMENT[sentiment].upper()))
        with t2:
            description_section("Modele", "Random Forest")
            model = joblib.load('../data/models/nb_model75.sav')

            text2 = st.text_input("Saissisez le texte a classer", key="text2")
            # Predict the sentiment
            sbt2 = st.button("Prédire le sentiment", key="sbt2")
            if sbt2:
                sentiment = predict_sentiment(model, vectorizer, text2)
                # Show the sentiment
                st.write('Le sentiment de la critique est **{}**.'.format(SENTIMENT[sentiment].upper()))
        # according to the model selected, predict the sentiment

    if st.sidebar.button("Explore notebooks",
                         on_click=style_button_row,
                         key="notebooks",
                         type="primary",
                         kwargs={
                             'clicked_button_ix': 5,
                             'n_buttons': 5,
                         }):
        section = "Explore notebooks"
        # display the notebook
        description_section("Explore notebooks")


if __name__ == "__main__":
    main()
