import re
import os.path, time
from os import listdir
from os.path import isfile, join


def get_files(path):
	files = [f for f in listdir(path) if isfile(join(path, f))]
	return files

# -----------------------------------------------------------------------------
# list files in current directory
# -----------------------------------------------------------------------------
path = "./"
onlyfiles = get_files(path)
for filename in onlyfiles:
	print '{} created: {}'.format(filename, time.ctime(os.path.getctime(filename)))

# print(onlyfiles)




# print(entries)

# print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
# print("Created: %s" % time.ctime(os.path.getctime("test.txt")))




# mac_re = '([a-fA-F0-9]{2}[:|\-]?){6}' # this is the regex for mac addreses

# entries = []

# f = open("test.txt","r") #opens file with name of "test.txt"

# print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
# print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

# for line in f:

#     entries.append(line)

# print(entries)


# for s in entries:
#     a = re.compile(mac_re).search(s)
#     if a:
#         print s[a.start(): a.end()]



