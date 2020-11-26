## 数据库

库 / 表 / 字段设计待定

- DataBase
  - InteractionObjects
    - groups
      - group_id `int`
      - group_names `list[str]`
    - users
      - user_id `int`
      - user_names `list[str]`
      - user_groups `list[int]`
  - GroupChat
    - [group_id]
      - user_id `int`
      - type `str` <img src="http://chart.googleapis.com/chart?cht=tx&chl=\in" style="border:none;"> [text, picture, audio, ...]
      - content `str`
      - is_instruction `bool`
      - is_bot `bool`
    - [group_id]
      - ...
  - Multimedia
    - ImageInGroupMessage
      - content `byte`
      - mentioned_times `int`
      - is_porn `float`



待续↑



#### 用户数据库

记录所有与 bot 交互过、与 bot 共处一个群的用户数据，闲时更新。

    qq  ...

#### 群聊数据库

记录群聊内容，每个群聊一张表。

##### 群 A 表

    user_id    type    content     is_instruction    is_bot

#### 多媒体数据库

##### ImageInGroupMessage（注意存储格式）

    content     mentioned_times     is_porn

##### AudioInGroupMessage

    content

##### AnimeImageHistory

    content    pid    twitter_url    is_porn    tag

#### 外置数据库
