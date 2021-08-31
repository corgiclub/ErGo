# ErGo

A qq-bot named 二狗, 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) / [nonebot2](https://github.com/nonebot/nonebot2)

持续开发中。

> Cogito, **ergo** sum.
>
> 我思，**故**我在。

## Bot 功能

###### 所有功能均可定制 / 可选开启（划去的为重构计划迁移，但还暂时未实现的功能）

- 💬 关键词回复
- ~~🧠 AI 续写（基于 CPM-LM）~~
- 🎥 Bilibil 视频信息查询
- 🔴 Bilibili 直播开播监控
- ~~📰 今日要闻~~
- 📃 聊天记录存储至数据库
- 🧮 系统状态查询
- ~~🐔 复读鸡~~
- 🎈 今日人品
- 📋 更新日志
- 🕹️ 其他 debug 用功能

## 直接使用

- 本项目有多个生产环境版本长期部署在稳定服务器上，可直接加入群中提供各种功能。
- 插件权限和服务器压力问题解决后，会公布账号。

1. #### メテオラ<sup>Meteora</sup>
   
   - 账号：
   - 功能：全部
   - 当前版本：v2.0.3b
   
2. #### 臭狗

   - 账号：
   - 功能：脏话对骂
   - 当前版本：未稳定上线

## 本地运行

手动运行：

- 运行 go-cqhttp 服务
- clone 本 repo
- 安装 requirements
- 运行  `nb run`

Docker 运行（推荐）：

- 开发中

## Todo List

#### 9月

- [ ] 多来源搜图
- [ ] 权限管理
- [ ] 插件帮助

#### 之后

- [ ] qq语音解码
- [ ] RSS订阅推送
- [ ] 备忘录
- [ ] 小游戏（9路围棋，五子棋，黑白棋，象棋，赛马）
- [ ] 画一个logo

## 参考项目及插件

Bot 在编写过程中，参考 / 学习 / 使用了以下项目，在此列出并感谢这些项目作者的工作。

- [bilibili-api](https://github.com/MoyuScript/bilibili-api)

Bot 在编写过程中，参考学习了以下插件的源码。为使用更为简洁的项目环境管理方法，并使对应功能在本 bot 环境下更好地工作，本项目未直接引用其他插件，而是将参考的 nonebot 插件在其源代码的基础上进行了一定的修改重构，并集成进本 repo 的项目文件中。

- [NoneBot Plugin APScheduler](https://github.com/nonebot/plugin-apscheduler)
- [nonebot_plugin_analysis_bilibili](https://github.com/mengshouer/nonebot_plugin_analysis_bilibili)

## 其他资源

Bot 在运行过程中，（有选择地）使用了以下列出的免费开放资源。

以下资源在部分 branch 中作为插件的依赖项使用，使用 docker 运行时将默认包含所需的依赖。若手动运行时出现报错，可检查是否存在以下资源缺失。

#### CPM-LM-TF2 中文预训练 GPT 模型

###### （仅 legacy branch 使用）

清源 CPM TensorFlow 版本 [github repo](https://github.com/qhduan/CPM-LM-TF2)

模型下载链接

- [百度云](https://pan.baidu.com/s/1tjbWty2hkbmtCrvV9Qh_SQ) 密码: n0nt

-  [GDrive](https://drive.google.com/drive/folders/1b2sF5sBuR_9zsT8UUijdsAcmFaMZJlpX?usp=sharing)

#### 小赖字体 / 小賴字體 / シャオライ / Xiaolai Font

###### （仅 legacy branch 使用）

A Chinese Font derived from SetoFont / Naikai Font / cjkFonts-AllSeto. 

一款衍生于濑户字体 / 内海字体 / cjkFonts 全濑体的中文字体。[github repo](https://github.com/lxgw/kose-font)