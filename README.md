# Daily-Quote.py

A simple quote emailer in python. 

Gets quotes of the day from http://feeds.feedburner.com/quotationspage/qotd 

Puts the whole file into an array. Finds the relevant tags ("title" and "description").
Then these can be found as indicies and each day a random number is selected out the daily quotes. 

This is then sent to whoever you want. 
The settings for which are in the config file.

You will need to change the settings in the main python file if you want to use another emailing service other than GMail. 


If any of the import statements don't work then just use 

    pip install 

to install the relevant packages
