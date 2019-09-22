# Random Number Generator Timing
We were tasked to create a program that requests a random number from all four of our IP addresses and record the time it takes. The code can be found [here](https://github.com/Andy-Vu-Viz/RandomTiming/Timing). In our [Random Number GCP Project](https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets), we created a [python script](https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets/blob/master/testscript.py) to test the uniqueness of our random number generators. The script requests 1000 numbers 10 times, and each time it checks that at least 750 are unique. To test the timing of our generators, we needed to modify the script to account for time.

## Implementation
### First Implementation
Our first test implementation was the following:
![](https://github.com/Andy-Vu-Viz/RandomTiming/blob/master/Timing/screenshots/first_implementation.PNG)
The loops were removed and code was added to record the time before and after pinging a server. 
### Full Implementation
Our full implementation is the following: ([link to script](https://github.com/Andy-Vu-Viz/RandomTiming/blob/master/Timing/timing.py))
![](https://github.com/Andy-Vu-Viz/RandomTiming/blob/master/Timing/screenshots/full_implementaion.PNG)
Now the code pings a server a ping_amount of times and averages the times. Results are printing to the command line and written to a file. The script takes a file with the IPs/URLs seperated by new lines as a program argument. To run the script, execute the command "python timing.py [name of file]".
