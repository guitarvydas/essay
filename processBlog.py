import subprocess
import tempfile
import sys
import os

#https://janakiev.com/blog/python-shell-commands/

testfname="test.txt"
tempfname = "temp.tmp"

def writeTemp (str):
    temp = open (tempfname, "w")
    temp.write (str)
    temp.write ("\n")
    temp.close
    temp.flush ()


def removeCommentsFilename (fname):
    p = subprocess.run(["parse", fname, "rmcomments.ohm", "rmcomments.action"], capture_output=True, universal_newlines=True)
    return p.stdout

def rmFrontMatterString (str):
    writeTemp (str)
    p = subprocess.run(["parse", tempfname, "rmFrontMatter.ohm", "rmFrontMatter.action"], capture_output=True, universal_newlines=True)
    return p.stdout

def rmBoilerPlateLinksString (str):
    writeTemp (str)
    p = subprocess.run(["parse", tempfname, "rmBoilerPlateLinks.ohm", "rmBoilerPlateLinks.action"], capture_output=True, universal_newlines=True)
    return p.stdout

def processEssay (fname):
    print(fname, file=sys.stderr)
    commentsSectionRemoved = removeCommentsFilename (fname)
    frontMatterRemoved = rmFrontMatterString (commentsSectionRemoved)
    boilerPlateRemoved = rmBoilerPlateLinksString (frontMatterRemoved)
    return boilerPlateRemoved

r = processEssay (testfname)
print (r)

