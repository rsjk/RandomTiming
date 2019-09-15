# Random Number Generator GCP Project
This repository contains the 4 different implementations of the Random Number Generator. The generators generate a random number between 1 and 1 million.
* java-appengine-randomnumbergenerator-master is the Java App Engine Implementation. 
* RandomNumberTomcat-master is the Java Virtual Machine implementation.
* RandomNumberPythonAE is the Python App Engine Implementation. 
* RandomNumberFlask is the Python Virtual Machine implementation.

## Our Deployments
Our deployments can be found at the following URLs:
* Java App Engine https://randomnumbergeneratorclean.appspot.com/
* Java Virtual Machine http://35.209.25.119/Servlets/RandomNumberGen
* Python App Engine http://python-rand-ae.appspot.com/
* Python Virtual Machine http://35.193.182.65/

## Testing
The testing script is testscript.py. The script accepts the URL of the generator to test as an argument. To run the script, execute "python testscript.py [URL of Generator]". We ran the script for each generator 10 times, generating 1000 numbers each time. The script checks that at least 750 numbers are unique in each run. Our test results are in the TestResults directory. Each test was successful.

## Deployment Instructions
Instructions to create your own deployments of the apps.
### Java App Engine
1. Download the code for the Java App Engine deployment
2. Create a new project in Google Cloud Platform
3. Navigate to the App Engine page and click on "Create Application"
4. Select an appropriate server location
5. Select "Java" as the language and select "Standard" as the environment
6. Open Google Cloud console
7. Navigate to the path "~/getting-started-java/appengine-standard-java8/helloworld"
8. Execute command "rm -rf src"
9. Copy the downloaded "src" folder into the directory replacing the old one you removed
10. Execute command "mvn appengine:deploy"
11. Navigate to the link shown on the dashboard page of App Engine to receive a generated number

### Java Virtual Machine
1. Download the code for the Java Tomcat/Virtual Machine deployment or the WAR file named "Servlets.war"
2. Create a new project in Google Cloud Platform
3. Navigate to the link "https://console.cloud.google.com/marketplace/details/click-to-deploy-images/tomcat"
4. Click on "LAUNCH ON COMPUTE ENGINE"
5. Select the project you created
6. Leave the settings as default except for changing the Zone to an appropriate location
7. Scroll to the bottom of the page and click "Deploy"
8. Wait for the deployment operation to finish
9. You may follow the "Suggested next steps" if you choose to
10. Using the source code for the servlet create a WAR file or the WAR file you downloaded from the repo.
11. Click on the "Visit the site" button
12. On the webpage that just openned click on the hyperlink "manager webapp" and login using the information provided in the deployment manager.
13. Under the "Deploy" section of the webpage go to the subsection labeled "WAR file to deploy" and click on "Choose File" and choose the WAR file you either created or downloaded and then click "Deploy"
14. Setup a static IP for your virtual machine by going to the VPC Network page on GCP
15. Under the "External IP addresses" find the IP address being used by the VM instance containing your Tomcat deployment
16. Switch "Emphemral" to "Static" and reserve an IP with any name you find appropriate
17. To access the random number generator navigate to "[The IP Address of the Server]/Servlets/RandomNumberGen"

### Python App Engine
1. Create a new project in Google Cloud Platform
2. Open the Cloud Shell
3. Clone this repository with the command "git clone https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets/"
4. Switch to the PythonRandomNumberAE directory with "cd RandomNumberGen-Servlets/RandomNumberPythonAE"
5. Install a virtual environment. Run the command "virtualenv --python python3 venv"
6. Activate the virtual environment by running "source venv/bin/activate"
7. Install project dependencies with "pip install -r requirements.txt"
8. Run in the Flask development server with "python main.py"
9. Create the app with "gcloud app create"
10. Deploy the app with "gcloud app deploy app.yaml --project [Project ID]"
11. The default URL of your app is [Project ID].appspot.com. Or you can use the "gcloud app browse" command to open it.

### Python Virtual Machine
1. Create a new project in Google Cloud Platform
2. Navigate to the Compute Engine page and create a new VM instance with f1-micro, Ubuntu 18.04 LTS, and enable HTTP and HTTPS traffic
3. Connect to the instance via SSH
4. Execute the command "sudo apt update && sudo apt upgrade"
5. Type "hostname" to find hostname. Edit the host file with "sudo nano /etc/hosts". Under the localhost line, type the IP address of the server, then press tab and type the hostname.
6. Set up a firewall. Execute the following commands:
* sudo apt install ufw
* sudo ufw default allow outgoing
* sudo ufw default deny incoming
* sudo ufw allow ssh
* sudo ufw allow http/tcp
* sudo ufw enable
7. Clone this repository with the command "git clone https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets/"
8. Switch to the RandomNumberFlask directory with "cd RandomNumberGen-Servlets/RandomNumberFlask/"
9. Install pip with "sudo apt install python3-pip"
10. Install virtual environment with "sudo apt install python3-venv"
11. Create virtual environment with "python3 -m venv venv"
12. Activate the virtual environment with "source venv/bin/activate"
13. Install project dependencies with "pip install -r requirements.txt"
14. Install nginx with "sudo apt install nginx"
15. Install gunicorn with "pip install gunicorn"
16. Update nginx config file. Do the following: 
* sudo rm /etc/nginx/sites-enabled/default
* sudo nano /etc/nginx/sites-enabled/random_number_generator
* Copy the contents of RandomNumberFlask/nginx_config.txt into the file. Change [The IP Address of the Server] to your IP.
17. Restart nginx server with "sudo systemctl restart nginx"
18. Install supervisor with "sudo apt install supervisor"
19. Set up supervisor with "sudo nano /etc/supervisor/conf.d/random_number_generator.conf"
20. Find out the number of workers for gunicorn with (2 * number of cores) + 1. Execute "nproc --all" to find number of cores.
21. Copy the contents of RandomNumberFlask/supervisor_config.txt into the file. Change [Your Username] and [Number of Workers].
22. Make the log files. Do "sudo mkdir -p /var/log/random_number_generator". Then "sudo touch /var/log/random_number_generator/random_number_generator.err.log". Then do "sudo touch /var/log/random_number_generator/random_number_generator.out.log".
23. Restart supervisor with "sudo supervisorctl reload"
24. Setup a static IP for your virtual machine by going to the VPC Network page on GCP
25. Under the "External IP addresses" find the IP address being used by the VM instance containing your Tomcat deployment
26. Switch "Emphemral" to "Static" and reserve an IP with any name you find appropriate
27. To access the random number generator navigate to "http://[The IP Address of the Server]"
