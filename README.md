# ErGo

A qq-bot named 二狗, 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) / [nonebot2](https://github.com/nonebot/nonebot2)

绝赞重构中！

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

## 运行方法

手动运行：

- 运行 go-cqhttp 服务
- clone 本 repo
- 安装 requirements
- 运行  `nb run`

Docker 运行（推荐）：

- 开发中

## Todo list

- [x] 数据库功能
- [ ] pixiv 搜图
- [ ] 推特搜图
- [x] qq语音解码
- [ ] 备忘录，自动提醒
- [x] 直播提醒
- [ ] 小游戏（9路围棋，五子棋，黑白棋，象棋，赛马）
- [ ] 画一个logo

#### 待修复 BUG / issue

- 

## 其他依赖

### CPM-LM-TF2 中文预训练 GPT 模型

清源 CPM TensorFlow 版本 [github repo](https://github.com/qhduan/CPM-LM-TF2)

模型下载链接

- [百度云](https://pan.baidu.com/s/1tjbWty2hkbmtCrvV9Qh_SQ) 密码: n0nt

-  [GDrive](https://drive.google.com/drive/folders/1b2sF5sBuR_9zsT8UUijdsAcmFaMZJlpX?usp=sharing)

### 小赖字体 / 小賴字體 / シャオライ / Xiaolai Font

A Chinese Font derived from SetoFont / Naikai Font / cjkFonts-AllSeto. 

一款衍生于濑户字体 / 内海字体 / cjkFonts 全濑体的中文字体。[github repo](https://github.com/lxgw/kose-font)