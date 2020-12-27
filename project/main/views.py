from flask import Blueprint, request, render_template, flash
from project.main.forms import MainForm
from project.apicalls import *
from pprint import pprint


main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    error = None
    form = MainForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            ip_or_asn = form.ip_or_asn.data
            result = get_bgplay(ip_or_asn)
            pprint(result)
            flash("Result is \n{}".format(result))
        else:
            print("NOT VALID!")
    return render_template('main.html', form=form, error=error)
