#!/bin/bash

ERGO_PROJECT_DIR=$( dirname "$(readlink -f -- "$0")" )
ERGO_PROJECT_DIR="${ERGO_PROJECT_DIR}/.."
# 此脚本应在docker容器内运行
cd $ERGO_PROJECT_DIR 
if [ ! -d "${ERGO_PROJECT_DIR}/logs" ]; then
	mkdir logs
fi
# 启动miral
if [ ! -d "${ERGO_PROJECT_DIR}/mirai" ]; then
	mkdir ${ERGO_PROJECT_DIR}/mirai
	#TODO: 添加miraiOK_linux-amd64下载指令，或取消.gitignore中mirai文件夹以及其中不涉及个人隐藏信息的文件，GitHub上原MiraiOK仓库提供的下载地址均已失效
fi
cd mirai
screen -md -S miraiOK ./miraiOK_linux-amd64
cd $ERGO_PROJECT_DIR
sleep 3
# 启动bot
screen -md -S bot bash -c 'python3 main.py 2>&1 | tee logs/bot.log'
