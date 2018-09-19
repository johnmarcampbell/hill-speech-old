from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from pymongo import MongoClient
from bokeh.embed import components
import pickle

from helpers import get_speaker_topics, get_topic_name, make_topic_plot
from forms import GetSpeakerForm

DICTIONARY_PATH = 'models/dictionary_97-07_and_10-18.dict'
with open(DICTIONARY_PATH, 'rb') as f:
    dictionary = pickle.load(f)

MODEL_PATH = 'models/all_50topics.lda'
model = LdaModel.load(MODEL_PATH)

bootstrap = Bootstrap()
app = Flask(__name__)
app.secret_key = 'dev_key'
bootstrap.init_app(app)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speaker', methods=['GET', 'POST'])
def speaker():
    form = GetSpeakerForm()
    if form.validate_on_submit():
        speaker = form.name.data
        print("Speaker: " + speaker)
    else:
        speaker = 'kilmer'

    topics = get_speaker_topics(model,speaker, dictionary)
    topics = [(get_topic_name(x[0]), x[1]) for x in topics]

    topics.sort(key=lambda x:x[1])
    labels = [x[0] for x in topics]
    vals = [x[1] for x in topics]

    p = make_topic_plot(labels, vals)
    script, div = components(p)

    return render_template('speaker.html', speaker=speaker,
            script=script, div=div, form=form)


if __name__ == '__main__':
	app.run(port=5000, debug=True)
