#!/usr/bin/env bash
# This script sets up a server 

root_dir="/data"
data_root="/data/web_static"
release_dir="$data_root/releases"
shared_folder="$data_root/shared"
test_folder="$release_dir/test"
test_file="$test_folder/index.html"
current_f="$data_root/current"

apt-get -y update && apt-get -y upgrade
apt-get -y install nginx


mkdir -p "$shared_folder" "$test_folder"
echo "Hello Nginx" > "$test_file"

if [ -e "$current_f" ]; then
	rm -v "$current_f"
fi

ln -sf "$test_folder" "$current_f"
chown -hR  ubuntu:ubuntu "$root_dir"
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx stop
service nginx start
