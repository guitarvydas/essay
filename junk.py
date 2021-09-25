import subprocess
import tempfile
import sys
import os
import pipes

t = pipes.Template()
t.append('tr a-z A-Z <junk.txt', 'f-')
# f = t.open('pipefile', 'w')
# f.write('hello world')
# f.close()
print (open('pipefile').read())
