#!/bin/bash

apt-get update && apt-get upgrade -y

sudo apt-get remove docker docker-engine docker.io containerd runc

sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

apt-get install nginx -y

snap install core
snap refresh core
snap install docker
snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot

sudo certbot certonly --nginx

docker-compose -f /path/to/docker-compose.yml down
docker-compose -f /path/to/docker-compose.yml up -d

