from pick import pick
from datetime import date
import ConfigParser, os, subprocess, sys

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

def find_roster():
    if len(sys.argv) > 1:
        path = str(sys.argv[1])
    else:
        default_path = '/home/brian/downloads/ps.xls'
        path = raw_input("Input path to roster [{}]: ".format(default_path)) or default_path

    while not os.path.isfile(path):
        default_path = '/home/brian/downloads/ps.xls'
        path = raw_input("Path invalid. Try again [{}]: ".format(default_path)) or default_path

    return path

def make_roster_file(roster_path, new_path):
    command = "ssconvert {0} {1}".format(roster_path, new_path)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

def make_dirs(l):
    for x in l:
        if not os.path.exists(x):
            os.makedirs(x)

# def make_labels():
#     csv.DictReader(open())
#     target = open(file_path, 'w')
#     target.write("\documentclass[]{letter}\n")
#     target.write("\usepackage[avery5160label,noprintbarcodes,nocapaddress]{envlab}\n")
#     target.write("\makelabels\n")
#     target.write("\begin{document}\n")
#     target.write("\startlabels\n")

#     target.write("\mlabel{}{\texttt{Ryan Alexander Bloom\\Section 4}}\n")
#     target.write("\end{document}\n")

#     target.close()

def make_course():
    semester       = choose_semester()
    year           = choose_year()
    course_number  = choose_course_number()
    section_number = choose_section_number()
    roster_path    = find_roster()

    term_abbrev = abbreviate_term(year, semester)

    config = ConfigParser.RawConfigParser()
    config.read('.dirs.cfg')

    teaching_path  = config.get('dirs', 'teaching_directory')
    term_path      = teaching_path + term_abbrev
    course_path    = term_path + '/math-' + course_number
    exams_path     = course_path + '/exams'
    info_path      = course_path + '/info'
    gradebook_path = course_path + '/gradebook'
    scratch_path   = course_path + '/scratch'
    
    make_dirs([
        teaching_path, 
        term_path, 
        course_path, 
        exams_path, 
        info_path, 
        gradebook_path, 
        scratch_path
    ])
    make_roster_file(roster_path, info_path + '/sec{}-roster.csv'.format(section_number))

make_course()
