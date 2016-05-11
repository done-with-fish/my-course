#!/usr/bin/python

import csv, os, sys, inspect, subprocess, statistics, re

def strip_fringe_whitespace(s):
    s = s.lstrip(' ')
    s = s.rstrip(' ')
    return s

def parse_name(s):
    last, rest = s.split(',')

    last = strip_fringe_whitespace(last)
    rest = strip_fringe_whitespace(rest)

    first    = rest
    middle   = False
    nickname = False

    if '(' in rest:
        nickname = rest[rest.index('(') + 1:rest.rindex(')')]
        nickname = strip_fringe_whitespace(nickname)

        rest = rest.rstrip('(' + nickname + ')')
        rest = strip_fringe_whitespace(rest)

    if ' ' in rest:
        first, middle = rest.split(' ', 1)

        first  = strip_fringe_whitespace(first)
        middle = strip_fringe_whitespace(middle)

    return {'first': first, 'last': last, 'middle': middle, 'nickname': nickname}

def swap_problem(s):
    n = s.strip('abcdefghijklmnopqrstuvwxyz')
    # n = n.lstrip('0')
    l = s.strip('0123456789')
    if l:
        l = ' (' + l + ')'
    return 'Problem ' + n + l

def get_category_info(category):
    dirs = [x for x in os.listdir('../') if category in x]
    for assignment in dirs:
        bash_command = "sh export-table-from-org.sh ../{0}/ {1} {2}".format(assignment, 'scores.org', 'scores')
        process      = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output       = process.communicate()[0]
    sheets = [csv.DictReader(open('../' + assignment + '/scores.csv')) for assignment in dirs]
    return [[row for row in sheet] for sheet in sheets]

def replace_keys(d):
    for key in d.keys():
        if not key == 'name':
            d[swap_problem(key)] = d.pop(key)
    return d

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def sort_dict(d):
    keys = [key for key in d]
    keys.sort(key = natural_keys)
    return [[key, d[key]] for key in keys]

class Student:
    possible_exam_points     = []
    possible_homework_points = []
    possible_final_points    = []
    def __init__(self, d):
        self.sid         = d['Student ID']
        self.uid         = d['Duke Unique ID']
        self.name        = d['Name']
        self.email       = d['Email Address']
        self.dean        = d['Dean']
        self.grade_basis = d['Grade Basis']

        self.name_dict = parse_name(self.name)

        self.first_name  = self.name_dict['first']
        self.last_name   = self.name_dict['last']
        self.middle_name = self.name_dict['middle']
        self.nickname    = self.name_dict['nickname']

        self.exam_scores       = []
        self.homework_scores   = []
        self.final_exam_scores = []

class Exam:
    def __init__(self, path):
        self.reader = csv.DictReader(open(path))
