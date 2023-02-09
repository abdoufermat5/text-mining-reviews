import os
import pickle
import re
from time import sleep

import spacy
import contractions
import streamlit as st
from PIL import Image
from fermat_helpers.dbConnector import DBConnector
import emoji


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


def convert_emojis_and_emoticons_to_word(text):
    # current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # file path in current directory
    file_path = os.path.join(current_dir, 'Emoticon_Dict.p')
    with open(file_path, 'rb') as fp:
        Emoticon_Dict = pickle.load(fp)
    # remove emoticons
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in Emoticon_Dict) + u')')
    text = emoticon_pattern.sub(r'', text)
    # replace emoji
    text = emoji.demojize(text).replace(",", "").replace(":", "").strip()
    return " ".join(text.split())


def tokenize(text):
    """
    Tokenize the text using regular expressions.
    """
    # tokenize the text using regular expressions
    tokens = re.findall(r"[a-zA-Z0-9]+", text)
    # return the tokens
    return tokens


def preprocess(text):
    with st.spinner('Expansion des contractions'):
        sleep(1)
        text = contractions.fix(text)
        st.markdown("""#### Enlever les contractions """)
        st.markdown("""
        Code:
        ```python
        text = contractions.fix(text)
        ```""")
        st.markdown("> Sortie:")
        st.write(text)

    st.markdown("---")
    # streamlit spinner
    with st.spinner('Conversion en minuscule...'):
        sleep(1)
        # Convert to lowercase
        text = text.lower()

        st.write("#### Convertir en minuscule")
        st.markdown("""
        Code:
        ```python
        text = text.lower()
        ```""")
        st.markdown("> Sortie: ")
        st.write(text)

    st.markdown("---")

    with st.spinner('Conversion des emojis en texte...'):
        sleep(1)
        # Remove emojis
        text = convert_emojis_and_emoticons_to_word(text)
        # Remove punctuation

        st.write("#### Conversion des emojis en texte")
        st.markdown("""
        Code:
        ```python
        def convert_emojis_and_emoticons_to_word(text):
            with open('./Emoticon_Dict.p', 'rb') as fp:
                Emoticon_Dict = pickle.load(fp)
            # remove emoticons
            emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in Emoticon_Dict) + u')')
            text = emoticon_pattern.sub(r'', text)
            # replace emoji
            text = emoji.demojize(text).replace(",", "").replace(":", "").strip()
            return " ".join(text.split())
        ```""")

        st.markdown(f"""> Sortie:""")
        st.write(text)

    st.markdown("---")

    with st.spinner("Tokenisation du texte..."):
        sleep(1)
        # Tokenize the text
        tokens = tokenize(text)

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

        st.markdown(f"""> Sortie: """)
        st.write(tokens)

    st.markdown("---")

    with st.spinner("Suppression des stopwords et lemmatisation..."):
        sleep(1)
        # Load the spacy model
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(" ".join(tokens))
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

        st.markdown(f"""> Sortie:""")
        st.write(tokens)

    return f"tokens:  {tokens}"
