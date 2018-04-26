from craigslist import CraigslistForSale
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection


def ebay(keyword):

    api = Connection(appid='OwenKrus-pythonch-PRD-051ca6568-f8289d88', config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': keyword})
    
    reply = response.dict()
    #item = response.dict()
    #url = reply['searchResult']['item'][listingnum]['viewItemURL']
    #title = item['searchResult']['item'][listingnum]['title']
    prices = []
    for listingnum in range(10):
        try:
            prices.append(reply['searchResult']['item'][listingnum]['sellingStatus']['currentPrice']['value'])
        except KeyError:
            continue
    intprice = []
    if len(prices) == 0:
        return 0
    for price in prices:
        intprice.append(float(price))
    return sum(intprice)/len(intprice)




def fillter(name):
    blacklist = "new misc miscellaneous lol :) excellent awesome condition with without it work works working of vintage old pair your take very fast wow turkey car truck table furniture like no reduced ready ultra-high ultra high w/ free and eight-core (eight-core) core 8-core microsoft hd dual band touch parts brand pre-owned preowned pre owned ultra-portable portable fantastic grea great fast powerful extreme OP,KS overland park in hand slim slimline plus almost college kid selling sell need touchscreen first last good long little own other old right big high different small large next early young important few public bad same able yourself better done for sale well maintained two one support new wholesale".split(' ')
    graylist = "DVI HDMI sale ! @ # $ % ^ & * ( ) _ + = [ ] \ : \" ; ' < > ? , /".split()
    for b in blacklist:
        name = name.lower().replace(' '+b+' ', ' ')
    for b in blacklist:
        name = name.lower().replace(b+' ', ' ')
    for b in blacklist:
        name = name.lower().replace(' '+b, ' ')
    try:
        for g in graylist:
            name  = name.replace(g, '')
    except:
        print 'something went wrong'

    return name
        
  
    

cfs = CraigslistForSale(site='kansascity', filters={'query': 'oculus rift'})
craigs_list = [] 

for result in cfs.get_results(limit=10): #Getting craigslist prices and names
    if result['price'] != None:
        craigs_list.append([fillter(result['name']), result['url'], float(result['price'][1:])])



succ_ebay = []
for listing in craigs_list:
    curr_test = ebay(listing[0]) 
    if curr_test != 0:
        succ_ebay.append([listing[0], listing[1], curr_test])
























        
        
   









    

    


