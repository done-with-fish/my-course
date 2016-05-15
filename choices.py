from pick import pick
from datetime import date
from tabulate import tabulate

def chooseYear():
    if date.today().month > 10:
        default_year = date.today().year + 1
    else:
        default_year = date.today().year
    input_year = raw_input("Input term year [{}]: ".format(default_year)) or default_year
    while not str(input_year).isdigit():
        input_year = raw_input("Input term year [{}]: ".format(default_year)) or default_year
    return str(input_year)

def chooseSemester():
    semesters   = ['Fall', 'Spring',  'Summer Term 1',  'Summer Term 2']
    semester, i = pick(semesters, 'Choose semester.', indicator = '=>', default_index = 0)
    return semester

def chooseCourseNumber():
    course_number = raw_input("Input course number [212]: ") or '212'
    return course_number

def chooseSectionNumber():
    section_number = raw_input("Input section number [1]: ") or '1'
    return section_number

def t():
    categories = ['Exams', 'Final Exam', 'Homework', 'Labs', 'Projects', 'Quizzes']
    dic        = {}
    prompt     = 'Choose graded categories.'
    choice, i  = pick(categories, prompt, indicator = '=>', default_index = 0)

    del categories[i]
    categories.append('DONE')

    choice_weight = False
    while not str(choice_weight).isdigit():
        choice_weight = raw_input("Enter weight for category '{}': ".format(choice))

    dic[choice] = int(choice_weight)
    L           = [[key, dic[key]] for key in dic]
    table       = tabulate(L, headers = ['Type', 'Weight'], tablefmt='orgtbl')

    while choice != 'DONE':
        prompt      = "Current list is:\n\n{}\n\nAdd another graded category?".format(table)
        choice, i = pick(categories, prompt, indicator = '=>', default_index = 0)
        
        if choice != 'DONE':
            del categories[i]
            choice_weight = False
            while not str(choice_weight).isdigit():
                choice_weight = raw_input("Enter weight for category '{}': ".format(choice))
                dic[choice] = int(choice_weight)
                L           = [[key, dic[key]] for key in dic]
                table       = tabulate(L, headers = ['Type', 'Weight'], tablefmt='orgtbl')
    
    return dic
    
