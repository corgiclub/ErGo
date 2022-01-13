create table chat
(
    id          bigint                                                            not null,
    group_id    bigint      default 0                                             not null comment '群 id',
    user_id     bigint      default 0                                             not null comment '用户 qq',
    message_id  int         default 0                                             null comment 'nonebot 内部消息ID',
    type        varchar(10) default ''                                            not null comment '消息段类型',
    add_time    datetime    default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime    default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int         default 0                                             not null comment '删除时间'
)
    comment '聊天表';

create table chat_text
(
    id          bigint                                                              not null,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    text        varchar(1023) default ''                                            not null comment 'text',
    add_time    datetime      default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间'
)
    comment '聊天表';

create table chat_face
(
    id          bigint                                                         not null,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    face_id     bigint   default 0                                             not null comment 'QQ 表情 ID',
    add_time    datetime default CURRENT_TIMESTAMP                             not null comment '添加时间',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间'
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
    delete_time int           default 0                                             not null comment '删除时间'
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
    delete_time int           default 0                                             not null comment '删除时间'
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
    delete_time int           default 0                                             not null comment '删除时间'
)
    comment 'chat_video';

create table chat_at
(
    id          bigint                                                         not null,
    chat_id     bigint   default 0                                             not null comment 'chat id',
    qq          bigint   default 0                                             not null comment 'at 的 QQ 号（1 表示 at 全体）',
    update_time datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int      default 0                                             not null comment '删除时间'
)
    comment 'chat_at';


create table chat_poke
(
    id          bigint                                                            not null,
    chat_id     bigint      default 0                                             not null comment 'chat id',
    type        tinyint(4)  default 0                                             not null comment '戳一戳类型',
    qq          bigint      default 0                                             not null comment '戳一戳动作 ID',
    name        varchar(10) default ''                                            not null comment '戳一戳表情名',
    update_time datetime    default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int         default 0                                             not null comment '删除时间'
)
    comment 'chat_poke';



create table chat_share
(
    id          bigint                                                              not null,
    chat_id     bigint        default 0                                             not null comment 'chat id',
    url         varchar(1023) default ''                                            not null comment '分享链接',
    title       varchar(255)  default ''                                            not null comment '分享标题',
    update_time datetime      default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP not null comment '修改时间',
    delete_time int           default 0                                             not null comment '删除时间'
)
    comment 'chat_share';
