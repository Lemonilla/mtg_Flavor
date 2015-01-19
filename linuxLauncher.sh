#!/bin/bash 

consumer_key=$(head -n 1 ConsumerKey.txt)
consumer_secret=$(head -n 1 ConsumerSecret.txt)
access_token_key=$(head -n 1 AccessToken.txt)
access_token_secret=$(head -n 1 AccessTokenSecret.txt)

Python mtg_flavor.py consumer_key consumer_secret access_token_key access_token_secret