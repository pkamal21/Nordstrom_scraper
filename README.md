# Nordstrom_scraper
<h1>A python script to scrape Nordstrom website.</h1>

Technologies used:
<ol> 
<li>Python</li>
<li>Selenium</li>
<li>Pandas</li>
</ol>

We use selenium webdriver to interact with a javascript content based websites which can't be scraped like regular websites using BeautifulSoup and Requests.<br>
For selenium to work, first we have to install geckodriver combatible with the browser going to be used for scraping.   <em>Geckodriver</em> directory should be mentioned in the script.
I am using Geckodriver for firefox and windows64.
Then after analyzing the website for prices, colors, sizes

The copied XPATHs, using the developer tools and inspect in the browser are usd to select the specific tags and sections of html rendered.
the driver function find_element_by_xpath is used to select the particular tags. The method get_attribute is used to get the values in the tags.<br><br>
Pandas is used to convert the values scraped into a readable format which is easy to analyze, visualize and work on.
