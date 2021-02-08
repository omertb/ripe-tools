from flask import Blueprint, request, render_template, jsonify, session
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
def lg():
    error = None
    form = MainForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            network = form.ip_or_asn.data
            if addr_is_valid(network):
                network += "/24"
            else:
                error = "Invalid input!"
                return error

            lg_result = get_lg(network)
            result_list = lg_table_source(lg_result)
            return jsonify(result_list)

    return render_template('lg.html', form=form, error=error)


@main_blueprint.route('/bgplay', methods=['GET', 'POST'])
def bgplay():
    error = None
    if request.method == "GET":
        session['time_factor'] = 1
    form = MainForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            ip_or_asn = form.ip_or_asn.data
            if addr_is_valid(ip_or_asn):
                ip_or_asn += "/24"
            elif asn_is_valid(ip_or_asn):
                ip_or_asn = "AS" + ip_or_asn
            else:
                error = "Invalid input!"
                return error

            if request.form['timerange'] == "prev":
                session['time_factor'] += 1
            elif request.form['timerange'] == "next" and session['time_factor'] != 1:
                session['time_factor'] -= 1

            bgplay_result = get_bgplay(ip_or_asn, session['time_factor'])
            result_list = bgplay_table_source(bgplay_result)
            result = {
                'query_endtime': bgplay_result['data']['query_endtime'],
                'query_starttime': bgplay_result['data']['query_starttime'],
                'message': ": ".join(bgplay_result['messages'][0]) if bgplay_result['messages'] else "",
                'result_table': result_list
            }
            return jsonify(result)

    return render_template('bgplay.html', form=form, error=error)
