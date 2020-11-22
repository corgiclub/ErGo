# ErGo

A qq-bot named 二狗, powered by mirai.

> Cogito, ergo sum.
>
> 我思，故我在。

## 运行方法

build bot 所需 docker 镜像: `cd script/docker-image; sh docker-build.sh`

运行 bot 容器并启动 bot: `sh scripts/docker-start-bot.sh`

仅运行 bot 容器环境(debug 使用): `sh scripts/docker-run.sh`

接入正在运行的 bot 容器: `docker attach ergo-bot-container`

退出正在运行的 bot 容器（不可直接 ctrl+c 或 ctrl+d）: ctrl+p ctrl+q

## 一个基于 Garia 的测试性 bot

#### Bot 功能

pixiv 搜图

备忘录

视频详细信息

### 数据库

库 / 表 / 字段设计待定

#### 用户数据库

    qq

#### 群聊数据库

##### 群 A 表

    user_id	type    content     is_instruction

#### 多媒体数据库

##### ImageInGroupMessage（注意存储格式）

    content     mentioned_times     is_porn

##### AudioInGroupMessage

    content

##### AnimeImageHistory

    content	pid	twitter_url	is_porn	tag

#### 外置数据库

## 依赖

### CPM-LM-TF2 中文预训练 GPT 模型

源码: https://github.com/qhduan/CPM-LM-TF2

模型下载链接: https://pan.baidu.com/s/1tjbWty2hkbmtCrvV9Qh_SQ 密码: n0nt
--来自百度网盘超级会员 V7 的分享

or GDrive：

https://drive.google.com/drive/folders/1b2sF5sBuR_9zsT8UUijdsAcmFaMZJlpX?usp=sharing
