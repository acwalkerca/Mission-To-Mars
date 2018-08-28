from splinter import Browser
from bs4 import BeautifulSoup as bs


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    mars_data = {}

    ###NASA Mars News
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")
    
    #Find latest news article and text
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").text

    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p
    
    ###JPL Mars Space Images - Featured Image
    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    html = browser.html
    soup = bs(html, "html.parser")
    
    article = soup.find('article')
    img_url = article.find('figure', 'lede').a['href']
    base_url = 'www.jpl.nasa.gov'
    featured_img_url = base_url + img_url
    
    mars_data["featured_img_url"] = featured_img_url
    
    ###Mars Data
    browser = init_browser()
    
    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    # Target User
    target_user = "MarsWxReport"

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user)

    #Most Recent Tweet
    mars_weather = public_tweets[0]["text"]
    
    mars_data["mars_weather"] = mars_weather
    
    ###Mars Facts
    browser = init_browser()
    url = "http://space-facts.com/mars/"
    
    #Read the url with Pandas
    tables = pd.read_html(url)

    #Create DataFrame
    df = tables[0]

    #Name Columns
    df.columns = ["Data", "Values"]

    #Set Index
    df.set_index("Data")

    #Transfer info to HTML File
    html_table = df.to_html()
    html_table.replace('\n', '')
    
    mars_data["html_table"] = html_table
    
    ###Mars Hemispheres
    
    hemisphere_image_urls = []
    
    #Cerberus Hemisphere Enhanced
    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #Navigate to Cerberus Hemisphere
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    #Retreive data from url
    html = browser.html

    #Create Beautiful Soup object
    soup = bs(html, 'html.parser')

    #Locate Cerberus Link
    cerberus_link = soup.find('div', 'downloads').a['href']

    #Create Dictionary
    cerberus = {'title' : 'Cerberus Hemisphere', 'img_url' : cerberus_link}

    #Append Dictionary to Hemisphere List
    hemisphere_image_urls.append(cerberus)
    
    #Schiaparelli Hemisphere Enhanced
    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    #Navigate to Schiaparelli Hemisphere
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    #Retreive data from url
    html = browser.html

    #Create Beautiful Soup object
    soup = bs(html, 'html.parser')

    #Locate Schiaparelli Link
    schiaparelli_link = soup.find('div', 'downloads').a['href']
    
    #Create Dictionary
    schiaparelli = {'title' : 'Schiaparelli Hemisphere', 'img_url' : schiaparelli_link}

    #Append Dictionary to Hemisphere List
    hemisphere_image_urls.append(schiaparelli)
    
    #Syrtis Major Hemisphere Enhanced
    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    #Navigate to Syrtis Major Hemisphere
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    #Retreive data from url
    html = browser.html

    #Create Beautiful Soup object
    soup = bs(html, 'html.parser')

    #Locate Syrtis Major Link
    syrtis_major_link = soup.find('div', 'downloads').a['href']

    #Create Dictionary
    syrtis_major = {'title' : 'Syrtis Major Hemisphere', 'img_url' : syrtis_major_link}

    #Append Dictionary to Hemisphere List
    hemisphere_image_urls.append(syrtis_major) 
    
    #Valles Marineris Hemisphere Enhanced
    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    #Navigate to Valles Marineris Hemisphere
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    #Retreive data from url
    html = browser.html

    #Create Beautiful Soup object
    soup = bs(html, 'html.parser')

    #Locate Valles Marineris Link
    valles_marineris_link = soup.find('div', 'downloads').a['href']

    #Create Dictionary
    valles_marineris = {'title' : 'Valles Marineris Hemisphere', 'img_url' : valles_marineris_link}

    #Append Dictionary to Hemisphere List
    hemisphere_image_urls.append(valles_marineris)
    
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    
    return mars_data
