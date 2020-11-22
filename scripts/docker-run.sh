docker container rm ergo-bot-container
docker run -v /home/xingyaow/Projects/ErGo:/ErGo -itd --name ergo-bot-container ergo-bot /bin/bash
