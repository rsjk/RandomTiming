import re
import urllib.request
import math
import sys
import time

# Tests ping of random number generators
def get_random_numbers(url, line):
    ping_amount = 10
    avg = 0
    response = "from_ip_address:" + line.rstrip('\n') + " "
    for i in range(ping_amount):
        start = time.time()
        try:
            webpage = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            response += str(e.reason)
            print(response)
            return response
        loading_page = webpage.read()
        end = time.time()
        webpage.close()
        avg += end - start

    # Average out the pings and convert to milliseconds
    avg = (avg / ping_amount)*1000
    # return the time to ping
    response = str(math.ceil(avg))+ "ms"
    print(response)
    return response


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a text file with URLs")
    else:
        # Get the file from the second arg
        responses = []
        with open(sys.argv[1], 'r') as file, open("latency_log.csv","w+") as out:
            out.write("info,url,latency(ms)\n")
            for line in file:
                try:
                    info, url = line.split('@')
                    if ("http://"not in url) and ("https://" not in url):
                        url = "http://" + url
                    # Get the random numbers
                    result = get_random_numbers(url, line)
                    responses.append(result)
                    csvrow = info + "," + url.rstrip('\n') + "," + result + '\n'
                    out.write(csvrow)
                except ValueError as e:
                    print(e.reason)
        file.close()
        # Log the results
        logfile = open("timing_experiment_test_log.txt","w+")
        for i in range(len(responses)):
            line = responses[i] + '\n'
            logfile.write(line)
        logfile.close()

