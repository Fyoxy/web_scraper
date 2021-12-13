import os
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup


for x in range(1, 5):
    #websites to scrape from
    my_url = "https://www.prismamarket.ee/products/17258/page/%d?main_view=1" % (x)
    
    #opening up connection, grabbing the page
    hdr = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    req = Request(my_url, headers=hdr)
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    
    
    #html parsing
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("li",{"class":"js-shelf-item"})
    
    filename = "Prisma_lk%d.txt" % (x)
    f = open(filename, "w")
    
    
    for container in containers:
    
        price_container = container.findAll("div", {"class":"js-info-price"})
        price_whole = price_container[0].span.text
        priceDec_container = price_container[0].findAll("span", {"class":"decimal"})
        price_decimal = priceDec_container[0].text
        price = price_whole + "," + price_decimal + "€"
        
        title_container = container.findAll("div", {"class":"name"})
        title = title_container[0].text.strip()
        
        pricePer_container = container.findAll("div", {"class":"unit-price"})
        price_per = pricePer_container[0].text.strip()
    
        f.write (title + "#" + price + "#" + price_per + "\n")
        
    f.close()


with open('Prisma_Karastus.txt', 'a') as outfile:
    for x in range(1, 5):
        fname = 'Prisma_lk%d.txt' % (x)
        with open('Prisma_Karastus.txt', 'a') as outfile:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                    
for x in range(1, 5):
    file = "Prisma_lk%d.txt" % (x)
    os.remove(file)