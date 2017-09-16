# -*- coding: utf-8 -*-

from goose import Goose
import urllib
from multiprocessing import Pool ##parallelization
import itertools ##functions provided allow for efficient looping, allowing for specification of multiple arguments for Pool paralleization
import os

def read_url((url, websiteslist, date)): ##accepting first parameter as tuple, because pool() does not accept multiple arguments for functions
	#tying website url to original GDELT csv file id number
	id = 1
	for i in websiteslist:
		if i == url:
			break
		id = id + 1

	idnumber = str(id).zfill(6)

	filename = date + idnumber
	imagefilename = filename + ".jpg"

	file = open(os.path.join(date,filename), 'w')
	g = Goose()
	try:
		article = g.extract(url=url)
	except:
		pass
	try:
		file.write("TITLE|" + article.title.encode('utf-8') + "\n")
	except:
		pass
	try:
		file.write("INDEX NUMBER|" + idnumber + "\n")
		file.write("ARTICLE_URL|" + url + "\n")
	except:
		pass
	try:
		file.write("IMAGE_URL|" + article.top_image.src.encode('utf-8') + "\n")
	except:
		pass
	try:
		file.write("META_DESCRIPTION|" + article.meta_description.encode('utf-8') + "\n")
	except:
		pass
	try: 
		file.write("CONTENT|" + article.cleaned_text.encode('utf-8') + "\n")
	except:
		pass
	try:
		urllib.urlretrieve(article.top_image.src, os.path.join(date,imagefilename))
	except:
		pass
	file.close()

	return;

def read_file(date):
	filelocation = "http://data.gdeltproject.org/events/" + str(date) + ".export.CSV.zip"
	zipfilename = str(date) + ".export.CSV"
	from StringIO import StringIO
	from zipfile import ZipFile
	from urllib2 import urlopen

	url = urlopen(filelocation)
	zipfile = ZipFile(StringIO(url.read()))
	lines = zipfile.open(zipfilename).readlines()
	dateoffile = date

	websiteslist = list()

	for i,l in enumerate(lines):
		lineelements = l.split("\t")
		websiteurl = lineelements[-1]
		websiteurl = websiteurl.strip()
		websiteslist.append(websiteurl)

	uniquewebsiteslist = set(websiteslist) #removing non-unique options

	#converting back to list object
	finallist = list()
	for i in uniquewebsiteslist:
		finallist.append(i)

	os.makedirs(date)

	pool = Pool() #uses all available Cores if set to empty.  specify number of cores as argument if necessary

	pool.map(read_url, itertools.izip(finallist,itertools.repeat(websiteslist),itertools.repeat(dateoffile)))
	pool.close()
	pool.join()

	return;

def main():
	##testing on sample file
	read_file('20160922')
	read_file('20160923')

	return;

if __name__ == '__main__':
	main()



