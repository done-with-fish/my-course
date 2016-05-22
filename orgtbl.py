import csv
import re


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def is_relevant(s):
    return bool(s.startswith('|') and not s.startswith('|-'))


def fix_row(s):
    s = s.replace('|', '', 1)
    s = rreplace(s, '|', '', 1)
    s = '|'.join(i.strip() for i in s.split('|'))
    return s


def reader_to_dcts(reader):
    return [row for row in reader]


def list_to_reader(l):
    relevant_lines = [fix_row(row) for row in l if is_relevant(row)]
    reader = csv.DictReader(relevant_lines, delimiter='|')
    return reader


def list_to_dcts(l):
    reader = list_to_reader(l)
    return reader_to_dcts(reader)


def string_to_reader(s):
    table_lines = s.splitlines()
    return list_to_reader(table_lines)


def string_to_dcts(s):
    reader = string_to_reader(s)
    return reader_to_dcts(reader)


def file_to_reader(file_path, table_name=''):
    try:
        string = open(file_path).read()
    except IOError:
        print 'Not a valid filepath.'
        return None
    if table_name:
        header = "TBLNAME: {0}\n.*?\n(\n|$)".format(table_name)
        mo = re.search(header, string, re.S)
        table_lines = mo.group(0).splitlines()
    else:
        table_lines = string.splitlines()
    return list_to_reader(table_lines)


def file_to_dcts(file_path, table_name=''):
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    reader = file_to_reader(file_path, table_name)
    return reader_to_dcts(reader)
