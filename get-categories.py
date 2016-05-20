import sys
from pick import pick
from tabulate import tabulate
from natsort import natsorted, ns

def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def inInterval(s, m, n):
    try:
        digit = int(s)
    except ValueError:
        return False
    if digit >= m and digit <= n:
        return True
    else:
        return False

def getWeight(category_name, min_weight, max_weight):
    weight = raw_input("Enter weight for category '{}': ".format(category_name))
    while not inInterval(weight, min_weight, max_weight):
        weight = raw_input("Weight for category '{2}' must be between {0} and {1}.\nEnter weight for category '{2}': ".format(min_weight, max_weight, category_name))
    return int(weight)

def getCustomCat():
    choice = raw_input("Enter custom category: ")
    while choice == '':
        choice = raw_input("\nCategory cannot be empty!\nEnter custom category: ")
    return choice

def u(total_points = 100):
    categories  = ['Custom', 'Midterms', 'Final Exam', 'Homework', 'Labs', 'Quizzes']
    prompt      = 'Choose graded categories.'
    choice, i   = pick(categories, prompt, indicator = '=>')
    if choice == 'Custom':
        choice = getCustomCat()
    else:
        del categories[i]
    chosen_cats = [[choice]]
    categories.append('DONE')
    table = tabulate(chosen_cats, headers = ['Type'], tablefmt = 'orgtbl')
    while choice != 'DONE':
        prompt = "Current categories:\n\n{}\n\nAdd another category?".format(table)
        choice, i = pick(categories, prompt, indicator = '=>')
        if choice != 'DONE':
            if choice == 'Custom':
                choice = getCustomCat()
            else:
                del categories[i]
            chosen_cats.append([choice])
            table = tabulate(chosen_cats, headers = ['Type'], tablefmt = 'orgtbl')
    query_yes_no("Are these all the categories?")
