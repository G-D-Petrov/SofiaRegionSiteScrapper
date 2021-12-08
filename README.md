# Project **Feed Parser**

## Prerequisites 
1. Python 3.8+
2. run: pip install -r requirements.txt in your shell
3. Relies on the **Google API** for sending mails, [read the following for setting up **credentials.json**](https://developers.google.com/gmail/api/guides/sending).

## Flow

### Config
The scrapper tries to scrape the sites defined in *config/sites.json*. \
Each region has corresponding *main_url* and *talks_url*. \
The sript scrapes only the *talks_url*. 

### Parsing
Each region has a separately defined parser, the parsers and a region-parser map are defined **parsers.py**

### Caching
The parsed information is stored in the *cache* folder, in files for each region. \
This is used to store the info if needed for something else. \
Currently, it is only used to determine when we have new posts in the sites. 

**The data in the cache folder should be pushed to git, so mails are not sent unnecessarily.**

### Main business logic
The main script to run the scraper is **main.py**. \
The script parses each site and retrieves the relevant data for each post.\
Currently, this is *only a title, link and date(if available)*.  
Then this data is compared to the cached data for the region and all of the new posts are marked to be send in a mail. \
All of the data is then cached.

If there are any new posts, they are send as a mail to a receiving address (passed as argument).

### Mails
The logic for the mails is specified in **mails.py**. \
The templates in the *templates* folder are used to format the mail that is to be sent. \
For ths mailing to work a **credentials.json** is needed. \
And Oath needs to be performed (which will be cached as **token.pickle** file) \
Both the credentials.json and token.pickle are in the .gitignore so as to not be pushed in the git by mistake.

For more info on the Google API and its Oath, [please check here](https://developers.google.com/gmail/api/guides).

## Regions that are not supported
The following regions are currently not supported:
- Serdika - No site found
- Slatina - Site doesn't support crawling
- Vitosha - Site doessn't support crawling
- Vrabnitsa - No site found
- Kremikovci - No site found

It looks llike most of them are covered by the main site for [Sofia](https://www.sofia.bg/en/public-discussions).
