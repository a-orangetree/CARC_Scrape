import urllib.request
from bs4 import BeautifulSoup
import re
import time

print (time.asctime(time.localtime(time.time())))

washingtonPublishingCompanyURL = ('http://www.wpc-edi.com/reference/codelists/healthcare/claim-adjustment-reason-codes/')

try: CARC_HTML = urllib.request.urlopen(washingtonPublishingCompanyURL).read()
except: print ('URL is not working:',washingtonPublishingCompanyURL)

CARCSoup = BeautifulSoup(CARC_HTML, 'html.parser')
CARCTags = CARCSoup('td')

start = 'no'

for tag in CARCTags:
    if len(str(tag.contents)[2:-2]) == 2 or len(str(tag.contents)[2:-2]) == 3\
    or len(str(tag.contents)[2:-2]) == 1:     
        print (str(tag.contents)[2:-2])
        start = 'yes'
    if start == 'yes' and len(str(tag.contents)[2:-2]) > 3:
        re.search('[A-Za-z]\'',str(tag.contents)[2:-2])        
        print (str(tag.contents)[2:-2])
