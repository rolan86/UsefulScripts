import os


INFO = 'C:\Users\HP\Desktop\myout.txt'
INFO_HTML = 'C:\Users\HP\Desktop\myout.html'

fp = open(INFO, 'w')
fp_html = open(INFO_HTML, 'w')
dir_path = raw_input("Enter the directory path: ")
ext = raw_input("Enter the extension to search: ")
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
			fp.write(os.path.join(root, items))
			fp.write('\n')
			html = '<a href="%s">%s</a><br>' %(os.path.join(root, items), os.path.join(root, items))
			fp_html.write(html)
fp_html.write('</body>')
fp_html.close()
fp.close()
