## 数据库

- DataBase
  - InteractionObjects
    
    记录所有与 bot 交互过、与 bot 共处一个群的用户数据。
    
    - groups
      - group_id `int`
      - group_names `list[str]`
    - users
      - user_id `int`
      - user_names `list[str]`
    - user_groups `list[int]`
    
  - GroupChats
    
  记录群聊内容，每个群聊一张表。
    
    - [Group.id]
  
      - user_id `int`
    - source`int`
      - type `str` <img src="http://chart.googleapis.com/chart?cht=tx&chl=\in" style="border:none;"> ['Plain', 'Quote', ...]
    - content `str`
      - is_instruction `bool`
    - is_bot `bool`
    
    - [Group.id]
    
      | _id  | user_id   | source    | type  | content                          | is_instruction            | is_bot      |
      | ---- | --------- | --------- | ----- | -------------------------------- | -------------------------------- | -------------------------------- |
      |      | Member.id | Source.id | Plain | Plain.text                       | `False`       | `False`                |
      |      | Member.id | Source.id | Quote    | Quote.targetId | `False` | `False` |
      |      | Member.id | Source.id | At       | At.target                        | `False`                 | `False`                 |
      |      | Member.id | Source.id | AtAll    | `None` | `False` | `False` |
      |      | Member.id | Source.id | Face     | Face.faceId | `False` | `False` |
      |      | Member.id | Source.id | Image    | Image.imageId[1: -7] | `False` | `False` |
      |      | ~~Member.id~~ | ~~Source.id~~ | ~~FlashImage~~ | ~~FlashImage.imageId~~ | ~~`False`~~ | ~~`False`~~ |
      |      | ~~Member.id~~ | ~~Source.id~~ | ~~Voice~~  | ~~Voice.voiceId~~ | ~~`False`~~ | ~~`False`~~ |
      |      | Member.id | Source.id | Xml        | Xml.xml | `False` | `False` |
      |      | Member.id | Source.id | Json | Json.Json | `False` | `False` |
      |      | Member.id | Source.id | App | App.content | `False` | `False` |
      |      | Member.id | Source.id | Poke | Poke.PokeMethods | `False` | `False` |
    
  - Images
    - ImageInGroupMessage
      - content `byte`
      - mentioned_times `int`
      - is_porn `float`
    - AnimeImagePixiv
      - content `byte`
      - pid `int`
      - author_id `int`
      - is_porn `float`
      - tag `List[str]`
    - AnimeImageTwitter
      - content `byte`
      - url `str`
      - author_id `str`
      - is_porn `float`
      - tag `List[str]`
