#!/usr/bin/env bash
# This script sets up a server 

root_dir="/data"
data_root="/data/web_static"
release_dir="$data_root/releases"
shared_folder="$data_root/shared"
test_folder="$release_dir/test"
test_file="$test_folder/index.html"
current_f="$data_root/current"

sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get -y install nginx


sudo mkdir -p "$shared_folder" "$test_folder"
echo "Hello Nginx" | sudo tee "$test_file"

if [ -e "$current_f" ]; then
	sudo rm -v "$current_f"
fi

sudo ln -sf "$test_folder" "$current_f"
sudo chown -hR  ubuntu:ubuntu "$root_dir"
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx stop
sudo service nginx start
