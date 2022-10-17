#!/usr/bin/bash

set -eu -o pipefail

if [ "$(ps aux | grep '[n]ginx')" != "" ]; then
	sudo kill $(ps aux | grep '[n]ginx' | awk '{print $2}')
fi

workdir="$(git rev-parse --show-toplevel)/SimpleDjango"

sudo /usr/sbin/nginx -c "$workdir/nginx/nginx.conf"

export POSTGRES_NAME=films
export POSTGRES_USER=filmadmin
export POSTGRES_PASSWORD=P@ssword
export POSTGRES_HOST=localhost

"$workdir/manage.py" runserver 192.168.122.108:8000
