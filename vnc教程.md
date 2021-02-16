### 准备工作

- 下载 [gitbash](https://github-releases.githubusercontent.com/23216272/9d5ae680-6ae4-11eb-949c-9a5528f8df81?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20210216%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210216T091543Z&amp;X-Amz-Expires=300&amp;X-Amz-Signature=f102e0a8b7bf081a8f378c8813469115f0b917f4c81431545baa3fee5bcec371&amp;X-Amz-SignedHeaders=host&amp;actor_id=38696052&amp;key_id=0&amp;repo_id=23216272&amp;response-content-disposition=attachment%3B%20filename%3DGit-2.30.1-64-bit.exe&amp;response-content-type=application%2Foctet-stream) 并安装

- 下载 [VNCViewer](https://www.realvnc.com/download/file/viewer.files/VNC-Viewer-6.20.529-Windows.exe) 并安装

- 下载群文件内的 corgitechnonroot corgitechnonroot.pub 和 config，放入 用户/.ssh 目录
  如 C:\Users\\{user_name}\\.ssh\

- 用记事本打开config，按下面格式修改

  ```bash
  Host corgitech
      HostName tech.corgi.plus
      User lune								# 修改为你的用户名
      Port 2222
      IdentityFile ~/.ssh/corgitechnonroot
  
  ```

### 连接

- 打开 gitbash

- 运行指令 `ssh corgitech` 

- 运行指令 `vncserver` ，第一次运行时会要求设置密码，设置长度小于等于8的密码并重复确认，看到

  ```bash
  Desktop 'TurboVNC: corgitech-server:8 (corgitech)' started on display corgitech-server:8
  
  Starting applications specified in /home/corgitech/.vnc/xstartup.turbovnc
  Log file is /home/corgitech/.vnc/corgitech-server:8.log
  ```
  
  则此时我们的端口开在了 5908。
  
- 再次打开config，在最后一行加上 `LocalForward 5908 localhost:5908`（注意缩进），保存后在gitbash按 `ctrl+D` 退出，再次使用 `ssh corgitech` 连接。

- 打开 VNCViewer，在顶端输入 localhost:5908，回车后输入访问密码，则进入桌面。

- 暂时没有中文输入法，之后安装。

- 注意：

  - 在连接时 gitbash 不能关闭
  - 运行3D程序时需要从 terminal 运行，前加 vglrun。
  - 安装大型程序需要在群里提出，管理员使用root权限安装在系统路径，避免磁盘空间浪费。

### iPad 连接

- 之后再写，我先研究研究。

