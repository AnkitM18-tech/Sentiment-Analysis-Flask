from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob,Word
import random
import time

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze',methods=['POST'])
def analyze():
    start = time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        blob = TextBlob(rawtext)
        received_text = blob
        blob_sentiment,blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        number_of_tokens = len(list(blob.words))
        nouns = list()
        summary =list()
        time_elapsed =0
        for word,tag in blob.tags:
            if tag=="NN":
                nouns.append(word.lemmatize())
                len_of_words = len(nouns)
                rand_words = random.sample(nouns, len_of_words)
                final_word = list()
                for item in rand_words:
                    word = Word(item).pluralize()
                    final_word.append(word)
                    summary = final_word
                    end = time.time()
                    time_elapsed = end - start

    return render_template("index.html", received_text=received_text,number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity, summary=summary, time_elapsed=time_elapsed)

if __name__ == '__main__':
    app.run(debug=True)