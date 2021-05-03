from django.shortcuts import render
from .models import uppdernavimages
# import shopping_scraper
from django.contrib import messages
from bs4 import BeautifulSoup
from selenium import webdriver #Web Drivers Import
from selenium.webdriver.chrome.options import Options
import csv 
import offerimg
from .forms import contactUs, feedbackForm

# Create your views here.

def shopfasthome(request):
    
    offerimages=offerimg.getOfferImages()
    if len(offerimages)==0:
        offerimages= uppdernavimages.objects.all()
    if request.method=='POST':
        searchText=request.POST['search_box']
        #print("THis is print" + searchText)
        SearchRecords=SearchTerm(searchText)
        # SearchRecords.sort(key=lambda x:x[2])
        return render(request,'index.html',{'offerimages':offerimages,'SearchRecords':SearchRecords})
    else:
        SearchRecords=[]
    
    return render(request,'index.html',{'offerimages':offerimages})



    

def get_url(search_term):
    template_url='https://www.google.com/search?tbm=shop&sxsrf=ALeKk02xlZ4o6-7063SZJgdAtkGiQMH-Tg%3A1613122348676&ei=LEsmYNjYKPzUrtoPiOu26AM&q={}&oq={}&gs_lcp=Cgtwcm9kdWN0cy1jYxADUKuZDVjlpA1gj6cNaABwAHgAgAEAiAEAkgEAmAEAoAEBqgEPcHJvZHVjdHMtY2Mtd2l6wAEB&sclient=products-cc&ved=0ahUKEwjYnsmEheTuAhV8qksFHYi1DT0Q4dUDCAs&uact=5'
    search_term=search_term.replace(' ','+')
    return template_url.format(search_term,search_term)

#Function to define each items of product
def extract_results(item):
# item=results[0]
    itemTag=item.find('h3').text
    # print(itemTag)
    # try:
    #     # itemPrice=item.find('span',class_="QIrs8").span.text #item.find('span').span.span.text
    #     # print(itemPrice)
    #     # itemPrice=item.find('div',{'data-sh-or':'price'}).div.span.span.span.text
    #     itemPrice=item.find('spna',class_="a8Pemb").text
    #     # itemBrand=item.find(class_='shntl hy2WroIfzrX__merchant-name').text
    #     itemBrand=item.find('div',class_="b07ME mqQL1e").span.text
    #     # print(itemBrand)
    #     # itemWebLink= 'https://www.google.com'+item.find(class_='shntl hy2WroIfzrX__merchant-name').get('href')
    #     itemWebLink='https://www.google.com'+item.find('a',class_="VZTCjd translate-content").get('href')  
    #     # print(itemWebLink)
    #     # itemImageLink=item.find('img',class_='TL92Hc').get('src')#.find('div',class_='JRlvE XNeeld')
    #     itemImageLink=item.find('div',class_="JRlvE XNeeld").img.get('src')
    #     # itemImageLink=imageLink['src']
    #     # print(itemImageLink)
    # except:
        # itemPrice="Not Available"
        # itemBrand="Brand Not defined"
        # itemWebLink="No link Available"
        # itemImageLink="No Image Available"
        # exit();
    try:
         # itemPrice=item.find('span',class_="QIrs8").span.text #item.find('span').span.span.text
        # print(itemPrice)
        # itemPrice=item.find('div',{'data-sh-or':'price'}).div.span.span.span.text
        itemPrice=item.find('span',class_="a8Pemb").text
    except:
        itemPrice="Not Available"
    

    try:
        # itemBrand=item.find(class_='shntl hy2WroIfzrX__merchant-name').text
        itemBrand=item.find('div',class_="b07ME mqQL1e").span.text
        # print(itemBrand)
    except:
        itemBrand="Brand Not defined"

    try:
        # itemWebLink= 'https://www.google.com'+item.find(class_='shntl hy2WroIfzrX__merchant-name').get('href')
        itemWebLink='https://www.google.com'+item.find('a',class_="VZTCjd translate-content").get('href')  
        # print(itemWebLink)
    except:
        itemWebLink="No link Available"

    try:
        itemImageLink=item.find('img',class_="TL92Hc").get('src')#.find('div',class_='JRlvE XNeeld')
        # itemImageLink=item.find('div',class_="JRlvE XNeeld").img.get('src')
        # itemImageLink=imageLink['src']
        # print(itemImageLink)
    except:
        itemImageLink="No Image Available"


    try:
        itemRating=item.find('div',{'role':'tree'}).get('aria-label')
        # itemRating=item.find('span',class_="Rsc7Yb").text
        # print(itemRating)
    except:
        itemRating="No Ratings avilable"
        

    try:
        # itemRatingNumber=item.find('div',class_='tDoYpc').find_all('span')[1].text
        itemRatingNumber=item.find('div',{'role':'tree'}).text
        # print(itemRatingNumber)
    except:
        itemRatingNumber="No product reviews available"

    try:
        itemDiscription=item.find_all('div',class_='hBUZL')[2].text
        # print(itemDiscription)
    except:
        itemDiscription="No discription click the link to know more about product."
    itemData=(itemTag,itemBrand,itemPrice,itemRating,itemRatingNumber,itemDiscription,itemWebLink,itemImageLink)
    return itemData

def SearchTerm(searchTerm):
    options=Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver= webdriver.Chrome(chrome_options=options)

    url=get_url(searchTerm)
    SearchRecords=[]

    driver.get(url)   #Get the url for further
    soup= BeautifulSoup(driver.page_source,'html.parser')
    try:
        itemView=soup.find('div', class_='NmsQ6b').span.get('class')
        if len(itemView)==2 and 'qa708e' in itemView:
            print('Normal View')
        else:
            url='https://www.google.com/'+ soup.find('div',class_='NmsQ6b').a.get('href')
            driver.get(url)   #Get the url for further
            soup= BeautifulSoup(driver.page_source,'html.parser')
            itemView=soup.find('div', class_='NmsQ6b').span.get('class')
    except:
        itemView=None
    results=soup.findAll("div", {"class": "sh-dlr__list-result"})
    # print("Number of Results "+ str(len(results)))

    for item in results:
        searchRecord=extract_results(item)
        # if searchRecord:
        SearchRecords.append(searchRecord)

    driver.close()
    return SearchRecords

    # with open('results.csv','w',newline='',encoding='utf-8') as finalResults:
    #     writer=csv.writer(finalResults)
    #     writer.writerow(['Tag','Price','Brand','Link','Image Link','Rating','Number of Ratings','Product Discription'])
    #     writer.writerows(searchRecords)

def navmaster(request):

    return render(request,'navigation.html')

def wishlist(request):

    return render(request,'wish_list.html')
    
def offers(request):

    return render(request,'offers.html')
    
def history(request):

    return render(request,'history.html')
    
def settings(request):

    return render(request,'settings.html')
    
def contactus(request):

    if request.method == 'POST' or None:
        form= contactUs(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'contect_us.html',{'form':form})
            print("This valid form is running")
        else:
            form=contactUs()
            return render(request,'contect_us.html',{'form':form})
            print("This is else part something is wrong")
    else:
        form=contactUs()
        print("Nothing is getting request")

    return render(request,'contect_us.html')
    
def feedback(request):

    if request.method == "POST" or None:
        form= feedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'feedback.html',{'form':form})
        else:
            form= feedbackForm()
            return render(request, 'feedback.html',{'form':form})
    else:
        form=feedbackForm()

    return render(request,'feedback.html')
    
def aboutus(request):

    return render(request,'about_us.html')


