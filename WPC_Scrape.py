import urllib.request
from bs4 import BeautifulSoup
import re
import numpy as np
import time
import pandas as pd

#Enter the desired destination of the output file. If using a windows machine
# please place an "r" prior to the first quote(')
outputFilePath = '/path/to/output'


washingtonPublishingCompanyURL = ('http://www.wpc-edi.com/reference/codelists/healthcare/claim-adjustment-reason-codes/')

try: CARC_HTML = urllib.request.urlopen(washingtonPublishingCompanyURL).read()
except: print('URL is not working:',washingtonPublishingCompanyURL)

soup = BeautifulSoup(CARC_HTML, 'html.parser')


codes = []
descriptions = []
startDates = []
stopDates = []
actives = []


tags = soup('td', { "class" : "code" })


for tag in tags: 
#    print (str(tag.contents)[2:-2])
    code = str(tag.contents)[2:-2]
    codes.append(str(code))


tags = soup('td', {"class" : "description"})
for tag in tags: 
    description = re.findall('^.*Note:\s\w|^.*<span',str(tag.contents))   
    description = str(description).replace('\\','')[4:-10]
    descriptions.append(description)
    
    startDate = re.findall(r'Start:[^|<]*',str(tag.contents))
    startDates.append(str(startDate)[9:19])
    
    stopDate = re.findall(r'Stop:[^|<]*',str(tag.contents))
    stopDates.append(str(stopDate)[8:18])
    
    active = re.search(r'Stop:[^|<]*',str(tag.contents))
    if active == None:
        active = 'Active'
    else:
        active = 'Not Active'
    actives.append(str(active))
    

intoDataFrame = {"Codes" : codes\
                ,"Descriptions" : descriptions\
                ,"Start Date" : startDates\
                ,"Stop Date" : stopDates\
                ,"Active" : actives}
                
CARCs = pd.DataFrame(intoDataFrame)


#def activeOrNot(x):
#    if x.notnull():
#        return "Active"
#    else:
#        return "Not Active"
#
#CARCs['Active'] = CARCs.apply(lambda x: activeOrNot(x['Stop Date']), axis = 1)
CARCs['CARC/RARC'] = 'CARC'
 
#print (CARCs)


##############################################################################3


washingtonPublishingCompanyURL2 = ('http://www.wpc-edi.com/reference/codelists/healthcare/remittance-advice-remark-codes/')

try: RARC_HTML = urllib.request.urlopen(washingtonPublishingCompanyURL2).read()
except: print('URL is not working:',washingtonPublishingCompanyURL2)

soup = BeautifulSoup(RARC_HTML, 'html.parser')


codes = []
descriptions = []
startDates = []
stopDates = []
actives = []

tags = soup('td', { "class" : "code" })


for tag in tags: 
#    print (str(tag.contents)[2:-2])
    code = str(tag.contents)[2:-2]
    codes.append(str(code))


tags = soup('td', {"class" : "description"})
for tag in tags: 
    if 'Alert' in str(tag.contents):
        description = re.findall('^.*\s<s|^.*,<s',str(tag.contents)[63:])
        description = str(description)[3:-7].replace('\\','')
        descriptions.append(description)
    else:
        description = re.findall('^.*\s<s|^.*,<s',str(tag.contents)) 
        description = str(description)[4:-7].replace('\\','')
        descriptions.append(description)
    
    startDate = re.findall(r'Start:[^|<]*',str(tag.contents))
    startDates.append(str(startDate)[9:19])
    
    stopDate = re.findall(r'Stop:[^|<]*',str(tag.contents))
    stopDates.append(str(stopDate)[8:18])
    
    active = re.search(r'Stop:[^|<]*',str(tag.contents))
    if active == None:
        active = 'Active'
    else:
        active = 'Not Active'
    actives.append(str(active))
    

intoDataFrame = {"Codes" : codes\
                ,"Descriptions" : descriptions\
                ,"Start Date" : startDates\
                ,"Stop Date" : stopDates\
                ,"Active" : actives}
                
RARCs = pd.DataFrame(intoDataFrame)

#RARCs['Active'] = RARCs.apply(lambda x: activeOrNot(x['Stop Date']), axis = 1)
RARCs['CARC/RARC'] = 'RARC'

#print(RARCs)
CARCs = CARCs.append(RARCs)

todayYear = time.strftime("%Y")
todayMonth = time.strftime("%m")
todayDay = time.strftime("%d")


CARCs.to_excel(outputFilePath+'_'+todayYear+todayMonth+todayDay+'.xlsx', index = False)
print('Excel file created at: ',outputFilePath)
