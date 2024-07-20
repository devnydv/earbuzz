from bs4 import BeautifulSoup
import requests
import json

def handleerror(val):
    if val == None:
        val = " Not Found"
    else:
        val = val.text
    return val
url = "https://www.flipkart.com/search?q=neckband"
#url = "https://www.flipkart.com/realme-c53-champion-black-128-gb/p/itm5df90168ecd05?pid=MOBGTEVGGM7CTGXU"
head = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language":"en-US , en;q=0.5",
    'Accept-Encoding': 'gzip, deflate, br'
})
data = requests.get(url, headers=head)
soup = BeautifulSoup(data.content, "html.parser")
link = soup.find_all(attrs={"class": "slAVV4"})

# grab name and link
allproducts =[]
for x in range(8):
    url_title = link[x].find(attrs={"class": "wjcEIp"})
    pname = url_title.text
    img = link[x].find(attrs={"class": "DByuf4"})
    thumbnail = img.get("src")
    share_url = url_title.get("href")
    real_price = link[x].find(attrs={"class": "Nx9bqj"}).text
    
    mrp = link[x].find(attrs={"class":"yRaY8j"}).text
    #print(pname, thumbnail, share_url)
    ratt = link[x].find(attrs={"class":"XQDdHH"})
    ratt = handleerror(ratt)
    
    
    total_review = link[x].find(attrs={"class": "Wphh3N"})
    total_review = handleerror(total_review)
    
    discount = link[x].find(attrs={"class": "UkUFwK"})
    discount = handleerror(discount)
    print(total_review)
    

    makeJson= {
        "name" : pname,
        "current_price" : real_price,
        "original_price": mrp,
        "discount_percent": discount,
        "rating": ratt,
        "t_review": total_review,
        "share_url": share_url,
        "thumbnail": thumbnail
        }
    allproducts.append(makeJson)
    #print(allproducts)
def senddata():
    #print(json.dumps(allproducts))
    return allproducts
senddata()
