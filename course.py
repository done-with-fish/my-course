import choices

class Course:
    def __init__(self, dct):
        self.year = dct['year']
        self.semester = dct['semester']
        self.course_nbr = dct['course number']
        self.section_nbr = dct['section number']
        self.grade_weights = dct['grade weights']
        # self.roster_path = dct['roster path']

    @classmethod
    def from_input(cls):
        dct = {}
        dct['year'] = choices.year()
        dct['semester'] = choices.semester()
        dct['course number'] = choices.course_nbr()
        dct['section number'] = choices.section_nbr()
        dct['grade weights'] = choices.grade_weights()
        dct['roster path'] = choices.find_roster()
        return cls(dct)
