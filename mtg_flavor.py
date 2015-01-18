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

# Loop forever
while True:
        # Catch connection errors
        try:
                # Define defaults
                message="........................................................................................................................................................................................................................................................................."
                card_name=None
                flavor_text=None

                # loop until a match is found
                while len(message) > 140 or message == None:
                        while flavor_text == None or card_name == None:

                                # Generate random number
                                ran = random.randrange(1,60000)
                                if debug == True:
                                        print ran

                                # Check random number for flavor text
                                req = requests.get("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=%d" % ran)
                                for l in flavor.findall(req.text):
                                    l = l.replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("</i></div><div class='cardtextbox'></i>","\n").replace("</i></div></div>","")
                                    if l <> None:
                                        flavor_text = l.encode('utf8')

                                # Check random number for card name
                                for n in name.findall(req.text):
                                        if n <> None:
                                                card_name = n.replace("<span id=\"ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay\">","").replace("</span>","").replace("  ","").replace("\n","")
                                                card_name = card_name.encode('utf8')
                                                card_name = "["+str(card_name[:-1])+"]"
                                                card_name = card_name + "\n"

                                # Print debug information
                                if debug == True:
                                        print card_name

                        # Combine into single string
                        message = card_name + flavor_text

                        # Add hashtage if possable
                        if len(message)+13 < 140:
                                message = message + hashtag

                        # Check message length and restart if too long
                        if len(message) > 140 or message == None:
                                message="........................................................................................................................................................................................................................................................................."
                                card_name=None
                                flavor_text=None

                # Print debug information
                if debug == True:
                        print message

                # Post status
                status = twitter.Api(consumer_key=consumer_key,
                                        consumer_secret=consumer_secret,
                                        access_token_key=access_token_key,
                                        access_token_secret=access_token_secret,
                                        input_encoding='utf-8').PostUpdate(message)

                # Wait for random time between 1 min and 1 hr
                time.sleep(random.randrange(1*60,1*60*60))

        # Catch connection errors
        except:
                print "Error, retrying in 30 seconds. . ."
                time.sleep(30)
