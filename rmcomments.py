import subprocess

#https://janakiev.com/blog/python-shell-commands/

testfname="../test_export/Draft/Agile_Takeaways.txt"
print(fname)

def rmComments (fname):
    p = subprocess.run(["parse", fname, "rmcomments.ohm", "rmcomments.glue"], capture_output=True, universal_newlines=True)
    return p.stdout

r = rmComments (testfname)
print (f)
