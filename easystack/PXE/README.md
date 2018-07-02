# PXE

## 定义
- `PXE`(preboot execute environment, 预启动执行环境)是由Intel公司开发的最新技术, 工作于`Client/Server`的网络模式, 支持工作站通过网络从远端服务器下载镜像, 并由此支持通过网络启动操作系统, 在启动过程中, 终端要求服务器分配IP地址, 再用`TFTP(trivial file transfer protocol)`或者`MTFTP(multicast trivial file transfer protocol)`协议下载一个启动软件包到本机内存中执行, 由这个启动软件包完成终端(客户端)基本软件设置, 从而引导预先安装在服务器中的终端操作系统。PXE可以引导多种操作系统, 如: `Windows95/98/2000/windows2003/windows2008/winXP/win7/win8`,`linux`系列系统等。
- 严格来说, `PXE`不是一种安装方式, 而是一种引导方式。进行PXE安装的必要条件是在要安装的计算机中必须包含一个PXE支持的网卡(NIC), 即网卡中必须要有PXE Client。PXE协议可以使计算机通过网络启动。此协议分为Client端和Server端, 而PXE Client则在网卡的ROM中。当计算机引导时, BIOS把PXE Client调入内存中执行, 然后由PXE Client将放置在远端的文件通过网络下载到本地运行。运行PXE协议需要设置DHCP服务器和TFTP服务器。DHCP服务器会给PXE Client(将要安装系统的主机)分配一个IP地址, 由于是给PXE Client分配IP地址, 所以在配置DHCP服务器时需要增加相应的PXE设置。此外, 在PXE Client的ROM中, 已经存在了TFTP Client, 那么它就可以通过TFTP协议到TFTP Server上下载所需的文件了。

------

## PXE的工作过程
- PXE Client从自己的PXE网卡启动, 向本网络中的DHCP服务器索取IP;
- DHCP服务器返回分配给客户机的IP以及PXE文件的放置位置(该文件一般是放在一台TFTP服务器上);
- PXE Client向本网络中的TFTP服务器索取pxelinux 0文件;
- PXE Client取得pxelinux 0文件之后执行该文件;
- 根据pxelinux 0的执行结果, 通过TFTP服务器加载内核和文件系统;
- 进入安装画面, 此时可以通过选择HTTP、FTP、NFS方式之一进行安装;
- 详细工作流程, 参考下图:

![detailed_workflow][1]



------

## Kickstart
- `Kickstart`是一种无人值守的安装方式。它的工作原理是在安装过程中记录典型的需要人工干预填写的各种参数, 并生成一个名为ks.cfg的文件。如果在安装过程中(不只局限于生成Kickstart安装文件的机器)出现要填写参数的情况, 安装程序首先会查找Kickstart生成的文件, 如果找到合适的参数, 就采用所找到的参数; 如果没有找到合适的参数, 便需要安装者手工干预了。所以, 如果Kickstart文件涵盖了安装过程中可能出现的所有需要填写的参数, 那么安装者完全可以只告诉安装程序从何处取ks.cfg文件, 然后就去忙自己的事情。等安装完毕会根据ks.cfg中的设置重启系统, 并结束安装。

- PXE+Kickstart无人值守安装操作系统完整过程如下:

![PXE+Kickstart][2]

------

## 表现形式
- `PXE`最直接的表现是, 在网络环境下工作站可以省去硬盘, 但又不是通常所说的无盘站的概念, 因为使用该技术的PC在网络方式下的运行速度要比有盘PC快3倍以上。当然使用`PXE`的PC也不是传统意义上的`TERMINAL`终端, 因为使用了PXE的PC并不消耗服务器的CPU, RAM等资源, 故服务器的硬件要求极低。


> https://blog.csdn.net/qq_32907349/article/details/53057544


  [1]: ./images/work.jpg "work.jpg"
  [2]: ./images/PXE+kickstart.jpg "PXE+kickstart.jpg"