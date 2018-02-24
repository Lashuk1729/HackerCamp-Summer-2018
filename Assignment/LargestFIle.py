import heapq
import os, os.path
import sys
import operator

def convert_bytes(num):
    # This function will convert bytes to MB.... GB... etc
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_sizes(directory):
    # Walk the tree
    for dirpath, dirnames, files in os.walk(directory):
        # os.walk without hidden folders
        files = [f for f in files if not f[0] == '.']
        dirnames[:] = [d for d in dirnames if not d[0] == '.']
        for name in files:
            full_path = os.path.join(dirpath, name)
            yield full_path, os.path.getsize(full_path)

directory = sys.argv[1]
num_files = 10

big_files = heapq.nlargest(num_files, file_sizes(directory), key=operator.itemgetter(1))
for b in big_files:
	print("Name and location of the file: ",b[0])
	print("Size of the file: ", convert_bytes(b[1]),"\n")