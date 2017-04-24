class Student:
    def __init__(self, dct):
        self.sid = dct['Student ID']
        self.uid = dct['Duke Unique ID']
        self.name = dct['Name']
        self.email = dct['Email Address']
        self.dean = dct['Dean']
        self.grade_basis = dct['Grade Basis']


    @property
    def preferred_name(self):
        last, rest = self.name.split(',')
        last = last.strip()
        rest = rest.strip()
        first = rest
        middle = False
        nickname = False
        if '(' in rest:
            nickname = rest[rest.index('(') + 1:rest.rindex(')')]
            nickname = nickname.strip()
            rest = rest.rstrip('(' + nickname + ')')
            rest = rest.strip()
        if ' ' in rest:
            first, middle = rest.split(' ', 1)
            first = first.strip()
            middle = middle.strip()
        dct = {
            'first': first,
            'last': last,
            'middle': middle,
            'nickname': nickname
        }
        self.first_name = dct['first']
        self.last_name = dct['last']
        self.middle_name = dct['middle']
        self.nickname = dct['nickname']
        if self.nickname:
            return self.nickname + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    @property
    def abbrev(self):
        last = self.name.split(',')[0].split()[0]
        return last.lower()
