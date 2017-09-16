# -*- coding: utf-8 -*-

## updates made:
## 1) Storing all URLs in a list, using set() to only keep unique urls, before running read_url() function on said list

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

	masterlist = list()
	for i,l in enumerate(lines):
		lineelements = l.split("\t")
		websiteurl = lineelements[-1]
		websiteurl = websiteurl.strip() ##removes any trailing blank spaces
		websiteurl = websiteurl.split('/')[2] ##saves just the main website URl
		masterlist.append(websiteurl + "\n") ##append websiteurl to masterlist

	# ###toggle if writing to masterlist for the first time
	# masterlist = set(masterlist)
	# file = open('masterlist.txt', 'w')
	# for i in masterlist:
	# 	file.write(i)
	# file.close()

	# ##toggle if adding URLs to masterlist
	file = open('masterlist.txt','r')
	lines = file.readlines()
	for i in lines:
			masterlist.append(i)
	masterlist = set(masterlist) #removing non-unique options
	file.close()
	file = open('masterlist.txt','w')
	for i in masterlist: 
		file.write(i)
	file.close()

def main():
	##testing on sample file
	# read_file('20160720')
	# read_file('20160721')
	# read_file('20160722')
	# read_file('20160723')
	# read_file('20160724')
	# read_file('20160725')
	# read_file('20160726')
	read_file('20160727')
	read_file('20160728')
	read_file('20160729')
	read_file('20160730')
	read_file('20160731')
	read_file('20160801')
	read_file('20160802')

if __name__ == '__main__':
	main()



