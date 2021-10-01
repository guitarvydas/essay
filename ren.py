import subprocess
import tempfile
import sys
import os
import pipes

inDirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/test_export/Draft/"
outDirName="/Users/tarvydas/Desktop/book_manuscripts/takeaways/culled/"

for fname in os.listdir(inDirName):
    outFullName = outDirName + fname
    base = os.path.splitext (outFullName)[0]
    os.rename (outFullName, base + ".md")
    # print (base + ".md")    
