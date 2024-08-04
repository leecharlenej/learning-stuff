# To play with XPaths: https://scrapinghub.github.io/xpath-playground/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Headless mode
from selenium.webdriver.chrome.options import Options

website = "https://www.thesun.co.uk/sport/football"
path = "C:\\Users\\leech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Headless mode
options = Options()
# options.headless = True # Not working
options.add_argument("--headless=new")

service = Service(executable_path = path)
# driver = webdriver.Chrome(service = service)
driver = webdriver.Chrome(service = service, options = options)
driver.get(website)

# find_elements = Find all elements and return a list.
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles, subtitles, links = [], [], []

for container in containers:

    try:
        title = container.find_element(by="xpath", value='./a/span').text
        subtitle = container.find_element(by="xpath", value='./a/h3').text
        link = container.find_element(by="xpath", value='./a').get_attribute('href')

        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

    except Exception as e:
        continue


my_dict = {'title': titles,
           'subtitle': subtitles,
           'link': links}

df_headlines = pd.DataFrame(my_dict)
# df_headlines.to_csv('headlines.csv')
df_headlines.to_csv('headlines-headless.csv')

driver.quit()