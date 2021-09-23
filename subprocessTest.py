import subprocess
p = subprocess.run(["ls", "-l", "/dev/null"], capture_output=True, universal_newlines=True)
print(p.stdout)
