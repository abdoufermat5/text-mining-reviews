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


def remove_special_characters(text):
    """
    Remove special characters from a text includes dots, commas, exclamation marks, etc.
    """
    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    # remove multiple spaces
    text = re.sub(r"\s+", " ", text)
    # remove leading and trailing spaces
    text = text.strip()
    # return the text
    return text
