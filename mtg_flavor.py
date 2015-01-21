#!/usr/bin/env python
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
debug=True
consumer_key=sys.argv[1]
consumer_secret=sys.argv[2]
access_token_key=sys.argv[3]
access_token_secret=sys.argv[4]

# Loop forever
while True:
        # Define defaults
        message="........................................................................................................................................................................................................................................................................."
        card_name=None
        card_flavor=None
        card_name_s=None
        card_flavor_s=None

        # Catch connection errors
        try:


                # loop until a match is found
                while len(message) > 140 or message == None:
                        while card_flavor == None or card_name == None:

                                # Generate random number
                                ran = random.randrange(1,60000)
                                if debug == True:
                                        print ran
                                try:
                                        # Check random number for flavor text
                                        req = requests.get("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=%d" % ran)
                                        card_name = name.findall(req.text)
                                        card_flavor = flavor.findall(req.text)
                                        card_name_s = card_name[0].replace("<span id=\"ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay\">","").replace("</span>","").replace("  ","").replace("\n","").replace("\n","")
                                        card_flavor_s = card_flavor[0].replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("<div class=\"cardtextbox\" style=\"padding-left:10px;\"><i>","").replace("</i></div><div class='cardtextbox'></i>","\n").replace("</i></div></div>","")

                                except IndexError:
                                        message="........................................................................................................................................................................................................................................................................."
                                        card_name=None
                                        flavor_text=None

                        message = "[" + card_name_s[:-1] + "]\n" + card_flavor_s

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
                        try:
                                print message
                        except: UnicodeEncodeError:
                                print "Unicode Error"
                # Post status
                status = twitter.Api(consumer_key=consumer_key, 
                                        consumer_secret=consumer_secret, 
                                        access_token_key=access_token_key, 
                                        access_token_secret=access_token_secret, 
                                        input_encoding='utf-8').PostUpdate(message) 

                # Wait for random time between 1 min and 1 hr
                sleep = random.randrange(1,30*60)
                while sleep > 0:
                        time.sleep(1)
                        sleep = sleep - 1
                        if debug == True:
                                sys.stdout.flush()
                                print "\r",
                                print "        ",
                                print "\r",
                                print sleep,

        # Catch connection errors
        except requests.exceptions.ConnectionError:
                print "Error, retrying. . ."
        