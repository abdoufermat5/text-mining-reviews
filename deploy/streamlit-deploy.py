import joblib
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from predict import predict_sentiment

st.title('Classification des critiques sur les telephones portables')
st.markdown('Classifiez les critiques sur les telephones portables en 5 niveaux de sentiments: **negatif**, '
            '**neutre**, **positif**, **tres positif** et **tres negatif**.')
st.markdown('**Exemple:** "Le telephone est tres bon, je le recommande." le sentiment est **tres positif**.')
st.markdown('**Exemple:** "Le telephone est tres mauvais, je ne le recommande pas." le sentiment est **tres negatif**.')
st.markdown('**Exemple:** "Le telephone est bon." le sentiment est **positif**.')
st.markdown('**Exemple:** "Le telephone est mauvais." le sentiment est **negatif**.')
st.markdown('**Exemple:** "Le telephone est acceptable." le sentiment est **neutre**.')

# load the classifier and vectorizer
classifier = joblib.load('../data/models/rf_model75.sav')
vectorizer = pickle.load(open('../data/vectorizers/vectorizer75.pickle', 'rb'))

# get the user input
user_input = st.text_input('Entrez votre critique sur les telephones portables:')

if user_input and st.button("Predict sentiment"):
    sentiment = predict_sentiment(classifier, vectorizer, user_input)
    st.write('Le sentiment de la critique est **{}**.'.format(sentiment))

st.markdown('**Note:** Le modele a ete entraine sur un jeu de donnees de 100000 critiques sur les telephones portables.')
st.markdown(
    '`Create by` [esprit_bayesien](https://twitter.com/esprit_bayesien) | \
         `Code:` [GitHub](https://github.com/abdoufermat5/text-mining-reviews)')
