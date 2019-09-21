import re
import urllib.request
import math
import sys
import time

# Tests ping of rendom number generators
def get_random_numbers(url):
    ping_amount = 10
    avg = 0
    for i in range(ping_amount):
        start = time.time()
        webpage = urllib.request.urlopen(url)
        loadingpage = webpage.read()
        end = time.time()
        webpage.close()
        avg += end - start

    # Average out the pings and convert to milliseconds
    avg = (avg / ping_amount)*1000
    # return the time to ping
    response = url.rstrip('\n') + "\n      Average latency: " + str(math.ceil(avg))+ "ms"
    print(response)
    return response

    


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a text file with URLs")
    else:
        # Get the file from the second arg
        responses = []
        with open(sys.argv[1], 'r') as file:
            for url in file:
                # Get the random numbers
                responses.append(get_random_numbers(url))
        file.close()
        # Log the results
        logfile = open("test_log.txt","w+")
        for i in range(len(responses)):
            line = responses[i] + '\n'
            logfile.write(line)
        logfile.close()
        
