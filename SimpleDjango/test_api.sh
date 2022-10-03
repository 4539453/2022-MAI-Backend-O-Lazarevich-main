#!/usr/bin/bash

set -eu -o pipefail

echo "GET"
curl -X GET -H "Content-Type: application/json" \
	-d '{"key1":"value1", "key2":"value2"}' \
	http://192.168.122.108/api/

echo -e "\n\nPOST"
curl -X POST -H "Content-Type: application/json" \
	-d '{"key1":"value1", "key2":"value2"}' \
	http://192.168.122.108/api/

echo -e "\n\nPUT"
curl -X PUT -H "Content-Type: application/json" \
	-d '{"key1":"value1", "key2":"value2"}' \
	http://192.168.122.108/api/
