import csv, re

def stripFringeWhitespace(s):
    s = s.lstrip(' ')
    s = s.rstrip(' ')
    return s

def rreplace( s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def legalRow(s):
    status = True
    if s.startswith('|-') or s.startswith('TBL') or len(s) < 1 or s.startswith('#+TBL'):
        status = False
    return status

def parseTableRow(s):
    s = s.replace('|', '', 1)
    s = rreplace(s, '|', '', 1)
    s = stripFringeWhitespace(s)
    s = re.sub(r'\s*\|\s*', '|', s)
    return s

def orgTableToReader(file_path, table_name = False):
    data = open(file_path).read()

    if table_name:
        mo   = re.search("TBLNAME: {0}\n.*?\n(\n|$)".format(table_name), data, re.S)
        myfile = mo.group(0).splitlines()
    else:
        myfile = data.splitlines()

    myNewFile = [parseTableRow(row) for row in myfile if legalRow(row)]

    reader = csv.DictReader(myNewFile, delimiter='|')

    return reader

def orgTableToDict(file_path, table_name = False):
    reader = orgTableToReader(file_path, table_name)
    return [row for row in reader]

L = orgTableToDict('/home/brian/teaching/16-fall/math-212/info/sec1-roster.org')

for x in L:
    print x

print len(L)
