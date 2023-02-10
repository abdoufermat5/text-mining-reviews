import os
import pickle

import joblib
import streamlit as st
from PIL import Image

from fermat_helpers.descriptions import description_section
from fermat_helpers.predict import predict_sentiment
from fermat_helpers.utils import show_sidebar_footer

SENTIMENT = {1: "très mauvais", 2: "mauvais", 3: "neutre", 4: "bon", 5: "très bon"}
SENTIMENT_WITH_EMOJI = {1: "TRÈS NÉGATIVE" + " " + u"\U0001F62D",
                        2: "NÉGATIVE" + " " + u"\U0001F622",
                        3: "NEUTRE" + " " + u"\U0001F610",
                        4: "POSITIVE" + " " + u"\U0001F60A",
                        5: "TRÈS POSITIVE" + " " + u"\U0001F60D"}

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")


def modeling_page():
    dmImage = Image.open(os.path.join(data_path, "assets", "social-data-mining.webp"))
    # config
    st.set_page_config(
        page_title="Modeles",
        page_icon=dmImage,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.markdown("""## Exploration de modeles et predictions""")
    st.sidebar.markdown("""---""")
    st.sidebar.markdown("""Dans cette section, vous pouvez explorer les modeles de machine learning et faire des 
    predictions sur des commentaires/avis""")
    show_sidebar_footer()
    st.session_state.more_stuff = False
    st.header("Modele de classification")
    # Get the model to use
    t1, t2 = st.tabs(["Naive Bayes", "Random Forest"])
    # load image
    sentimentJpg = Image.open(os.path.join(data_path, "assets/sentiment analysis.jpg"))

    st.image(sentimentJpg, caption='Sentiment Analysis', use_column_width=True)

    # load the vectorizer with pickle
    vectorizer = pickle.load(open(os.path.join(data_path, 'vectorizers/vectorizer75.pickle'), 'rb'))

    with t1:
        model1 = joblib.load(os.path.join(data_path, 'models/nb_model75.sav'))
        description_section("Modele", "Naive Bayes")
        st.markdown("""### Demonstration""")
        text1 = st.text_area("Saissisez le texte a classer", key="text1")
        sbt1 = st.button("Prédire le sentiment", key="sbt1")
        if sbt1:
            sentiment = predict_sentiment(model1, vectorizer, text1)
            # Show the sentiment using emoji and color in a box and with big font
            st.markdown(f"""<div style="background-color:#F5F5F5; padding: 10px; border-radius: 10px;
                        font-size: 25px; color: #000000; font-weight: bold; text-align: center;">
                        {SENTIMENT_WITH_EMOJI[sentiment]}</div>""", unsafe_allow_html=True)
    with t2:
        description_section("Modele", "Random Forest")
        model = joblib.load(os.path.join(data_path, 'models/nb_model75.sav'))
        st.markdown("""### Demonstration""")
        text2 = st.text_input("Saissisez le texte a classer", key="text2")
        # Predict the sentiment
        sbt2 = st.button("Prédire le sentiment", key="sbt2")
        if sbt2:
            sentiment = predict_sentiment(model, vectorizer, text2)
            # Show the sentiment using emoji and color in a box and with big font
            st.markdown(f"""<div style="background-color:#F5F5F5; padding: 10px; border-radius: 10px;
            font-size: 25px; color: #000000; font-weight: bold; text-align: center;">
            {SENTIMENT_WITH_EMOJI[sentiment]}</div>""", unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown("""## Conclusion""")
    st.markdown("""Les deux modeles ont donné des resultats satisfaisants. Le modele Naive Bayes a donné un score de 77% dans un premier temps,
    et le modele Random Forest a donné un score de 84%.
    Puis lorsque nous avons reduit la longueur des critiques et entrainé avec un vectoriseur de bi-grammes, le modele Naive Bayes a donné un score de 80%,
    qui est un peu meilleur que le premier modele. Le modele Random Forest a donné un score de 83% un peu moins que le premier modele.
    """)
    st.markdown("""---""")
    # load image
    accuracy_scores = Image.open(os.path.join(data_path, "assets", "Modeles_Accuracy.png"))
    st.image(accuracy_scores, caption='Modeles Accuracy', use_column_width=True)


if __name__ == '__main__':
    modeling_page()
