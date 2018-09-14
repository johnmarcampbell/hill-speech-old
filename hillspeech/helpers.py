from pymongo import MongoClient

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
