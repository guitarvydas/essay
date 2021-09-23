import os

dir = "../test_export/Draft"
for file in os.listdir(dir):
    orig = dir + "/" + file
    renamed = dir + "/" + file.replace (" ", "_")
    # print(orig)
    # print(renamed)
    os.rename(orig,renamed)
