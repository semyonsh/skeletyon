from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
 
class ExampleForm(FlaskForm):
    username = StringField(u'Username', [InputRequired(), Length(max=100)])
    submit = SubmitField(u'Go!')