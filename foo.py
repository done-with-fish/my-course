from pick import pick
from datetime import date
import sys
import os

def choose_year():
    if date.today().month > 10:
        default_year = date.today().year + 1
        default_year = str(default_year)
    else:
        default_year = date.today().year
        default_year = str(default_year)
    chosen_year = raw_input("Input term year [{}]: ".format(default_year)) or default_year
    return chosen_year

def choose_semester():
    dic = {
        'Fall'          : 'fall',
        'Spring'        : 'spring',
        'Summer Term 1' : 'summer-t1',
        'Summer Term 2' : 'summer-t2'
    }
    semesters   = ['Fall', 'Spring',  'Summer Term 1',  'Summer Term 2']
    semester, i = pick(semesters, 'Choose semester.', indicator = '=>', default_index = 0)
    return semester

def choose_course_number():
    course_number = raw_input("Input course number [212]: ") or '212'
    return course_number

def choose_section_number():
    section_number = raw_input("Input section number [1]: ") or '1'
    return section_number

def abbreviate_term(year, semester):
    dic = {
        'Fall'          : 'fall',
        'Spring'        : 'spring',
        'Summer Term 1' : 'summer-t1',
        'Summer Term 2' : 'summer-t2'
    }
    term_abbrev = year.replace('20', '', 1) + '-' + dic[semester]
    return term_abbrev

def make_course():
    semester       = choose_semester()
    year           = choose_year()
    course_number  = choose_course_number()
    section_number = choose_section_number()

    print "You chose year: {}".format(year)
    print "You chose semester: {}".format(semester)
    print "You chose section number: {}".format(section_number)
    print "Your term abbreviation: {}".format(abbreviate_term(year, semester))
    print "Your course: Math {}".format(course_number)

def find_roster():
    if len(sys.argv) > 1:
        path = str(sys.argv[1])
    else:
        default_path = '/home/brian/downloads/ps.xls'
        path = raw_input("Input path to roster [{}]: ".format(default_path)) or default_path
    print os.path.isfile(path)

find_roster()


# title = 'Welcome to myClass!\n\nWhat would you like to do?'
# options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
# option, index = pick(options, title, indicator='=>', default_index=2)
# print(option, index)
