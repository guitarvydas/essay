import subprocess
import tempfile
import sys
import os

inDirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/test_export/Draft/"

def findlinksFilename (fname):
    ## print(fname, file=sys.stderr)
    p = subprocess.run(["pfr", fname, "findlinks.ohm", "findlinks.action"], capture_output=True, universal_newlines=True)
    return p.stdout

for fname in os.listdir(inDirName):
    r = findlinksFilename (inDirName + "/" + fname)
    print (r)

