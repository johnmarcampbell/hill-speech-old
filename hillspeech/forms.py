from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Required

class GetSpeakerForm(FlaskForm):
    '''Have the user input the name of a speaker'''
    name = StringField('speaker_name', [Length(min=1)] )
    submit = SubmitField('Search for Speaker')

