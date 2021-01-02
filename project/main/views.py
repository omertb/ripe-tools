from flask import Blueprint, request, render_template, flash, jsonify
from project.main.forms import MainForm
from project.apicalls import *
from project.json_functions import *
import re


def addr_is_valid(form_input):
    ip_regex = "^(22[0-3]|2[0-1][0-9]|[0-1]?[0-9][0-9]?)\." \
               "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
               "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
               "(0)$"

    if re.search(ip_regex, form_input):
        return True
    return False


def asn_is_valid(form_input):
    try:
        number_input = int(form_input)
        if 0 < number_input < 4200000000 and (number_input < 64512 or number_input > 65534):
            return True
        else:
            return False
    except ValueError:
        return False


main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    error = None
    form = MainForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            ip_or_asn = form.ip_or_asn.data
            if addr_is_valid(ip_or_asn):
                ip_or_asn += "/24"
            elif asn_is_valid(ip_or_asn):
                ip_or_asn = "AS" + ip_or_asn
            else:
                print("ERROR")
                print(ip_or_asn)
                error = "Invalid input!"
                return error
            print(ip_or_asn)
            bgplay_result = get_bgplay(ip_or_asn)
            result = bgplay_table_source(bgplay_result)
            return jsonify(result)
    return render_template('main.html', form=form, error=error)
