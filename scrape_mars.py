# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json

#Set up splinter for scraping
def scrape_info(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
   
#MARS NEWS SCRAPE
mars_info = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_="content_title").text
    print(news_title)
    news_p = soup.find('div', class_='article_teaser_body').text
    print(news_p)

    mars_info["news_p"]=news_p
    mars_info["news_title"]=news_title
    mars_info["featured_image"]= mars_img(browser)
    mars_info["mars_facts"]= mars_facts()
    mars_info["mars_hemispheres"]= mars_hemispheres)browser
    
    browser.quit()

return mars_info
    
#MARS IMAGES SCRAPE

def mars_image(browser):

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)

    html_img = browser.html
    soup = BeautifulSoup(html_img, 'html.parser')

    image = soup.find('div', class_'floating_text_area')
    link = image.find("a")['href']

    main_url = 'https://spaceimages-mars.com/'

    featured_image_url = main_url + link       
    
    return main_url

    browser.quit()

#MARS FACTS SCRAPE
def mars_facts():    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    table = pd.read_html(facts_url)
    facts_df=table[0]
    facts_df.columns = ['Description','Mars','Earth']
    facts_df=facts_df.set_index('Description', inplace=True)
    facts_df=facts_df.drop(["Mars - Earth Comparison"])   
    facts_html = facts_df.to_html()
    facts_html.replace('\n', '')
    browser.quit()

    return facts_html

#MARS HEMISPHERES SCRAPE
def mars_hemispheres(browser):  
    mars_hemispheres_url = ("https://marshemispheres.com/")
    browser.visit(hemisphere_image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    
    for item in items:
            title = item.find('h3').text
            hemisphere_image_url = 'https://marshemispheres.com/' + item.find('a', class_='itemLink product-item')['href']

            browser.visit(hemispheres_url)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            hemisphere_image_url = 'https://marshemispheres.com/' + soup.find('img', class_='wide-image')['src']
            hemisphere_image_urls.append({'title': title, 'img_url': hemisphere_image_url})
        return hemisphere_image_urls

if __name__ == "__main__":
    print(init_browser())



