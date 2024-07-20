#scrape single product details
from bs4 import BeautifulSoup
import requests
import json


url = "https://www.flipkart.com/boult-w20-zen-enc-mic-35h-battery-life-low-latency-gaming-made-india-5-3v-bluetooth-headset/p/itm42ba3da4c8d78?pid=ACCGRNFM5GBPUKPF"
#url = "https://www.flipkart.com/realme-c53-champion-black-128-gb/p/itm5df90168ecd05?pid=MOBGTEVGGM7CTGXU"
head = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language":"en-US , en;q=0.5",
    'Accept-Encoding': 'gzip, deflate, br'
})
data = requests.get(url, headers=head)
soup = BeautifulSoup(data.content, "html.parser")
Pimages = soup.find_all(attrs={"class": "_0DkuPH"})
thumbnail = []
for img in Pimages:
    img = img.get("src")
    img = img.replace("128", "460")
    thumbnail.append(img)
#print(thumbnail)
detailsdeiv = soup.find(attrs={"class": "DOjaWF YJG4Cf"})

# name original price mrp ratting
pname = detailsdeiv.find(attrs={"class": "VU-ZEz"}).text
pname = pname.replace("\u00a0", " ")
p_o_price = detailsdeiv.find(attrs={"class": "Nx9bqj CxhGGd"}).text
p_o_price = p_o_price.replace("\u20b9", " ")
rating =  detailsdeiv.find(attrs={"class": "XQDdHH"}).text
mrp =  detailsdeiv.find(attrs={"class": "yRaY8j A6+E6v"}).text
discount =  detailsdeiv.find(attrs={"class": "UkUFwK WW8yVX"}).text

# from ratting span get total review and total_rattings
rattindDiv =  detailsdeiv.find(attrs={"class": "hG7V+4"})
total_review = rattindDiv.next_sibling.text
total_review = total_review.replace("\xa05,", "")
total_rattings = rattindDiv.previous_sibling.text
total_rattings = total_rattings.replace("\xa0", "")
description =  detailsdeiv.find(attrs={"class": "yN+eNk w9jEaj"})
#print(description)
if description == None:
    print("Description not awailable")
    description = " not found"
else:
    description = description.text
#print(description)

# get highlights of the product
highlights =  detailsdeiv.find_all(attrs={"class": "_7eSDEz"})
allspecs = []
for item in highlights: 
    allspecs.append(item.text)


# get offers of the product
offersdiv =  detailsdeiv.find_all(attrs={"class": "+-2B3d row"})
alloffers= []
for child in offersdiv:
    offerTag = child.find(attrs={"class": "ynXjOy"})
    offers= offerTag.next_sibling.text
    alloffers.append({"tag": offerTag.text , "offer": offers})
    
#try to grab specs
specsdiv = detailsdeiv.find_all(attrs={"class": "GNDEQ-"})
alldetals =[]
for child in specsdiv:
    title = child.find(attrs={"class": "_4BJ2V+"}).text
    
    detailsdiv = child.find_all(attrs={"class": "WJdYP6 row"})
    some =[] 
    #print(detailsdiv)
    for items in detailsdiv:
        #print(items)
        
        details = items.find(attrs={"class": "+fFi1w col col-3-12"})
        if details == None:
            details = {"text": "Important Note"}
            details = details['text']
        else:
            details = details.text
        #print(details)
        
        #detailstr = details.next_sibling.text
        #print(detailstr)
        detailstr = items.find(attrs={"class": "+HPETK2"})
        some.append(f"{details} :  {detailstr}" )
    alldetals.append([{"details":some},{"title":title}])


#print(alldetals)

makeJson = {
    "name" : pname,
    "current_price" : p_o_price,
    "original_price": mrp,
    "discount_percent": discount,
    "rating": rating,
    "thumbnail": thumbnail,
    "t_ratting": total_rattings,
    "t_review": total_review,
    "description": description,
    "highlights": allspecs,
    "offers": alloffers,
    "specs": alldetals
    
}

def detailsdata():
    return makeJson



    