#!/usr/bin/bash

set -eu -o pipefail

if [ "$(ps aux | grep '[n]ginx')" != "" ]; then
	sudo kill $(ps aux | grep '[n]ginx' | awk '{print $2}')
fi
sudo /usr/sbin/nginx -c "$(pwd)/nginx.conf"
gunicorn --bind 192.168.122.108:8000 --workers=2 app:AppClass
