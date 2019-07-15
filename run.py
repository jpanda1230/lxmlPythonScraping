from lxml import html
import requests
import time

search_words = ["OPENDOOR","OFFERPAD","SPH"]
loopnum = 0
for i in range(62489,80001):
    i_str = "{:07d}".format(i)
    print("Checking ID " + i_str)

    # open the Deed page and get the content
    url = "http://services.wakegov.com/realestate/Deeds.asp?id="+i_str
    page = requests.get(url)
    tree = html.fromstring(page.content)
    back1 = tree.xpath('//tr[@valign="top"]/td[2]/b/font/text()')

    if len(back1) <= 1:
        continue
    currentStr = '  ' + back1[1].strip()
    if (currentStr.find(str(search_words[0]))>1 or currentStr.find(str(search_words[1]))>1 or currentStr.find(str(search_words[2])) > 1) and (currentStr.find("JOESPH")<=1):
        print("Current field detected : " + currentStr+ "\n")
        continue
    else:
        for loopindex in range(2, len(back1)):
            detectedStr = '  ' + back1[loopindex].strip()
            if (detectedStr.find(str(search_words[0])) > 1 or detectedStr.find(str(search_words[1])) > 1 or detectedStr.find(str(search_words[2])) > 1) and (detectedStr.find("JOESPH")<=1):
                f = open("matches.txt", "a")
                f.write(i_str + "   Detected Item: "+ detectedStr + "\n")
                #f.write(i_str + "\n")
                f.close()
                break
            else:
                continue





