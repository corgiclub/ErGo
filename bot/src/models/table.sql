create table chat
(
    id          bigint auto_increment,
    group_id    bigint     default 0                                             not null comment '群 id',
    user_id     bigint     default 0                                             not null comment '用户 qq',
    message_id  int        default 0                                             null comment 'nonebot 内部消息ID',
    type_id     tinyint(4) default 0                                             not null comment '消息段类型',
    add_time    datetime   default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime   default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int        default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment '聊天表';

create table chat_text
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    text        varchar(1023) default ''                                            not null comment 'text',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_text';

create table chat_face
(
    id          bigint auto_increment,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    face_id     bigint   default 0                                             not null comment 'QQ 表情 ID',
    add_time    datetime default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_face';

create table chat_image
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    image_id    bigint        default 0                                             not null comment 'image_id',
    qq_hash     varchar(32)   default ''                                            not null comment 'QQ 返回的 hash 值',
    url         varchar(1023) default ''                                            not null comment '图片链接',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_image';


create table chat_record
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    file_url    varchar(1023) default ''                                            not null comment '音频文件链接',
    file_name   varchar(1023) default ''                                            not null comment '音频文件名',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_record';

create table chat_video
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    file_url    varchar(1023) default ''                                            not null comment '视频文件链接',
    file_name   varchar(1023) default ''                                            not null comment '视频文件名',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_video';

create table chat_at
(
    id          bigint auto_increment,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    qq          bigint   default 0                                             not null comment 'at 的 QQ 号（1 表示 at 全体）',
    add_time    datetime default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_at';


create table chat_poke
(
    id          bigint auto_increment,
    chat_id     bigint      default 0                                             not null comment 'chat id',
    type        tinyint(4)  default 0                                             not null comment '戳一戳类型',
    poke_id     bigint      default 0                                             not null comment '戳一戳动作 ID',
    name        varchar(10) default ''                                            not null comment '戳一戳表情名',
    add_time    datetime    default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime    default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int         default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_poke';

create table chat_share
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    url         varchar(1023) default ''                                            not null comment '分享链接',
    title       varchar(255)  default ''                                            not null comment '分享标题',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_share';

create table chat_contact
(
    id          bigint auto_increment,
    chat_id     bigint     default 0                                             not null comment 'chat id',
    type        tinyint(4) default 0                                             not null comment '戳一戳类型',
    contact_id  bigint     default 0                                             not null comment '被推荐人的 QQ 号 / 群号',
    add_time    datetime   default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime   default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int        default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_contact';

create table chat_location
(
    id          bigint auto_increment,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    lat         float    default 0                                             not null comment '纬度',
    lot         float    default 0                                             not null comment '经度',
    add_time    datetime default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_location';

create table chat_reply
(
    id          bigint auto_increment,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    message_id  bigint   default 0                                             not null comment '回复消息时引用的 ID',
    add_time    datetime default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_reply';

create table chat_forward
(
    id          bigint auto_increment,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    message_id  bigint   default 0                                             not null comment '合并转发 ID',
    add_time    datetime default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_forward';

create table chat_xml
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    data        varchar(1023) default ''                                            not null comment 'XML 内容',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_xml';

create table chat_json
(
    id          bigint auto_increment,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    data        varchar(1023) default ''                                            not null comment 'JSON 内容',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'chat_json';

create table image
(
    id           bigint auto_increment,
    url          varchar(255) default ''                                            not null comment '图片链接',
    filename     varchar(255) default ''                                            not null comment '文件名',
    type_id      tinyint(4)   default 0                                             not null comment '来源类型',
    suffix       varchar(4)   default ''                                            not null comment '后缀名',
    file_existed bool         default FALSE                                         not null comment '图片是否保存',
    p_hash       binary(32)   default 0                                             not null comment '图片 P 哈希',
    fix_count    tinyint(4)   default 0                                             not null comment '图片库修复次数',

    add_time     datetime     default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time  datetime     default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time  int          default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'image';

create table image_chat
(
    id          bigint auto_increment,
    image_id    bigint      default 0                                             not null comment 'image id',
    session_id  bigint      default 0                                             not null comment '群号',
    qq_hash     varchar(32) default ''                                            not null comment 'QQ 返回的 hash 值',
    qq_count    bigint      default 0                                             not null comment '总计发送次数',
    add_time    datetime    default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime    default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int         default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'image_chat';

create table image_sauce
(
    id          bigint auto_increment,

    similarity  float         default 0                                             not null comment '相似度',
    thumbnail   varchar(255)  default ''                                            not null comment '临时预览链接',
    index_id    bigint        default 0                                            not null comment 'index_id',
    index_name  varchar(255)  default ''                                            not null comment 'index_name',
    title       varchar(255)  default ''                                            not null comment '标题',
    url         varchar(255)  default ''                                            not null comment '找到的链接',
    author      varchar(50)   default ''                                            not null comment '作者',

    pixiv_id    bigint        default 0                                             not null comment 'P站 ID',
    image_id    bigint        default 0                                             not null comment 'image id',
    member_id   bigint        default 0                                             not null comment '作者 pixiv id',

    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'image_sauce';

create table image_tag
(
    id          bigint auto_increment,
    image_id    bigint       default 0                                             not null comment 'image id',
    tag_source  tinyint(4)   default 0                                             not null comment 'tag 来源',
    tag         varchar(255) default ''                                            not null comment 'tag 内容',

    add_time    datetime     default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime     default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int          default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'image_tag';

create table image_gallery
(
    id          bigint auto_increment,
    image_id    bigint      default 0                                             not null comment 'image id',
    theme       varchar(32) default ''                                            not null comment '图像主题',
    add_time    datetime    default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime    default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int         default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'image_gallery';

create table note
(
    id          bigint auto_increment,
    note        varchar(32)  default 0                                             not null comment '触发词',
    value       varchar(255) default ''                                            not null comment '回复',
    group_id    bigint       default 0                                             not null comment '群 id',
    add_time    datetime     default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime     default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int          default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'note';

create table image_pixiv
(
    id          bigint auto_increment,
    image_id    bigint        default 0                                             not null comment 'image id',


    pixiv_id    bigint        default 0                                             not null comment 'P站 ID',
    author_id   int           default 0                                             not null comment '作者 ID',
    title       varchar(255)  default ''                                            not null comment '标题',
    bookmarks   int           default 0                                             not null comment '收藏数',
    view        int           default 0                                             not null comment '点击数',
    illust_type varchar(32)   default ''                                            not null comment '图片类型',

    page_count  smallint      default 0                                             not null comment '页数',
    page        smallint      default 0                                             not null comment '页数',

    sanity_level tinyint      default 0                                             not null comment '限制级',
    x_restrict  bool          default FALSE                                         not null comment 'x级图片',

    image_url   varchar(255)  default ''                                            not null comment '原始图链接',
    create_date datetime      default CURRENT_TIMESTAMP                             not null comment '上传时间',

    add_time    datetime     default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime     default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int          default 0                                             not null comment '删除时间',

    constraint table_name_pk
        primary key (id)
)
    comment 'image_pixiv';
