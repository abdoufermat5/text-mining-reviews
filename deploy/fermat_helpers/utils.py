import re
import spacy

import streamlit as st


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


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
