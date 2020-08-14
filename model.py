from wtforms import Form, FloatField, validators, IntegerField, StringField
from math import pi

class InputForm(Form):
    nodes = StringField(
        label='nodes', default="-1",
        validators=[validators.InputRequired()])

    edges = StringField(
        label='edges', default= "-1,-1",
        validators=[validators.InputRequired()])
