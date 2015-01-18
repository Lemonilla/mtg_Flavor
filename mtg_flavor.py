# mtg_flavor.py <consumer_key> <consumer_secret> <access_token_key> <access_token_secret>

import twitter
import requests
import re as regex
import random
import time
import sys

# define global variables
flavor = regex.compile(r'<div class="cardtextbox" style="padding-left:10px;"><i>.*')
name = regex.compile(r'<span id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay">.*')
hashtag = "\n#mtg_flavor"
debug=False
consumer_key=sys.argv[1]
consumer_secret=sys.argv[2]
access_token_key=sys.argv[3]
access_token_secret=sys.argv[4]



while True:
        try:
                message="........................................................................................................................................................................................................................................................................."
                card_name=None
                flavor_text=None

                while len(message) > 140 or message == None:
                        while flavor_text == None or card_name == None:

                                ran = random.randrange(1,60000)
                                if debug == True:
                                        print ran

                                req = requests.get("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=%d" % ran)
                                for l in flavor.findall(req.text):
                                    l = l.replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("</i></div><div class='cardtextbox'></i>","\n").replace("</i></div></div>","")
                                    if l <> None:
                                        flavor_text = l.encode('utf8')

                                for n in name.findall(req.text):
                                        if n <> None:
                                                card_name = n.replace("<span id=\"ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay\">","").replace("</span>","").replace("  ","").replace("\n","")
                                                card_name = card_name.encode('utf8')
                                                card_name = "["+str(card_name[:-1])+"]"
                                                card_name = card_name + "\n"

                                if debug == True:
                                        print card_name

                        message = card_name + flavor_text

                        if len(message)+13 < 140:
                                message = message + hashtag
                        if len(message) > 140 or message == None:
                                message="........................................................................................................................................................................................................................................................................."
                                card_name=None
                                flavor_text=None

                if debug == True:
                        print message

                status = twitter.Api(consumer_key=consumer_key,
                                        consumer_secret=consumer_secret,
                                        access_token_key=access_token_key,
                                        access_token_secret=access_token_secret,
                                        input_encoding='utf-8').PostUpdate(message)
                time.sleep(random.randrange(1*60,1*60*60))

        except:
                print "Error, Retrying in 30 Seconds. . ."
                time.sleep(30)
