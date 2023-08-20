![uploading](https://github.com/iamistiyak/Face-Recognizer-Classifier/assets/86108816/3e7641f2-3998-4c4a-ad76-a2d55c9458a7)
![Uploading structure.png…]()
o![Uploading results.png…]()
# Face-Recognizer-Classifier
**Functionality :** Upload the image and get the result.<br>
**Description:** I have created this web-app for classify and predict the person's identifications based on the thier image. I am mainly consider the visible eyes for images.
Because I have used training model of SVM who basically consider the facial patterns to predict the results.<br><br>

I have hosted this web-app on the **AWS server** and used EC-2 instance.<br>
Fronted: I have used **HTML, CSS, JS**<br>
Backend: I have used **Flask**<br>
web-server: I have used **ngin-x** receive the http request from the user and communucate with the model and return the values(reverse proxy).

# Basic architecture
<img src="https://github.com/iamistiyak/Face-Recognizer-Classifier/blob/main/outputs/structure.png" width="700" height="500"> <br><br>

| Serial No. | Topics | 
| :--- | --- |
| 01 | Fetch the images data |
| 02 | Crop the images for the better predictions |
| 03 | Train the model |
| 04 | Save the model into the seprated file |
| 05 | Download and install the n-ginx |
| 06 | Create the front-end |
| 07 | Create the backend |
| 08 | Create the AWS accoun |
| 09 | Install the ngin-x on the server |
| 10 | Download WinSCP software to upload the all files on the server |
| 11 | Host the web-app |<br><br><br><br>

# Deploy this app to cloud (AWS EC2)

1. Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic
2. Now connect to your instance using a command like this,
```
ssh -i "C:\Users\shaik.ssh\gpfr.pem"  ubuntu@.us-east-2.compute.amazonaws.com
```
3. nginx setup
   1. Install nginx on EC2 instance using these commands,
   ```
   sudo apt-get update
   sudo apt-get install nginx
   ```
   2. Above will install nginx as well as run it. Check status of nginx using
   ```
   sudo service nginx status
   ```
   3. Here are the commands to start/stop/restart nginx
   ```
   sudo service nginx start
   sudo service nginx stop
   sudo service nginx restart
   ```
   4. Now when you load cloud url in browser you will see a message saying "welcome to nginx" This means your nginx is setup and running.<br>
4. Now you need to copy all your code to EC2 instance. You can do this either using git or copy files using winscp. We will use winscp. You can download winscp from here: https://winscp.net/eng/download.php<br>
5. Once you connect to EC2 instance from winscp (instruction in a youtube video), you can now copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: **/home/ubuntu/FaceRecognizer**
6.  After copying code on EC2 server now we can point nginx to load our property website by default. For below steps,
    1. Create this file /etc/nginx/sites-available/bhp.conf. The file content looks like this,
    ```
    server {
	    listen 80;
            server_name bhp;
            root /home/ubuntu/faceRecognizer/UI;
            index app.html;
            location /api/ {
                 rewrite ^/api(.*) $1 break;
                 proxy_pass http://127.0.0.1:5000;
            }
    }
    ```
    
    2. Create symlink for this file in /etc/nginx/sites-enabled by running this command,
       
    ```
     sudo ln -s /etc/nginx/sites-available/gpfr.conf /etc/nginx/sites-enabled/
    ```
    
    3. Remove symlink for default file in /etc/nginx/sites-enabled directory,
    ```
    sudo unlink default
    ```
    4. Restart nginx,
    ```
    sudo service nginx restart
    ```
7. Now install python packages and start flask server
```
sudo apt-get install python3-pip
sudo pip3 install -r /home/ubuntu/faceRecognizer/server/requirements.txt
python3 /home/ubuntu/faceRecognizer/server/server.py
```
Running last command above will prompt that server is running on port 5000.<br>
8. Now just load your cloud url in browser (for me it was http://ec2-df.compute.amazonaws.com/) and this will be fully functional website running in production cloud environment<br><br>


# Terminal commands for a performing actions

| Serial No. | Commands | Descriptions|
| :--- | --- | --- |
| 01 | pwd | Show the present working directory| 
| 02 | ll  | Show the all the files in the directory| 
| 03 | ls | Show the all the folders in the directory | 
| 04 | less nginx.conf | Read the file| 
| 05 | press ‘q’ | This will enable you to enter command again.| 
| 06 | cd sites-enabled/ | Enter inside the folder | 
| 07 | sudo vim gpfr.conf  | Create the file | 
| 08 | press  'i' | Insert mode enable | 
| 09 |  esc | Exit from the insert mode | 
| 10 | :wq  | Save the file|<br><br><br><br>

# Functional Video





https://github.com/iamistiyak/Face-Recognizer-Classifier/assets/86108816/71ca0e12-e947-4a5c-a8e9-97d7a322aa9e

