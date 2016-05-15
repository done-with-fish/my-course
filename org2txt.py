import subprocess

def exportOrgFiles(path):
    my_command = "find {} -type f -iname \"*.org\" -print0 | parallel -0 org2txt".format(path)
    process = subprocess.Popen(my_command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0]
    return None

