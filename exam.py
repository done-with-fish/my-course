from student import Student
import csv
import orgtbl
import os
import statistics


def swap_problem(s):
    n = s.strip('abcdefghijklmnopqrstuvwxyz')
    l = s.strip('0123456789')
    if l:
        l = ' (' + l + ')'
    return 'Problem ' + n + l


class Exam():
    def __init__(self, scores_dcts):
        self.scores_dcts = scores_dcts

    @property
    def students(self):
        roster_path = (
            '/home/brian/ownCloud/teaching/16-summer-t1/math-216/info/sec1-roster.csv'
        )
        reader = csv.DictReader(open(roster_path))
        dcts = [row for row in reader]
        return [Student(dct) for dct in dcts]

    @property
    def scores(self):
        return [
            sum(dct[_] for _ in dct if _ != 'name') 
            for dct in self.scores_dcts
            if dct['name'] != 'grothendieck'
        ]

    @property
    def mean(self):
        return statistics.mean(self.scores)

    @property
    def median(self):
        return statistics.median(self.scores)

    @property
    def high(self):
        return max(self.scores)

    @property
    def low(self):
        return min(self.scores)

    @property
    def grothendieck(self):
        for dct in self.scores_dcts:
            if dct['name'] == 'grothendieck':
                return dct
                break

    def write_org_files(self):
        reports_path = '/home/brian/ownCloud/teaching/16-summer-t1/math-216/gradebook/exam3/reports'
        problems = sorted(self.grothendieck.keys())
        problems.remove('name')
        for student in self.students:
            for dct in self.scores_dcts:
                if student.name == dct['name']:
                    student_dct = dct
                    break
            file_name = student.abbrev + '.org'
            file_path = os.path.join(reports_path, file_name)
            problem_names = [key for key in dct if key != 'name']
            target = open(file_path, 'w')
            target.write('#+Title: Exam III Results\n')
            target.write('#+Author: {}\n'.format(student.preferred_name))
            target.write('#+Options: timestamp:t date:t toc:nil num:nil\n\n')
            target.write('* Score: {}\n\n'.format(sum(student_dct[key] for key in student_dct if key != 'name')))
            target.write('| Problem | Possible | Score |\n')
            target.write('|-\n')
            for problem in problems:
                target.write('| {0} | {1} | {2} |\n'.format(swap_problem(problem), self.grothendieck[problem], student_dct[problem]))
            target.write('|-\n')
            target.write('| Total | {0} | {1} |\n\n'.format(sum(self.grothendieck[_] for _ in self.grothendieck if _ != 'name'), sum(student_dct[_] for _ in student_dct if _ != 'name')))
            target.write('* Statistics\n\n')
            target.write('| Mean | {0:.3f} |\n'.format(self.mean))
            target.write('| Median | {} |\n'.format(self.median))
            target.write('| High | {} |\n\n'.format(self.high))
            target.write('* Grade Cutoffs (Approximate)\n\n')
            target.write('| A | 83-100 |\n')
            target.write('| B | 64-82 |\n')
            target.write('| C | 0-63|\n')
            target.close()


def make_grades():
    scores_path = (
        '/home/brian/ownCloud/teaching/16-summer-t1/math-216/gradebook/exam3/scores.org'
    )
    scores_dcts = orgtbl.file_to_dcts(scores_path, table_name='scores')
    return scores_dcts


# make_grades()

def make_exam():
    x = Exam(make_grades())
    x.write_org_files()

make_exam()
