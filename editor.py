import os
import tempfile


def edit_string(content=''):
    f = tempfile.NamedTemporaryFile(mode='w+')
    if content:
        f.write(content)
        f.flush()
    status = os.system('emacs -nw {} -f org-mode'.format(f.name))
    f.seek(0, 0)
    text = f.read()
    f.close()
    assert not os.path.exists(f.name)
    return text


def edit_file(file_path):
    f = tempfile.NamedTemporaryFile(mode='w+')
    if os.path.isfile(file_path):
        with open(file_path, 'r') as myfile:
            f.write(myfile.read())
            f.flush()
    status = os.system('emacs -nw {} -f org-mode'.format(f.name))
    f.seek(0, 0)
    text = f.read()
    f.close()
    assert not os.path.exists(f.name)
    return text
