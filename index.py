from Crawler import Crawler
from Website import Website


crawler = Crawler()
id = 10157
idLength = 15000
successLink = []
faileLink = []
while id < idLength :
    url = 'https://item.szlcsc.com/' + str( id ) + '.html'
    crawler.parse( Website(), url)
    id += 1


