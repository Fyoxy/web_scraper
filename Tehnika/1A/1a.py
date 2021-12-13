import os
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup

for x in range(1, 11):
    #websites to scrape from
    my_url = "https://www.1a.ee/arvutikomponendid_vorgutooted/komponendid/videokaardid/%d" % (x)
    
    #opening up connection, grabbing the page
    hdr = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    req = Request(my_url, headers=hdr)
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    
    
    #html parsing
    page_soup = soup(page_html.content, "html.parser").encode("utf-8").decode("utf-8")
    containers = page_soup.findAll("section",{"class":"product"})
    
    filename = "1A_lk%d.txt" % (x)
    f = open(filename, "w")
    
    
    for container in containers:
    
        price_container = container.findAll("div", {"class":"price"})
        price_container[0].sub.extract()
        price_cents = price_container[0].sup.text
        price_container[0].sup.extract()
        price = price_container[0].text + "," + price_cents + "€"
        
        title_container = container.findAll("h3")
        title = title_container[0].text.strip()
        
        info_container = container.findAll("ul", {"class":"info-list"})
        info = info_container[0].text.strip()
    
        f.write (title + "#" + price + "#\n" + info + "\n")
        
    f.close()


with open('1A.txt', 'a') as outfile:
    for x in range(1, 11):
        fname = '1A_lk%d.txt' % (x)
        with open('1A.txt', 'a') as outfile:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                    
for x in range(1, 11):
    file = "Prisma_lk%d.txt" % (x)
    os.remove(file)