import subprocess
import tempfile
import sys
import os
import pipes

dirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/test_export/Draft/"

def process1 (fname):
    result = subprocess.run (['python', 'processBlog.py', fname], stdout=subprocess.PIPE);
    print ( (result.stdout).decode ('utf-8') )

process1 (dirName + 'Agile_Takeaways.txt')

# for fname in os.listdir(dirName):
#     fullname = dirName + fname
#     r = processEssay (fullname)
#     print (fullname)
