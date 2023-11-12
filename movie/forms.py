from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class CreateMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
