#!/usr/bin/env bash
# Serves web Content

sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello, World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo systemctl restart nginx
exit 0
