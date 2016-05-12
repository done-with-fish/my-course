import subprocess, glob, os, sys

def findOrgFiles(path):
    os.chdir(path)
    file_paths = [path+x for x in glob.glob("*.org")]
    return file_paths

def makeCommand(l):
    s = 'parallel org2txt ::: '
    for x in l:
        s += x + ' '
    return s

def runBashCommand(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return None

def exportOrgFiles(path):
    list_of_files = findOrgFiles(path)
    command       = makeCommand(list_of_files)
    runBashCommand(command)
    return None

exportOrgFiles(sys.argv[1])
