import os
import shutil


SOURCEFILE = "C:\\Users\\HP\\Desktop\\sfile.txt"
SOURCEDIR = "C:\\Users\\HP\\Desktop\\SourceDir"
DESTDIR = "C:\\Users\\HP\\Desktop\\DestDir"

all_files = [os.path.join(SOURCEDIR, items) for items in os.listdir(SOURCEDIR)]
if not os.path.exists(DESTDIR):
	os.mkdir(DESTDIR)

with open(SOURCEFILE, 'r') as src_file:
	for files in src_file:
		files = files.strip('\n')
		if files in all_files:
			splitfile = os.path.split(files)[1]
			destfile = os.path.join(DESTDIR, splitfile)
			shutil.copyfile(files, destfile)
			