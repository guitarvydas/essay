import subprocess
import tempfile
import sys
import os
import pipes

#https://janakiev.com/blog/python-shell-commands/

dirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/test_export/Draft/"
testfname="test.txt"
tempfname = "temp.tmp"

def writeTemp (str):
    temp = open (tempfname, "w")
    temp.write (str)
    temp.write ("\n")
    temp.close
    temp.flush ()


def removeCommentsFilename (fname):
    p = subprocess.run(["pfr", fname, "rmcomments.ohm", "rmcomments.action"], capture_output=True, universal_newlines=True)
    return p.stdout

def rmFrontMatterString (str):
    writeTemp (str)
    p = subprocess.run(["pfr", tempfname, "rmFrontMatter.ohm", "rmFrontMatter.action"], capture_output=True, universal_newlines=True)
    return p.stdout

def rmBoilerPlateLinksString (str):
    writeTemp (str)
    p = subprocess.run(["pfr", tempfname, "rmBoilerPlateLinks.ohm", "rmBoilerPlateLinks.action"], capture_output=True, universal_newlines=True)
    return ( p.stdout )

def processEssay (fname):
    print(fname, file=sys.stderr)
    commentsSectionRemoved = removeCommentsFilename (fname)
    frontMatterRemoved = rmFrontMatterString (commentsSectionRemoved)
    boilerPlateRemoved = rmBoilerPlateLinksString (frontMatterRemoved)
    return boilerPlateRemoved

r = processEssay (sys.argv[1])
print (r)


