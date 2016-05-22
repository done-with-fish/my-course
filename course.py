from natsort import natsorted, ns
from student import Student
import choices
import csv
import os
import pickle
import subprocess
import sys


class Course:

    teaching_dir = '/home/brian/TEST-COURSE/teaching'
    webpage_dir = '/home/brian/TEST-COURSE/webpage/public_html/teaching'

    def __init__(self, dct):
        self.year = dct['year']
        self.semester = dct['semester']
        self.course_nbr = dct['course number']
        self.section_nbr = dct['section number']
        self.grade_weights = dct['grade weights']
        self.roster_source = dct['roster source']

    @classmethod
    def from_input(cls):
        dct = {}
        dct['year'] = choices.year()
        dct['semester'] = choices.semester()
        dct['course number'] = choices.course_nbr()
        dct['section number'] = choices.section_nbr()
        dct['grade weights'] = choices.grade_weights()
        dct['roster source'] = choices.find_roster()
        return cls(dct)

    def make_term(self):
        dct = {
            'Fall': 'fall',
            'Spring': 'spring',
            'Summer Term 1': 'summer-t1',
            'Summer Term 2': 'summer-t2'
        }
        self.term = self.year.replace('20', '', 1) + '-' + dct[self.semester]
        return None

    def make_name(self):
        self.name = 'math' + self.course_nbr
        return None

    def make_dirs(self):
        self.make_term()
        self.make_name()
        under_teaching = ['docs', 'exams', 'gradebook', 'scratch', 'info']
        under_webpage = [self.term + '/' + self.name]
        for path in [Course.teaching_dir, Course.webpage_dir]:
            if not os.path.exists(path):
                os.makedirs(path)
        for d in under_teaching:
            path = os.path.join(Course.teaching_dir, d)
            setattr(self, d + '_path', path)
            if not os.path.exists(path):
                os.makedirs(path)
        path = os.path.join(Course.webpage_dir, self.term, self.name)
        setattr(self, 'webpage_path', path)
        if not os.path.exists(path):
            os.makedirs(path)
        return None

    def make_roster(self):
        roster_dest = os.path.join(
            self.info_path, 'sec{}-roster.csv'.format(self.section_nbr))
        command = "ssconvert {0} {1}".format(self.roster_source, roster_dest)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        self.roster_path = roster_dest
        return None

    def get_students(self):
        reader = csv.DictReader(open(self.roster_path))
        dcts = [row for row in reader]
        self.students = [Student(dct) for dct in dcts]
        for student in self.students:
            student.parse_name()
        return None

    def make_labels(self):
        self.labels_tex = os.path.join(
            self.info_path, 'sec{}-labels.tex'.format(self.section_nbr))
        target = open(self.labels_tex, 'w')
        target.write('\\documentclass[]{letter}\n')
        target.write(('\\usepackage[avery5160label,noprintbarcodes,'
                      'nocapaddress]{envlab}\n'))
        target.write('\\makelabels\n')
        target.write('\\begin{document}\n')
        target.write('\\startlabels\n')
        for x in self.students:
            target.write('\\mlabel{{}}{{\\texttt{{{0}\\\\ Section {1}}}}}\n'.format(x.preferred_name, self.section_nbr))
        target.write('\\end{document}\n')
        target.close()
        labels_pdf = os.path.join(
            self.info_path, 'sec{}-labels.pdf'.format(self.section_nbr))
        command = (
            'pdflatex -output-directory={0} {1}'
        ).format(self.info_path, self.labels_tex)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

x = Course({'year': '2016', 'semester': 'Fall', 'course number': '212', 'section number': '1', 'grade weights': {}, 'roster source': '/home/brian/downloads/ps.xls'})
x.make_dirs()
x.make_roster()
x.get_students()
x.make_labels()

