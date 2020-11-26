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
  - GroupChats
    - [Group.id]

      - user_id `int`
      - source`int`
      - type `str` <img src="http://chart.googleapis.com/chart?cht=tx&chl=\in" style="border:none;"> [plain, picture, audio, ...]
      - content `str`
      - is_instruction `bool`
      - is_bot `bool`

    - [Group.id]

      | _id  | user_id   | source    | type  | content                          | is_instruction            | is_bot      |
      | ---- | --------- | --------- | ----- | -------------------------------- | -------------------------------- | -------------------------------- |
      |      | Member.id | Source.id | Plain | Plain.text                       | `False`       | `False`                |
      |      | Member.id | Source.id | Quote    | [Quote.senderId, Quote.targetId] | `False` | `False` |
      |      | Member.id | Source.id | At       | At.target                        | `False`                 | `False`                 |
      |      | Member.id | Source.id | AtAll    | `None` | `False` | `False` |
      |      | Member.id | Source.id | Face     | Face.faceId | `False` | `False` |
      |      | Member.id | Source.id | Image    | Image.imageId | `False` | `False` |
      |      | Member.id | Source.id | FlashImage | FlashImage.imageId | `False` | `False` |
      |      | Member.id | Source.id | Voice      | Voice.voiceId | `False` | `False` |
      |      | Member.id | Source.id | Xml        | Xml.xml | `False` | `False` |
      |      | Member.id | Source.id | Json | Json.Json | `False` | `False` |
      |      | Member.id | Source.id | App | App.content | `False` | `False` |
      |      | Member.id | Source.id | Poke | Poke.PokeMethods | `False` | `False` |
    
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
