### 插件基本配置

- 聊天记录插件 priority=100
  - 任何 priority <= 100 插件不得使用 block=True，需手动设置 block=False
  - 为普通插件提供触发优先级，从而提高性能 (?)
- 普通触发插件 priority=10, block=False
- 高优先级插件 priority<10, block=False
- 需阻断插件 priority>100, block=True
- 需被阻断插件 priority >> 100, block=False