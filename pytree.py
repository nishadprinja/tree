#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import re


# YOUR CODE GOES here

link1 = '└── '
link2 = '├── '
pad1 = '    '
pad2 = '│   '

# reference: http://stackoverflow.com/questions/30743367/how-to-retain-only-letter-digit-space-using-at-most-re-module
def char_fix(text):
	return re.sub('[^A-Za-z0-9\s]+', '', text).lower()

def tree(path, cnt, pad=''):
	files = []
	dirList = os.listdir(path)

	# avoid hidden files, ref: http://stackoverflow.com/questions/7099290/how-to-ignore-hidden-files-using-os-listdir
	for file in dirList:
		if(not file.startswith(".")):
			files.append(file)

	# reference: https://docs.python.org/3/howto/sorting.html
	files = sorted(files, key=char_fix)
	length = 0

	for eachFile in files:
		# reference: https://docs.python.org/2/library/os.path.html
		child = os.path.join(path, eachFile)

		length = length + 1

		# print the files in a directory
		if length == len(files):
			print(pad + link1 + eachFile)
		else:
			print(pad + link2 + eachFile)

	# for directories, print files within them
	if os.path.isdir(child):
		cnt["dirs"] = cnt["dirs"] + 1
		if length == len(files):
			tree(child, cnt, pad + pad1)
		else:
			tree(child, cnt, pad + pad2)
	else:
		cnt["files"] = cnt["files"] + 1

cnt = {"files": 0, "dirs": 0}

# run tree on current directory
if len(sys.argv) == 1:
    tree('.', cnt)
    print('%d directories, %d files' % (cnt["dirs"], cnt["files"]))
# run tree on a specified directory
elif len(sys.argv) == 2:
    print(sys.argv[1])
    tree(sys.argv[1], cnt)
    print('%d directories, %d files' % (cnt["dirs"], cnt["files"]))
else:
    print('Error! Please enter a valid path.')
