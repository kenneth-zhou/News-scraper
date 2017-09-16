# News-scraper

News scraper that leverages the GDELT Project to download daily news articles released around the world.

Saves individual articles in the form of: title, index number, article url, image url, meta description, and text content.  Also downloads article's associated photo, if any.

Articles are saved as "yyyymmdd" + "index number".  If article has an associated photo, it will be saved with the same name in .jpg.

GDELT Project: releases daily csv files containing links to millions of news articles meant to be representative of day's news.

https://www.gdeltproject.org/data.html
