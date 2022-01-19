create table chat
(
    id          bigint auto_increment,
    group_id    bigint      default 0                                             not null comment '群 id',
    user_id     bigint      default 0                                             not null comment '用户 qq',
    message_id  int         default 0                                             null comment 'nonebot 内部消息ID',
    type        tinyint(4)  default ''                                            not null comment '消息段类型',
    add_time    datetime    default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime    default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int         default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment '聊天表';

create table chat_text
(
    id          bigint                                                              not null,
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
    id          bigint                                                         not null,
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
    id          bigint                                                              not null,
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
    id          bigint                                                              not null,
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
    id          bigint                                                              not null,
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
    id          bigint                                                         not null,
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
    id          bigint                                                            not null,
    chat_id     bigint      default 0                                             not null comment 'chat id',
    type        tinyint(4)  default 0                                             not null comment '戳一戳类型',
    qq          bigint      default 0                                             not null comment '戳一戳动作 ID',
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
    id          bigint                                                              not null,
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
    id          bigint                                                           not null,
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
    id          bigint                                                         not null,
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
    id          bigint                                                         not null,
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
    id          bigint                                                         not null,
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
    id          bigint                                                              not null,
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
    id          bigint                                                              not null,
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
    id          bigint                                                             not null,
    filename    varchar(255) default ''                                            not null comment '文件名',
    suffix      tinyint(4)   default 0                                             not null comment '后缀名',
    p_hash      binary(32)   default 0                                             not null comment '图片 P 哈希',

    add_time    datetime     default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime     default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int          default 0                                             not null comment '删除时间',
    constraint table_name_pk
            primary key (id)
)
    comment 'image';

create table image_chat
(
    id          bigint                                                            not null,
    image_id    bigint      default 0                                             not null comment 'image id',
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
    id          bigint                                                              not null,

    thumbnail   varchar(1023) default ''                                            not null comment '临时预览链接',
    similarity  varchar(1023) default ''                                            not null comment '相似度',
    index_id    varchar(1023) default ''                                            not null comment 'index_id',
    index_name  varchar(1023) default ''                                            not null comment 'index_name',
    title       varchar(1023) default ''                                            not null comment '相似度',
    urls        varchar(1023) default ''                                            not null comment '找到的所有链接',
    author      varchar(1023) default ''                                            not null comment '作者',
    raw         varchar(1023) default ''                                            not null comment '原始结果',

    pixiv_id    bigint        default 0                                             not null comment 'P站 ID',
    twitter_id  varchar(1023) default ''                                            not null comment '推特 ID',
    image_id    bigint        default 0                                             not null comment 'image id',

    part        bigint        default 0                                             not null comment '动画集数',
    year        bigint        default 0                                             not null comment '年份',
    est_time    varchar(1023) default ''                                            not null comment '出现时间',

    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间',
    constraint table_name_pk
        primary key (id)
)
    comment 'image_sauce';

create table image_tag
(
    id          bigint                                                             not null,
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


