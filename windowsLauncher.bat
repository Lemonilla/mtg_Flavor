@echo off
pushd ..\mtg_Flavor_keys
set /p consumer_key=<ConsumerKey.txt
set /p consumer_secret=<ConsumerSecret.txt
set /p access_token_key=<AccessToken.txt
set /p access_token_secret=<AccessTokenSecret.txt
popd

mtg_flavor.py %consumer_key% %consumer_secret% %access_token_key% %access_token_secret%