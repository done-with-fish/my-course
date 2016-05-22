import subprocess


def export_org_files(path):
    command = ("find {} -type f -iname \"*.org\" -print0 "
               "| parallel -0 org2txt").format(path)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0]
    return None
