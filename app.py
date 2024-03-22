from flask import Flask, render_template, request
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalnum() and word not in stop_words and word not in string.punctuation]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("mnb.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['text']
        transformed_mail = preprocess_text(input_text)
        vector = tfidf.transform([transformed_mail])
        prediction = model.predict(vector)[0]
        if prediction == 1:
            result = "The email is predicted to be spam."
        else:
            result = "The email is predicted to be Ham."
        return render_template('result.html', prediction=result)
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)