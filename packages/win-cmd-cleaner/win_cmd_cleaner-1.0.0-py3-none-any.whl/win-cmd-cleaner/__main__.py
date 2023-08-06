import os
import re
import sys

EXTENSIONS = ['.bat', '.btm', '.cmd']

envData = {}
collectedLines = []

def hasData(key):
    return key.lower() in envData

def appendData(key, value):
    if not hasData(key):
        envData[key.lower()] = value

def trimCarat(line):
    trimmedLine = line
    for match in re.findall(r"\^.", trimmedLine):
        trimmedLine = trimmedLine.replace(match, match[1])
    return trimmedLine

def parseData():
    for i in range(len(collectedLines)):
        line = collectedLines[i]
        deobfLine = line
        for match in re.findall(r"\%\w+:~\d+,\d+\%", deobfLine):
            handler = match.strip('%').replace(':~', ',').split(',')
            env = handler[0].lower()
            start = int(handler[1])
            end = start + int(handler[2])
            if hasData(env):
                deobfLine = deobfLine.replace(match, envData[env][start:end] if start < len(deobfLine) and end <= len(deobfLine) else '')
        if deobfLine.lower().strip().startswith('set '):
            index = deobfLine.index('=')
            newKey = deobfLine[4:index].strip()
            if not hasData(newKey):
                newValue = deobfLine[index + 1:len(deobfLine)]
                appendData(newKey, newValue)
        collectedLines[i] = deobfLine

try:
    if len(sys.argv) < 2:
        raise ValueError("Missing command-line argument for file name")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise ValueError(f"File '{filename}' does not exist")
    oldName, ext = os.path.splitext(filename)
    if ext.lower() not in EXTENSIONS:
        raise ValueError(f"File '{filename}' has an invalid extension")
    outFilename = oldName + '_cleaned' + ext
    for k in os.environ:
        appendData(k, os.environ[k])
    deobfLines = []
    with open(filename, 'r') as input:
        for line in input.readlines():
            collectedLines.append(trimCarat(line))
        input.close()
    parseData()
    with open(outFilename, 'w') as output:
        for deobfLine in collectedLines:
            output.write(deobfLine)
        output.flush()
        output.close()
except ValueError as err:
    print(err)
