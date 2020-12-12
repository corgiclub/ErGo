# 推理API默认已经启动

# 启动docker容器并启动bot
docker container stop ergo-bot-container
docker container rm ergo-bot-container
docker run --net=container:ergo-inference-service \
-v /home/xingyaow/Projects/ErGo:/ErGo -v /home/xingyaow/Projects/ErGo/database/mongo:/mongo \
-v /mnt/1/Projects/gif-reply/data/processed/dataset/gifs:/gifs \
-itd --name ergo-bot-container ergo-bot /bin/bash
# 启动mongo db
docker exec ergo-bot-container sh -c "screen -S mongodb -md mongod --dbpath /mongo --logpath /ErGo/logs/mongod.log --fork"
docker exec ergo-bot-container sh -c "sh /ErGo/scripts/start-bot.sh"
