import os
import pickle

import joblib
import streamlit as st
from PIL import Image

from fermat_helpers.descriptions import description_section
from fermat_helpers.predict import predict_sentiment

SENTIMENT = {1: "très mauvais", 2: "mauvais", 3: "neutre", 4: "bon", 5: "très bon"}

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
        text1 = st.text_area("Saissisez le texte a classer", key="text1")
        sbt1 = st.button("Prédire le sentiment", key="sbt1")
        if sbt1:
            sentiment = predict_sentiment(model1, vectorizer, text1)
            # Show the sentiment
            st.write('Le sentiment de la critique est **{}**.'.format(SENTIMENT[sentiment].upper()))
    with t2:
        description_section("Modele", "Random Forest")
        model = joblib.load(os.path.join(data_path, 'models/nb_model75.sav'))

        text2 = st.text_input("Saissisez le texte a classer", key="text2")
        # Predict the sentiment
        sbt2 = st.button("Prédire le sentiment", key="sbt2")
        if sbt2:
            sentiment = predict_sentiment(model, vectorizer, text2)
            # Show the sentiment
            st.write('Le sentiment de la critique est **{}**.'.format(SENTIMENT[sentiment].upper()))


if __name__ == '__main__':
    modeling_page()
