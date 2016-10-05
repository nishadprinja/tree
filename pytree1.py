import os
import sys

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '--' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '--' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if len(sys.argv) == 1:
    list_files('.')
    #print('%d directories, %d files' % (cnt["dirs"], cnt["files"]))
# run tree on a specified directory
elif len(sys.argv) == 2:
    #print(sys.argv[1])
    list_files(sys.argv[1])
    #print('%d directories, %d files' % (cnt["dirs"], cnt["files"]))
else:
    print('Error! Please enter a valid path.')