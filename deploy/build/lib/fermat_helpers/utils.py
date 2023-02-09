import os
import re
from time import sleep

import spacy

import streamlit as st
from PIL import Image
from fermat_helpers.dbConnector import DBConnector


def remove_special_characters_from_brand_name(text):
    """
    Remove special characters from a text.
    """
    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    # remove multiple spaces
    text = re.sub(r"\s+", " ", text)
    # remove leading and trailing spaces
    text = text.strip()
    # return the text
    return text


@st.cache(suppress_st_warning=True)
def get_collection_data(collection):
    db = DBConnector()
    db.change_collection(collection)
    return db.get_all()


@st.cache(suppress_st_warning=True)
def get_data(type='base'):
    db = DBConnector()
    if type == 'train':
        result = db.get_train_data()
    elif type == 'test':
        result = db.get_test_data()
    else:
        result = db.get_base_data()
    return result


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def remote_js(url):
    st.markdown(f'<script src="{url}"></script>', unsafe_allow_html=True)


def load_html(file_name):
    with open(file_name) as f:
        html = f.read()

    return html


def load_assets():
    remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")
    remote_css("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap")
    remote_css("https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,"
               "100..700,0..1,-50..200")
    remote_css("https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0")
    # bootstrap 5
    remote_css("https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css")
    # font awesome
    remote_css("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css")

    # remote javascript
    remote_js("https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js")
    remote_js("https://cdn.jsdelivr.net/npm/@popperjs/core@2.18.0/dist/umd/popper.min.js")
    remote_js("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js")


def show_sidebar_footer():
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")

    st.sidebar.markdown("<br/>" * 6, unsafe_allow_html=True)
    st.sidebar.markdown("""<i>Université Paris-Saclay - Master 2 Data Scale</i>""", unsafe_allow_html=True)
    st.sidebar.markdown("""<b>Module :</b> Data Mining""", unsafe_allow_html=True)
    paris_saclay = Image.open(os.path.join(data_path, "assets", "uvsq.png"))
    st.sidebar.image(paris_saclay, use_column_width=True)


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
        st.markdown("""
        Code:
        ```python
        text = text.lower()
        ```""")
        st.write("Sortie: {}".format(text))

    st.markdown("---")

    with st.spinner('Suppression des caractères spéciaux...'):
        sleep(1)
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        st.write("#### Suppression des caractères spéciaux")
        st.markdown("""
        Code:
        ```python
        text = re.sub(r'[^\w\s]', '', text)
        ```""")

        st.write("Sortie: {}".format(text))

    st.markdown("---")

    with st.spinner("Tokenisation du texte..."):
        sleep(1)
        # Tokenize the text
        doc = nlp(text)

        st.markdown("#### Tokenization")

        st.markdown("""
        Code:
        ```python
        def tokenization(text):
            text = re.sub(r'www', 'https', text)
            text = re.sub(r'http[^\s]+', '', text)
            text = re.sub('@[^\s]+', '', text)
            tokenizer = RegexpTokenizer("[a-zA-Z]+", discard_empty=True)
            text = tokenizer.tokenize(text)
            text = " ".join(text)
            return text.lower()
        ```""")

        st.write([token.text for token in doc])

    st.markdown("---")

    with st.spinner("Suppression des stopwords et lemmatisation..."):
        sleep(1)
        # Remove stopwords and lemmatize
        tokens = [token.lemma_ for token in doc if token.text not in stopwords]

        st.markdown("#### Suppression des stopwords et lemmatisation")

        st.markdown("""
        Code:
        ```python
        # stop words
        def remove_stop_words(text):
            res = []
            for w in text.split():
                if w not in stop_words:
                    res.append(w)
            return " ".join(res)[:-1]
        
        # lemmatization
        def lemmatize_text(text):
            # Tokeniser le texte en mots
            words = word_tokenize(text)
        
            # Initialiser le lemmatiseur
            lemmatizer = WordNetLemmatizer()
        
            # Lemmatiser chaque mot
            lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        
            # Rejoindre les mots lemmatisés en une chaîne de caractères
            lemmatized_text = ' '.join(lemmatized_words)
        
            return lemmatized_text
        ```""")

        st.write(tokens)

    return f"tokens:  {tokens}"
