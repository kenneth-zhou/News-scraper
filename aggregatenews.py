# -*- coding: utf-8 -*-

# from goose import Goose
import urllib
from multiprocessing import Pool ##parallelization
import itertools ##functions provided allow for efficient looping, allowing for specification of multiple arguments for Pool paralleization
import os
import MySQLdb
import peewee #documentation here: http://docs.peewee-orm.com/en/latest/peewee/example.html
from peewee import *
import geograpy
# import newspaper

def read_url((url, date)): ##accepting first parameter as tuple, because pool() does not accept multiple arguments for functions
    
    #connect to MySQL database on AWS
    db = MySQLDatabase('gdelt', user = 'root', passwd = '***********')

    #model class: database table named crawler
    #field instance: creating columns
    class Crawler(peewee.Model):
        Country = peewee.CharField()
        Title = peewee.TextField()
        Websiteurl = peewee.TextField()
        Date = peewee.DateField()
        Keyword1 = peewee.CharField()
        Keyword2 = peewee.CharField()
        Keyword3 = peewee.CharField()

        class Meta:
            database = db

    db.connect()

    db.create_tables([Crawler], True) # runs SQL CREATE TABLE statement (only has to be run once).  peewee will first check if table has already been created

    ## identifying associated country   
    mentioned_country = str('NA') 
    try:
        places = geograpy.get_place_context(url=url)
        mentioned_country = places.countries[0].encode('utf-8')
    except:
        pass

    ##identifying title and associated keywords
    mentioned_title = str('NA')
    mentioned_keyword1 = str('NA')
    mentioned_keyword2 = str('NA')
    mentioned_keyword3 = str('NA')
    # try:
    #     article = Article(url)
    #     article.download()
    #     article.parse()
    # except Exception:
    #     pass
    # try:
    #     mentioned_title = article.title
    # except Exception:
    #     pass
    # try:
    #     article.nlp()
    #     keywords = article.keywords()
    # except Exception:
    #     pass
    # try:
    #     mentioned_keyword1 = keywords[0]
    # except Exception:
    #     pass
    # try:
    #     mentioned_keyword2 = keywords[1]
    # except Exception:
    #     pass
    # try:
    #     mentioned_keyword3 = keywords[2]
    # except Exception:
    #     pass

    ##inserting into SQL
    if (mentioned_country != 'NA'):
        Crawler.create(Country = mentioned_country, Title = mentioned_title, Websiteurl = url, Date = date, Keyword1 = mentioned_keyword1, Keyword2 = mentioned_keyword2, Keyword3 = mentioned_keyword3)

    db.close()

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

    #converting back to list finallist
    finallist = list()
    for i in uniquewebsiteslist:
        finallist.append(i)

    pool = Pool() #uses all available Cores if set to empty.  specify number of cores as argument if necessary

    pool.map(read_url, itertools.izip(finallist,itertools.repeat(dateoffile)))
    pool.close()
    pool.join()

    return;


def main():

    read_file('20160923')

    return;

if __name__ == '__main__':
    
    main()