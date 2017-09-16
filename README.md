# News-scraper

News scraper that leverages the GDELT Project to download daily news articles released around the world.  Given the high volume of daily news articles, the news scraper is parallelized.

Saves individual articles locally as text files in the form of: title, index number, article url, image url, meta description, and text content.  Also downloads photos in article, if any.

Downloaded articles are titled "yyyymmdd" + "article's index number for that day".  If article has a photo, it will be saved with the same title in jpg format.

GDELT Project: releases daily csv files containing links to millions of news articles meant to be representative of day's news.

https://www.gdeltproject.org/data.html
