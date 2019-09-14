import re
import urllib.request
import math
from bs4 import BeautifulSoup
import sys


# Generate 1000 random numbers 10 times and check that there are at least 750 unique numbers in each iteration
def get_random_numbers(url):
    passes = 0
    fails = 0
    logfile = open("test_log.txt","w+")
    for f in range(0, 10):
        numbers = []
        for k in range(0, 1000):
            # Request from the given url
            html = urllib.request.urlopen(url)

            # Parse the text from the html
            soup = BeautifulSoup(html, features="html.parser")
            data = soup.findAll(text=True)
         
            # Print the numbers to the command line
            for i in list(data):
                if i.isdigit():
                    print(k,': ',i)
                    numbers.append(i)

        # Make a set of the numbers -- sets can only contain unique elements, so we can check for duplicates this way
        numbers_set = set(numbers)

        header = "Run " + str(f + 1) + ":\n"
        logfile.write(header)

        # Check if there are at least 750 unique numbers
        if len(numbers_set) < 750:
            logfile.write("Test failed\n")
            fails += 1
        else:
            logfile.write('Test passed\n')
            passes += 1
        logfile.write(str(len(numbers_set)))
        logfile.write(" unqiue numbers were retrieved\n")

    # Log the total passes and fails
    total_passes_str = "Total passes: " + str(passes) + "\n"
    logfile.write(total_passes_str)
    total_fails_str = "Total fails: " + str(fails) + "\n"
    logfile.write(total_fails_str)

    logfile.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL")
    else:
        # Get the url from the second arg
        url = sys.argv[1]
        # Get the random numbers
        get_random_numbers(url)
