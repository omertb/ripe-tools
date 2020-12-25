from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import escape


class MainForm(FlaskForm):
    ip_or_asn = StringField("Enter Network or ASN:", validators=[DataRequired()])
