# ErGo - 一个基于 Garia 的测试性 qq-bot

A qq-bot named 二狗, powered by mirai / Garia.

> Cogito, ergo sum.
>
> 我思，故我在。

## 运行方法

build bot 所需 docker 镜像: `cd script/docker-image; sh docker-build.sh`

运行 bot 容器并启动 bot: `sh scripts/docker-start-bot.sh`

仅运行 bot 容器环境(debug 使用): `sh scripts/docker-run.sh`

接入正在运行的 bot 容器: `docker attach ergo-bot-container`

退出正在运行的 bot 容器（不可直接 ctrl+c 或 ctrl+d）: ctrl+p ctrl+q

## Todo list

#### Bot 功能

- [ ] pixiv 搜图
- [ ] 推特相关功能
- [ ] 备忘录，自动提醒

- [ ] 视频详细信息（小程序支持）
- [ ] 聊天记录保存至数据库

#### 现有待修复 BUG

- 视频详细信息功能对短链接的支持
- config 加载函数逻辑优化
- 存储 gif 时帧率错误修复（疑似丢失了帧间隔信息？

## 依赖

### CPM-LM-TF2 中文预训练 GPT 模型

源码: https://github.com/qhduan/CPM-LM-TF2

模型下载链接: https://pan.baidu.com/s/1tjbWty2hkbmtCrvV9Qh_SQ 密码: n0nt
--来自百度网盘超级会员 V7 的分享

or GDrive：

https://drive.google.com/drive/folders/1b2sF5sBuR_9zsT8UUijdsAcmFaMZJlpX?usp=sharing
