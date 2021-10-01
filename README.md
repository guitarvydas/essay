process blog .md files for creating a book

all.py calls processBlog.py to:
- remove front matter
- remove boiler plate links (References and Table of Contents)
- remove comments section

findlinks.py prints all non-boilerplate links

see test.bash
