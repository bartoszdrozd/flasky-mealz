from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MealForm(FlaskForm):
    name = StringField('What is meal name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
