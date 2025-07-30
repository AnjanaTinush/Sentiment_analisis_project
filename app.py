from flask import Flask, render_template
# from helper import preprocessing, vectorizer, get_prediction
# from logger import logging

app = Flask(__name__)

data = dict()
reviews = ["Good product","Bad product",'I like id']
positive = 2
negative = 1

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    logging.info('========== Open home page ============')

    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()