from datetime import date
from pick import pick
# import ConfigParser
import editor
import orgtbl
import os
import yesno


def year():
    if date.today().month > 10:
        default_year = date.today().year + 1
    else:
        default_year = date.today().year
    prompt = 'Input term year [{}]: '.format(default_year)
    os.system('clear')
    input_year = raw_input(prompt) or default_year
    while not str(input_year).isdigit():
        prompt = 'Input term year [{}]: '.format(default_year)
        input_year = raw_input(prompt) or default_year
    return str(input_year)


def semester():
    semesters = ['Fall', 'Spring',  'Summer Term 1',  'Summer Term 2']
    semester, i = pick(semesters, 'Choose semester.', indicator='=>')
    return semester


def course_nbr():
    os.system('clear')
    return raw_input('Input course number [212]: ') or '212'


def section_nbr():
    os.system('clear')
    return raw_input('Input section number [1]: ') or '1'


def grade_weights():
    root = os.path.dirname(os.path.realpath(__file__))
    org_file = os.path.join(root, '.weights.org')
    table_string = open(org_file).read()
    while True:
        table_string = editor.edit_string(table_string)
        os.system('clear')
        print(table_string.split('#')[0])
        if yesno.query('Are these weights ok?'):
            break
    dcts = orgtbl.string_to_dcts(table_string)
    dct = {d['category']: int(d['weight'])
           for d in dcts if d['category'] != 'total'}
    return dct


def find_roster():
    default_path = '/home/brian/downloads/ps.xls'
    prompt = "Input path to roster [{}]: ".format(default_path)
    os.system('clear')
    path = raw_input(prompt) or default_path
    while not os.path.isfile(path):
        default_path = '/home/brian/downloads/ps.xls'
        prompt = 'Path invalid. Try again [{}]: '.format(default_path)
        path = raw_input(prompt) or default_path
    return path


# def make_default(dct):
#     config = ConfigParser.RawConfigParser()
#     config.add_section('section1')
#     config.set('section1', 'key', 'value')
#     with open('.config.cfg') as configfile:
#         config.write(configfile)
