from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators

class GetSpeakerForm(FlaskForm):
    '''Have the user input the name of a speaker'''
    name = TextField()
    submit = SubmitField('Get Speaker')

