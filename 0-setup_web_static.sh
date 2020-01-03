#!/usr/bin/env bash
# Airbnb deploy

# Install nginx if doesn't exist
apt-get update
apt-get -y install nginx

# reate the folder /data/ if it doesn’t already exist
mkdir -p /data/

# Create the folder /data/web_static/ if it doesn’t already exist
mkdir -p /data/web_static

# Create the folder /data/web_static/releases/ if it doesn’t already exist
mkdir -p /data/web_static/releases/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
touch /data/web_static/releases/test/index.html
echo "
<head>
</head>
<body>
    Holberton School Test
</body>
</html>
" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
ln -fsn /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu. /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i "36i location /hbnb_static/ {" /etc/nginx/sites-available/default
sed -i "37i alias /data/web_static/current/;" /etc/nginx/sites-available/default
sed -i "38i autoindex off;" /etc/nginx/sites-available/default
sed -i "39i }" /etc/nginx/sites-available/default

# restart nginx
service nginx restart
