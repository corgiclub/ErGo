# ErGo
A qq-bot named 二狗, powered by mirai.

> Cogito, ergo sum.
>
> 我思，故我在。


## 一个基于Garia的测试性bot

#### Bot功能

pixiv搜图

备忘录

视频详细信息



### 数据库

库 / 表 / 字段设计待定

#### 用户数据库

    qq

#### 群聊数据库

##### 	群A表

	user_id	type    content     is_instruction

#### 多媒体数据库

##### 	ImageInGroupMessage（注意存储格式）

    content     mentioned_times     is_porn

##### 	AudioInGroupMessage

    content

##### 	AnimeImageHistory

	content	pid	twitter_url	is_porn	tag


#### 外置数据库