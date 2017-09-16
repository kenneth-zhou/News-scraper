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

	#creating unicode strings to check for
	trump = u"trump"
	Trump = u"Trump"
	clinton = u"clinton"
	Clinton = u"Clinton"

	idnumber = str(id).zfill(6)

	filename = date + idnumber
	imagefilename = filename + ".jpg"

	#test if mentions trump or clinton
	g = Goose()
	try:
		article = g.extract(url=url)
	except:
		pass
	try:
		if not ((trump in article.cleaned_text) or (Trump in article.cleaned_text) or (clinton in article.cleaned_text) or (Clinton in article.cleaned_text)):
			return
	except:
		return

	#if contains trump or clinton, write to file
	file = open(os.path.join(date,filename), 'w')
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
		# urllib.urlretrieve(article.top_image.src, os.path.join(date,imagefilename))
		os.system("wget -O {0} {1}".format(os.path.join(date,imagefilename), article.top_image.src))
	except:
		pass
	file.close()

	return;

def read_file(date):
	filelocation = "http://data.gdeltproject.org/gdeltv2/" + str(date) + ".mentions.CSV.zip"
	zipfilename = str(date) + ".mentions.CSV"
	from StringIO import StringIO
	from zipfile import ZipFile
	from urllib2 import urlopen

	print "now attempting to access GDELT file " + str(date)

	url = urlopen(filelocation, timeout = 5)
	zipfile = ZipFile(StringIO(url.read()))
	lines = zipfile.open(zipfilename).readlines()
	dateoffile = date


	print "accessed GDELT file " + str(date)

	websiteslist = list()

	for i,l in enumerate(lines):
		lineelements = l.split("\t")
		websiteurl = lineelements[5]
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

	#done: 20160101000000
	#done: 20160201000000
	#done: 20160301000000
	#done: 20160401000000
	#done: 20160501000000
	#done: 20160601000000
	#done: 20160701000000
	#done: 20160801000000
	#done: 20160901000000
	# read_file('20160115000000')
	# read_file('20160215000000')
	# read_file('20160315000000')
	# read_file('20160415000000')
	# read_file('20160515000000')
	# read_file('20160615000000')
	# read_file('20160715000000')
	# read_file('20160815000000')
	# read_file('20160915000000')
	# read_file('20161019001500')
	# read_file('20161019003000')
	# read_file('20161019004500')
	# read_file('20161019010000')
	# read_file('20161019011500')
	# read_file('20161019013000')
	# read_file('20161019014500')
	# read_file('20161019020000')
	# read_file('20161019021500')
	# read_file('20161019023000')
	# read_file('20161019024500')
	# read_file('20161019030000')
	# read_file('20161019031500')
	# read_file('20161019033000')
	# read_file('20161019034500')
	# read_file('20161019040000')
	# read_file('20161019041500')
	# read_file('20161019043000')
	# read_file('20161019044500')
	# read_file('20161019050000')
	# read_file('20161019051500')
	# read_file('20161019053000')
	# read_file('20161019054500')
	# read_file('20161019060000')
	# read_file('20161019061500')
	# read_file('20161019063000')
	# read_file('20161019064500')
	# read_file('20161019070000')
	# read_file('20161019071500')
	# read_file('20161019073000')
	# read_file('20161019074500')
	# read_file('20161019080000')
	# read_file('20161019081500')
	# read_file('20161019083000')
	# read_file('20161019084500')
	# read_file('20161019090000')
	# read_file('20161019091500')
	# read_file('20161019093000')
	# read_file('20161019094500')
	# read_file('20161019100000')
	# read_file('20161019101500')
	# read_file('20161019103000')
	# read_file('20161019104500')
	# read_file('20161019110000')
	# read_file('20161019111500')
	# read_file('20161019113000')
	# read_file('20161019114500')
	# read_file('20161019120000')
	# read_file('20161019121500')
	# read_file('20161019123000')
	# read_file('20161019124500')
	# read_file('20161019130000')

	# read_file('20161019131500')
	# read_file('20161019133000')
	# read_file('20161019134500')
	# read_file('20161019140000')
	# read_file('20161019141500')
	# read_file('20161019143000')
	# read_file('20161019144500')
	# read_file('20161019150000')
	# read_file('20161019151500')
	# read_file('20161019153000')
	# read_file('20161019154500')
	# read_file('20161019160000')
	# read_file('20161019161500')
	# read_file('20161019163000')
	# read_file('20161019164500')
	# read_file('20161019170000')
	# read_file('20161019171500')
	# read_file('20161019173000')
	# read_file('20161019174500')
	# read_file('20161019180000')
	# read_file('20161019181500')
	# read_file('20161019183000')
	# read_file('20161019184500')
	# read_file('20161019190000')
	# read_file('20161019191500')
	# read_file('20161019193000')
	# read_file('20161019194500')
	# read_file('20161019200000')
	# read_file('20161019201500')
	# read_file('20161019203000')
	# read_file('20161019204500')
	# read_file('20161019210000')
	# read_file('20161019211500')
	# read_file('20161019213000')
	# read_file('20161019214500')
	# read_file('20161019220000')
	# read_file('20161019221500')
	read_file('20161019223000')
	# read_file('20161019224500')
	# read_file('20161019230000')
	# read_file('20161019231500')
	# read_file('20161019233000')
	# read_file('20161019234500')

	# read_file('20161020000000')

	return;

if __name__ == '__main__':
	main()