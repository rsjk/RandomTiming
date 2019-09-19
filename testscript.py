import re
import urllib.request
import math
from bs4 import BeautifulSoup
import sys
import time

# Tests ping of rendom number generators
def get_random_numbers(url):
    logfile = open("test_log.txt","w+")

    pingstart = time.time()
   ping start = time.time()
    html = urllib.request.urlopen(url)
    pingend = time.time()
    totalping = pingend - pingstart
    # Parse the text from the html
    soup = BeautifulSoup(html, features="html.parser")
    data = soup.findAll(text=True)

    # Print the numbers to the command line
    for i in list(data):
       if i.isdigit():
          print(k,': ',i)
    # Log the total passes and fails
    t = "Total time: " + str(totalping) + "\n"
    logfile.write(totalping)

    logfile.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL")
    else:
        # Get the url from the second arg
        url = sys.argv[1]
        # Get the random numbers
        get_random_numbers(url)
