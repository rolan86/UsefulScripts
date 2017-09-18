import os
import csv
import requests
import sqlite3

from bs4 import BeautifulSoup


def generate_csv(gendict):
	with open('result.csv','w') as csvfile:
		c = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		c.writerow(['extension', 'count', 'format', 'description', 'type', 'category'])
		for key, value in gendict.iteritems():
			#info = get_fileinfo(key)
			info = file_search(key)
			result = [key,value]+list(info)
			c.writerow(result)		
			
def generate_dict(fpath):
	ext_dict = {}
	for root, dirs, files in os.walk(fpath):
		for name in files:
			try:
				ext_dict[name.split('.')[-1]] = ext_dict.get(name.split('.')[-1], 0)+1
			except:
				print "No extension found"
	return ext_dict

def get_fileinfo(extension):
	base_url = "https://fileinfo.com/extension/{0}"
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	url = base_url.format(extension)
	req = requests.get(url, headers=headers)
	if req.status_code == 200:
		soup = BeautifulSoup(req.text)
		description = [soup.find('span', {'itemprop':'name'}).text]
		category = [items.text for items in \
					soup.find('table', {'class':'headerInfo'})\
					.findAll('a')[:2]]
		return description+category
	else:
		return [str(req.status_code) + " Error Code", None, None]
		
def get_conn():
	try:
		conn = sqlite3.connect('finfo_v_miss')
		return conn
	except Exception as e:
		return e
		
def get_conn2():
	try:
		conn = sqlite3.connect('finfo_v2')
		return conn
	except Exception as e:
		return e
		
def file_search(ext):
	conn = get_conn2()
	c = conn.cursor()
	query = "SELECT * from finfo_v2 WHERE extension LIKE '{0}'".format(ext.upper())
	c.execute(query)
	output = c.fetchall()
	#line = ['','','','']
	line = None
	for line in output:
		print line
	conn.close()
	if line == None:
		conn = get_conn()
		c = conn.cursor()
		query = "SELECT * from finfo_v_miss WHERE extension LIKE '{0}'".format(ext.upper())
		c.execute(query)
		output = c.fetchall()
		for line in output:
			print line
		if line == None:
			line = ['','','','']
		conn.close()
	return line
	
if __name__ == '__main__':
	source = raw_input("Enter source code path: ")
	gdict = generate_dict(source)
	generate_csv(gdict)
