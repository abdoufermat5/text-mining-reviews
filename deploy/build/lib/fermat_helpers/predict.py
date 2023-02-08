# function that predicts the sentiment of an input text
# input: classifier, vectorizer, text
# output: sentiment
def predict_sentiment(classifier, vectorizer, text):
    """
    Predict the sentiment of a text using a classifier.
    Vectorizes the text and uses the classifier to predict the sentiment.
    """
    # vectorize the text
    vectorized_text = vectorizer.transform([text])
    # predict the sentiment
    result = classifier.predict(vectorized_text)
    # return the predicted sentiment
    return result[0]