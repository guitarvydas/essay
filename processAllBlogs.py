import subprocess
import tempfile
import sys
import os
import pipes

dirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/test_export/Draft/"

for fname in os.listdir(dirName):
    fullname = dirName + fname
    r = processEssay (fullname)
    print (fullname)
