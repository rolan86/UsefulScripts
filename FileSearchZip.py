import os
import zipfile

UNZIP_DIR = "unzip_dir"
INFO = 'C:\Users\HP\Desktop\myout.txt'
INFO_HTML = 'C:\Users\HP\Desktop\myout.html'

def unzip_file(zipped, ext):
	if not os.path.exists(UNZIP_DIR):
		os.mkdir(UNZIP_DIR)
	if zipfile.is_zipfile(zipped):
		print "Unzipping: ", zipped
		zipstrip = os.path.split(zipped)[1].strip(ext)
		uabs = os.path.abspath(UNZIP_DIR)
		os.mkdir(os.path.join(uabs, zipstrip))
		sub_unzip_dir = os.path.join(os.path.abspath(UNZIP_DIR), zipstrip)
		zip_ref = zipfile.ZipFile(zipped, 'r')
		zip_ref.extractall(sub_unzip_dir)
		zip_ref.close()	

fp = open(INFO, 'w')
fp_html = open(INFO_HTML, 'w')
dir_path = raw_input("Enter the directory path: ")
ext = raw_input("Enter the extension to search: ")
option = """If it is a jar or zip extension, 
do you want to unzip the file (Enter y for yes and n for no): """
uzip = raw_input(option)
html = """<html>
			<head>
				<title>My Results</title>
			</head>
			<body>
"""
fp_html.write(html)
for root, dir, files in os.walk(dir_path):
	for items in files:
		if items.endswith(ext):
			print os.path.join(root, items)
			if uzip == 'y':
				unzip_file(os.path.join(root, items), ext)
			fp.write(os.path.join(root, items))
			fp.write('\n')
			html = '<a href="%s">%s</a><br>' %(os.path.join(root, items), os.path.join(root, items))
			fp_html.write(html)
fp_html.write('</body>')
fp_html.close()
fp.close()
