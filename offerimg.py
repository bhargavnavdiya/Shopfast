from bs4 import BeautifulSoup
from selenium import webdriver #Web Drivers Import
from selenium.webdriver.chrome.options import Options

def getOfferImages():
    options=Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver= webdriver.Chrome(chrome_options=options)
    url='https://www.amazon.in/'
    bannerResults=[]
    try:
        driver.get(url)   #Get the url for further
        soup= BeautifulSoup(driver.page_source,'html.parser')
        results=soup.find('div',class_='a-carousel-row-inner')
        bannersdata=results.find('ol', class_='a-carousel').findAll('a',class_='a-link-normal aok-inline-block')
    except:
        bannersdata=()

    if len(bannersdata) >0:
        for bannerData in bannersdata:
            bannerResult=extractBannerData(bannerData)
            bannerResults.append(bannerResult)
    else:
        bannersdata=();
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(bannerResults)
    driver.close()    
    return bannerResults

def extractBannerData(item):
    bannerLink=item.get('href')
    bannerImg=item.find('img').get('src')
    bannerData=('https://www.amazon.in/'+bannerLink,bannerImg)
    return bannerData
getOfferImages()