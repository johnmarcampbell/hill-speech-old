from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from pymongo import MongoClient
import pickle

from helpers import get_speaker_topics

DICTIONARY_PATH = 'models/dictionary_97-07_and_10-18.dict'
with open(DICTIONARY_PATH, 'rb') as f:
    dictionary = pickle.load(f)

MODEL_PATH = 'models/all_50topics.lda'
model = LdaModel.load(MODEL_PATH)

bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speaker/<speaker>')
def speaker(speaker):
    topics = get_speaker_topics(model, speaker, dictionary) # Not currently using

    client = MongoClient()
    db = client['congressional-record']
    speeches = db['speeches']   
    search = {"speaker": speaker}
    result = speeches.find_one(search)
    client.close()

    if result:
        content = result['text']
    else:
        content = 'No records returned'

    return render_template('speaker.html', speaker=speaker, content=content)


if __name__ == '__main__':
	app.run(port=5000, debug=True)
