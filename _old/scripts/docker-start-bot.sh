# 推理API默认已经启动
ERGO_PROJECT_DIR=$1
echo "Using Project Dir: "$ERGO_PROJECT_DIR
# 启动docker容器并启动bot
docker container stop ergo-bot-container
docker container rm ergo-bot-container
docker run \
-v $ERGO_PROJECT_DIR:/ErGo -v $ERGO_PROJECT_DIR/database/mongo:/mongo \
-itd --name ergo-bot-container ergo-bot /bin/bash
#--net=container:ergo-inference-service \
#-v /mnt/1/Projects/gif-reply/data/processed/dataset/gifs:/gifs \
# 启动mongo db
docker exec ergo-bot-container sh -c "screen -S mongodb -md mongod --dbpath /mongo --logpath /ErGo/logs/mongod.log --fork"
docker exec ergo-bot-container sh -c "sh /ErGo/scripts/start-bot.sh"
