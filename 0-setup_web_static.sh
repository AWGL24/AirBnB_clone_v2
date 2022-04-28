#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# create folders if they don't already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# created fake html file
echo "
<!DOCTYPE html>
<html>
<head>
</head>
<body>
Holberton School
</body>
</html> " > /data/web_static/releases/test/index.html

# created symlink
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gived ownership of data folder to ubuntu user and group
chown -hR ubuntu:ubuntu /data/

# Updates rge Nginx config to serve the content
sed -i "40 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# restarts nginx for the update to take effect
sudo service nginx restart