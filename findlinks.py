import subprocess
import tempfile
import sys
import os

dirName="../test_export/Draft"
testfname="../test_export/Draft/Agile_Takeaways.txt"

def findlinksFilename (fname):
    ## print(fname, file=sys.stderr)
    p = subprocess.run(["parse", fname, "findlinks.ohm", "findlinks.action"], capture_output=True, universal_newlines=True)
    return p.stdout

for fname in os.listdir(dirName):
    r = findlinksFilename (dirName + "/" + fname)
    print (r)

