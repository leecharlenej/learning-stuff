# To play with XPaths: https://scrapinghub.github.io/xpath-playground/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

website = "https://www.thesun.co.uk/sport/football"
path = "C:\\Users\\leech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(website)

# from selenium import webdriver
# import pandas as pd

# # To open the website
# url = "https://www.thesun.co.uk/sport/football"
# driver = webdriver.Chrome()
# driver.get(url)

# Getting elements with Browser > Inspect > Right Click > Inspect
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles, subtitles, links = [], [], []

for container in containers:
    try:
        title = container.find_element(by="xpath", value='.//a/span').text
    except Exception as e:
        print(f"Title not found in container: {e}")
        title = None
    try:
        subtitle = container.find_element(by="xpath", value='.//a/h3').text
    except Exception as e:
        print(f"Subtitle not found in container: {e}")
        subtitle = None
    try:
        link = container.find_element(by="xpath", value='.//a').get_attribute('href')
    except Exception as e:
        print(f"Link not found in container: {e}")
        link = None

my_dict = {'titles': titles,
           'subtitles': subtitles,
           'links': links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headlines.csv')

driver.quit()
