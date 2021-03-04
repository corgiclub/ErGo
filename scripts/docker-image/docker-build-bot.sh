#!/bin/sh
if [ ! -f "mongodb-linux-x86_64-ubuntu1804-4.4.2.tgz" ]; then
	wget http://downloads.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-4.4.2.tgz
fi
sudo docker build -t ergo-bot -f Dockerfile.bot .
