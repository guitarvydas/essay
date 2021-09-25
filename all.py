import subprocess
import tempfile
import sys
import os
import pipes

inDirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/test_export/Draft/"
outDirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/culled/"

def process1 (fname):
    result = subprocess.run (['python', 'processBlog.py', fname], stdout=subprocess.PIPE);
    # print ( (result.stdout).decode ('utf-8') )
    return  (result.stdout).decode ('utf-8')


for fname in os.listdir(inDirName):
    inFullname = inDirName + fname
    r = process1 ( inFullname )
    outFullName = outDirName + fname
    f = open (outFullName, "w")
    f.write (r)
    f.close ()
