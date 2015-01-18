# http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=<ID>

import requests
import re as regex
#import urlparse
import sys
import os

flavor = regex.compile(r'<div class="cardtextbox" style="padding-left:10px;"><i>.*')
results = []


def crawl(url):
        # Get the webpage
        req = requests.get(url)

        # Find all emails on current page
        for l in flavor.findall(req.text):
            print type(l)
            l.replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>\"","")
            if l <> None:
                print "--"
                save_obj.write(l.encode('utf8').replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("</i></div><div class='cardtextbox'></i>","\\n").replace("</i></div></div>","")+"\n")

with open(sys.argv[1],'w') as save_obj:
    for x in xrange(int(sys.argv[2]),int(sys.argv[3])+1):
        # os.system('cls')
        print x,"/",sys.argv[3]
        crawl("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=%d" % x)
save_obj.close()
'''
with open(sys.argv[1],'w') as save_obj:
    for line in results:
        if line <> "[]":
            save_obj.write(line.encode('utf8').replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("</i></div><div class='cardtextbox'></i>","\\n").replace("</i></div></div>","")+"\n")



'''