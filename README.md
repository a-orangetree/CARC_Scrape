##INTRODUCTION
This program scrapes relevant CARC/RARC codelist information from the Washington Publishing Company (WPC) and outputs an Excel file. These codelists are viewable free online. Viewing the lists online, however is often inconvenient and must be manually copied into another medium (e.g. Excel) to be useful. 


##REQUIREMENTS
Python 3 is required, along with several libraries, all of which comes standard in Continuum's Anaconda Python distrbution (found here: https://www.continuum.io/downloads) 

Microsoft Excel, LibreOffice, or some other spreadsheet application will be needed to read the file. The file is currently output in .xslx format.


##WEBSITES SCRAPED
The CARC website can be found here: http://www.wpc-edi.com/reference/codelists/healthcare/claim-adjustment-reason-codes/
The RARC website can be found here: http://www.wpc-edi.com/reference/codelists/healthcare/remittance-advice-remark-codes/


##CARCs
CARC stands for "Claim Adjustment Reason Code." 

From the WPC website:

"Claim adjustment reason codes communicate an adjustment, meaning that they must communicate why a claim or service line was 
paid differently than it was billed. If there is no adjustment to a claim/line, then there is no adjustment reason code."


##RARCs
RARC stands for "Remittance Advice Remark Code." 

From the WPC website:

"Remittance Advice Remark Codes (RARCs) are used to provide additional explanation for an adjustment already described by a 
Claim Adjustment Reason Code (CARC) or to convey information about remittance processing. Each RARC identifies a specific message 
as shown in the Remittance Advice Remark Code List. There are two types of RARCs, supplemental and informational. The majority of 
the RARCs are supplemental; these are generally referred to as RARCs without further distinction. Supplemental RARCs provide 
additional explanation for an adjustment already described by a CARC. The second type of RARC is informational; these RARCs are 
all prefaced with Alert: and are often referred to as Alerts. Alerts are used to convey information about remittance processing 
and are never related to a specific adjustment or CARC."
