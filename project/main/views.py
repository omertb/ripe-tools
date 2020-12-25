from flask import Blueprint, request, render_template, flash
from project.main.forms import MainForm


main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    error = None
    form = MainForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            ip_or_asn = form.ip_or_asn.data
            print(ip_or_asn)
            print(request.form['ip_or_asn'])
            flash("Entry is {}".format(ip_or_asn))
        else:
            print("NOT VALID!")
    return render_template('main.html', form=form, error=error)
