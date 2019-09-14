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
1. 

### Python Virtual Machine
1. 
