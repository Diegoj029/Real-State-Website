from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Contact_form(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired()])
    phone = StringField("Teléfono", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
    message = StringField("Mensaje", validators=[DataRequired()])
