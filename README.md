https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets
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
2. Navigate to the App Engine page and click on "Create Application"
3. Select an appropriate server location
4. Select "Python" as the language and select "Standard" as the environment
5. Open the Cloud Shell
6. Clone this repository with the command "git clone https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets/"
7. Switch to the PythonRandomNumberAE directory with "cd RandomNumberGen-Servlets/PythonRandomNumberAE/"
Install pip with "sudo apt install python3-pip"
8. Install project dependencies with "pip install -r requirements.txt"
9. Create the app with "gcloud app create"
10. Deploy the app with "gcloud app deploy app.yaml --[Project ID]"
11. The default URL of your app is [Project ID].appspot.com. Or you can use the "gcloud app browse" command to open it.

### Python Virtual Machine
1. Create a new project in Google Cloud Platform
2. Navigate to the Compute Engine page and create a new VM instance with your preferred options
3. Connect to the instance via SSH
4. Set up a firewall. Execute the following commands:
* sudo apt install ufw
* sudo ufw default allow outgoing
* sudo ufw default deny incoming
* sudo ufw allow ssh
* sudo ufw allow http/tcp
* sudo ufw enable
6. Clone this repository with the command "git clone https://github.com/Andy-Vu-Viz/RandomNumberGen-Servlets/"
7. Switch to the RandomNumberFlask directory with "cd RandomNumberGen-Servlets/RandomNumberFlask/"
8. Install pip with "sudo apt install python3-pip"
9. Install virtual environment with "sudo apt install python3-venv"
10. Create virtual environment with "python3 -m venv venv"
11. Activate the virtual environment with "source venv/bin/activate"
12. Install project dependencies with "pip install -r requirements.txt"
13. Install nginx with "sudo apt install nginx"
14. Install gunicorn with "pip install gunicorn"
15. Update nginx config file. Do the following: 
* sudo rm /etc/nginx/sites-enabled/default
* sudo nano /etc/nginx/sites-enabled/random_number_generator
* Inside the file, type:
server {
  listen 80;
  server_name = [The IP Address of the Server];
  
  location / {
    proxy_pass http://localhost:8000;
    include /etc/nginx/proxy_params;
    proxy_redirect off;
  }
}
16. Restart nginx server with "sudo systemctl restart nginx"
17. Find out the number of workers for gunicorn with (2 * number of cores) + 1. Execute "nproc --all" to find number of cores.
18. Install supervisor with "sudo apt install supervisor"
19. Set up supervisor with "sudo nano /etc/supervisor/conf.d/random_number_generator.conf"
* Inside the file type:
[program:random_number_generator]
directory=/home/[Your Username]/RandomNumberGen-Servlets/RandomNumberFlask
command=/home/[Your Username]/RandomNumberGen-Servlets/RandomNumberFlask/venv/bin/gunicorn -w [Number of Workers] random_number_generator:app
user=[Your Username]
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
20. Restart supervisor with "sudo supervisorctl reload"
21. Setup a static IP for your virtual machine by going to the VPC Network page on GCP
22. Under the "External IP addresses" find the IP address being used by the VM instance containing your Tomcat deployment
23. Switch "Emphemral" to "Static" and reserve an IP with any name you find appropriate
24. To access the random number generator navigate to "http://[The IP Address of the Server]"
  
