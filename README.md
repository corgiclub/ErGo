# ErGo - 一个基于 Garia 的测试性 qq-bot

A qq-bot named 二狗, powered by mirai / Garia.

> Cogito, ergo sum.
>
> 我思，故我在。

## Bot 功能

###### 所有功能均可定制 / 可选开启

💬 关键词回复

🧠 AI 续写（基于 CPM-LM ）

🖇 视频信息查询（ ✅ Bilibili / ➖ youtube）

📃 聊天记录存储至数据库

💾 系统信息 / 状态查询

## 运行方法

build bot 所需 docker 镜像: `cd script/docker-image; sh docker-build.sh`

运行 bot 容器并启动 bot: `sh scripts/docker-start-bot.sh`

仅运行 bot 容器环境(debug 使用): `sh scripts/docker-run.sh`

接入正在运行的 bot 容器: `docker attach ergo-bot-container`

退出正在运行的 bot 容器（不可直接 ctrl+c 或 ctrl+d）: ctrl+p ctrl+q

## Todo list

- [ ] pixiv 搜图 ← 工作中
- [ ] 推特搜图、记录相关功能
- [ ] 每日要闻
- [ ] 备忘录，自动提醒
- [ ] 视频详细信息（小程序、直播间、youtube 支持）
- [x] 聊天记录保存至数据库
- [ ] 小游戏（9路围棋，五子棋，黑白棋，象棋，赛马）
- [ ] 画一个logo

#### 待修复 BUG

- 视频详细信息功能对短链接的支持存在判断问题
- config 加载函数逻辑优化
- ~~存储 gif 时帧率错误修复（疑似丢失了帧间隔信息？~~

## 依赖

### CPM-LM-TF2 中文预训练 GPT 模型

源码: https://github.com/qhduan/CPM-LM-TF2

模型下载链接: https://pan.baidu.com/s/1tjbWty2hkbmtCrvV9Qh_SQ 密码: n0nt

or GDrive：https://drive.google.com/drive/folders/1b2sF5sBuR_9zsT8UUijdsAcmFaMZJlpX?usp=sharing

