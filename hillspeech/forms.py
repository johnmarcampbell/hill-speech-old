from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import Length, Required

class GetSpeakerForm(FlaskForm):
    '''Have the user input the name of a speaker'''
    name = TextField('speaker_name', [Length(min=1)] )
    submit = SubmitField('Get Speaker')

