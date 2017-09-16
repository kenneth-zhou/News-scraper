# News-scraper

News scraper that leverages the GDELT Project to download daily news articles released around the world.  Given the high volume of articles, the news scraper is parallelized across all available cores.

Saves individual articles locally as text files in the form of: title, index number, article url, image url, meta description, and text content.  Also downloads photos in article, if any.

Downloaded articles are titled "yyyymmdd" + "article's index number for that day".  If article has a photo, it will be saved with the same title in .jpg format.

Additional use cases:

trumpclinton: scrape daily articles + article images related to a specific topic.  In this case, I was building a train dataset for a research project at UCLA's Center for Vision Cognition Learning and Autonomy (VCLA) where we wanted to examine ties between article sentiment and image choice (negative/positive face emotion) for trump/clinton. 

aggregatenews: save contents of article, along with target features like mentioned country, to a SQL data table.

masterlistgenerator: generate list of all news websites gathered in GDELT project.

GDELT Project: releases daily csv files containing links to millions of news articles meant to be representative of day's news.

https://www.gdeltproject.org/data.html
