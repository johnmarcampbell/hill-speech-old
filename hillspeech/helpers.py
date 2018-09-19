from pymongo import MongoClient
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# These are hard-coded topic labels for a particular model.
# This is very brittle and will have to change later.
TOPIC_LABELS = [
    (1, 'Legislation'),
    (3, 'Committees'),
    (4, 'Community'),
    (5, 'Finance'),
    (6, 'Budget'),
    (7, 'Laws'),
    (9, 'Education'),
    (10, 'Healthcare'),
    (11, 'Military Service'),
    (14, 'International Relations'),
    (16, 'Economics'),
    (18, 'Employment'),
    (19, 'Procedure'),
    (20, 'Defense'),
    (22, 'History'),
    (24, 'Environment'),
    (26, 'Technology'),
    (28, 'Disaster'),
    (29, 'Resolutions/Bills'),
    (31, 'Energy'),
    (32, 'Taxes'),
    (33, 'Healthcare II'),
    (34, 'Procedure II'),
    (35, 'Procedure III'),
    (36, 'Sports'),
    (37, 'Immigration'),
    (40, 'Votes'),
    (41, 'Procedure IV'),
    (42, 'Agriculture'),
    (43, 'Hunger'),
    (45, 'Boy Scouts')
]

def get_speaker_corpus_bow(speaker, speech_dict):
    '''Connect to mongodb and get the corpus of text'''
    client = MongoClient()
    db = client['congressional-record']
    speeches = db['speeches']   
    search = {"speaker": speaker}

    speaker_corpus = ' '.join([post['lemma'] for post in speeches.find(search)])
    client.close()
    
    speaker_corpus_bow = speech_dict.doc2bow(speaker_corpus.split())

    return speaker_corpus_bow

def get_speaker_topics(model, speaker, speech_dict):
    bow = get_speaker_corpus_bow(speaker, speech_dict)
    return model.get_document_topics(bow)

def get_topic_name(index):
    for (n,t) in TOPIC_LABELS:
        if n == index:
            return t
    return 'Topic_'+str(index)

def make_topic_plot(labels, vals):
    source = ColumnDataSource(data=dict(topics=labels, focus=vals))
    p = figure(y_range=labels)
    p.hbar(y='topics', right='focus', source=source, height=0.8)
    return p
