import os

import streamlit as st
from PIL import Image

from fermat_helpers.utils import preprocess, show_sidebar_footer

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

    show_sidebar_footer()

    st.header("Preprocessing du texte")
    st.markdown("Le preprocessing est une etape importante dans le traitement des donnees textuelles."
                " En effet, il permet de nettoyer le texte et de le rendre plus comprehensible pour les modeles de machine learning."
                " Nous allons donc voir les differentes etapes de preprocessing et les justifier.")
    st.markdown("## Etapes de preprocessing utilisées")

    # load image
    image = Image.open(os.path.join(data_path, "assets", "preprocessing_flow.png"))
    st.image(image, caption="Natural language processing pipeline", use_column_width=True)
    st.markdown("---")
    # load image
    st.markdown("> ### Distribution des emojis dans les critiques")
    st.markdown("Nous avons remarqué par ailleurs que les emojis sont très importants dans les critiques de produits."
                " Nous allons donc les garder dans notre preprocessing."
                "Cependant, nous allons les remplacer par leur signification afin de ne pas fausser notre analyse.")
    image = Image.open(os.path.join(data_path, "assets", "emoji_distribution.png"))
    st.image(image, caption="Distribution des emojis dans les critiques", use_column_width=True)
    st.markdown("---")
    st.markdown("## Demonstration")
    # Get the text to preprocess
    text = st.text_area("Saissisez votre texte", placeholder="Saisissez votre texte ici puis cliquez sur entrer")
    # Tokenize and lemmatize the text
    if len(text) > 20:
        if st.button("Preprocess"):
            preprocess(text)
            # add heart emoji
            st.success("PREPROCESSING DONE!" + " " + u"\U0001F499")

    st.markdown("---")
    st.markdown("## Statistiques post preprocessing")
    st.markdown("""Avant de passer à l'étape suivante, nous allons voir les statistiques du texte après preprocessing.
                    Nous allons dans un premier temps regarder la longueur des critiques ainsi que le nombre de mots 
                    qu'elles contiennent.""")

    col1, col2 = st.columns(2)
    with col1:
        col1.header("Longueur des critiques")
        image = Image.open(os.path.join(data_path, "assets", "ditribution_longueur_reviews.png"))
        st.image(image, caption="Distribution de la longueur des critiques", use_column_width=True)
    with col2:
        col2.header("Nombre de mots par critique")
        image = Image.open(os.path.join(data_path, "assets", "ditribution_bn_mots_reviews.png"))
        st.image(image, caption="Distribution du nombre de mots par critique", use_column_width=True)
        # text in a rounded box with a shadow effect and a background color of light blue
        st.markdown("""
        <div style="background-color:#e6f7ff;padding:10px;border-radius:10px;">
        <h3 style="color:#0099ff;">Observations</h3>
        Comme on peut le voir sur les figures la plupart des reviews sont court en nombre de mots comme en 
        nombre de caractères on a donc choisi de ne conserver que des reviews de <b>longueur &lt 250 caractères</b>
        </div>""", unsafe_allow_html=True)
        st.markdown("---")

    st.markdown("### Nuage de mots des critiques")
    image = Image.open(os.path.join(data_path, "assets", "wordcloud.png"))
    st.image(image, caption="Nuage de mots des critiques positives", use_column_width=True)
    st.markdown("""
    <div style="background-color:#e6f7ff;padding:10px;border-radius:10px;">
    <h3 style="color:#0099ff;">Observations</h3>
    On peut voir que les mots les plus fréquents sont par exemples <b>PHONE, WELL, USE, GREAT, NEED</b> ce qui est 
    logique car on parle de téléphone et de leurs fonctionnalités.
    </div>""", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### Distribution n grams")
    image = Image.open(os.path.join(data_path, "assets", "ngram_positive.png"))
    st.image(image, caption="Distribution n grams", use_column_width=True)
    st.markdown("""
    <div style="background-color:#e6f7ff;padding:10px;border-radius:10px;">
    <h3 style="color:#0099ff;">Observations</h3>
    Dans cette figure on peut voir la distribution des n grams pour les critiques positives, on remarque que le trigramme
    <b>A GREAT PHONE</b> est très fréquent ce qui est logique pour une critique positive.
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## Vectorisation")
    st.markdown("""
    Nous allons maintenant vectoriser notre texte afin de pouvoir l'utiliser dans nos modèles de machine learning.
    Nous allons utiliser la vectorisation TF-IDF qui est une méthode de vectorisation qui prend en compte la fréquence
    des mots dans un document ainsi que la fréquence des mots dans l'ensemble des documents.
    """)
    # formule for tfidf
    st.latex(r'''tfidf(t,d,D) = tf(t,d) \times idf(t,D)''')
    st.markdown("Avec :")
    # formule for tf
    st.latex(r'''tf(t,d) = \frac{f_{t,d}}{\sum_{t'\in d}f_{t',d}}''')
    # formule for idf in markdown
    st.markdown(r"""idf(t,D) = log(\frac{|D|}{|\{d \in D : t \in d\}|}})""")

    st.markdown("## Notre fonction de vectorisation")
    st.markdown("""
    ```python
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    # fonction pour vectoriser
    def vectorize(ngrams, train_data, test_data):
        # initialisation du vectorizer
        vectorizer = TfidfVectorizer(ngram_range=ngrams)
        
        # vectorisation des données d'entrainement et de test
        vectorized1 = vectorizer.fit_transform(train_data['Reviews'])
        vectorized2 = vectorizer.transform(test_data["Reviews"])
        
        vector_train = vectorized1.toarray()
        vector_test = vectorized2.toarray()
        
        # affichage de quelques statistiques
        print("Somme 5 premiers vecteurs")
        print("Train: ")
        print(vector_train.sum(axis=0)[:5])
        print("Test: ")
        print(vector_test.sum(axis=0)[:5])
    
        print("Vocabulaire")
        print(vectorizer.get_feature_names_out()[100:150])
        return vector_train, vector_test, vectorizer
    ```
    """, unsafe_allow_html=True)

    # bouton page suivante


if __name__ == '__main__':
    preprocessing_page()
