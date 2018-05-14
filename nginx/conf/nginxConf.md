# nginxConf
## user
- 语法: `user user[group];`;
- 标签: `main`;
- 作用: 定义`user`和工作`group`进程使用的凭证。如果`group`省略, `user`则使用名称等于的组。
- 默认: `#user nobody;`;
- 简略含义: 定义使用的`user`和`group`。
- **注意**: `nginx.conf`中的配置语句必须是以`;`结尾。

------

## worker_process
- 语法: `work_process number | auto;`;
- 标签: `main`;
- 作用: 指定工作衍生进程数(一般等于`CPU`的总数或者总核数两倍);
- 默认: `work_process 1;`;

## worker_process(example):
```
worker_process 4;
worker_cpu_affinity 0001 0010 0100 1000;
```

- 将工作进程绑定到**`CPU`集合**。每个**`CPU`集合**由允许的CPU的掩码表示。应该为**每个工作进程**定义一个单独的集合。默认情况下，工作进程不绑定到任何的`CPU`。

## 绑定每个工作进程到一个单独的CPU
```
worker_process 2;
worker_cpu_affinity 0101 1010;
```

------

## error.log
- 语法: `error_log file [level];`;
- 完整语法: `error_log file | stderr | syslog:server=address[,parameter=value] [debug | info | notice | warn | error | crit | alert | emerg];`;
- 可用标签: `main`, `http`, `mail`, `stream`, `server`, `location`;
- 默认: `error_log logs/error.log error;`;
- 配置日志目录。可以在同一级别上指定多个日志(`1.5.2`)。如果在`main`配置级别上, 未明确定义将日志写入文件, 将使用默认文件。
- 第一个参数定义`file`将存储日志。特殊值`stderr`选择标准错误文件。可以通过指定`" "`前缀来配置日志记录到`syslog:syslog`。可以通过指定`" "`前缀和缓冲区来配置对循环内存缓冲区的日志记录，并且通常用于调试(1.7.11)。`memory:size`。
- 第二个参数决定了`level`的日志记录, 并且可以是下列之一: `debug`, `info`, `notice`, `warn`, `error`, `crit`, `alert`, `emerg`。以上的日志级别按严重性递增的顺序列出。设置特定日志级别将导致记录指定日志级别和更严重日志级别的所有消息。例如，默认级别`error`会导致`error`, `crit`, `alert`和`emerg`被记录的消息。如果省略此参数，则`error`被使用。

------

## nginx.pid
- 课外知识`pid`: 全称`Proportion Integration Differentiation`, `PID=port ID`, 在`STP`(生成树协议)中, 若在端口收到的`BPDU`中`BID`和`path cost`相同时, 则比较`PID`来选择**阻塞端口**。数字电视复用系统名词`PID(Packet Identifier)` 在数字电视复用系统中它的作用好比一份文件的文件名, 我们可以称它为**"标志码传输包"** 。`PID`由8位端口优先级加端口号组成, 端口号占低位, 默认端口号优先级128。
- 语法: `nginx.pid`路径;
- 标签: `main`;
- 作用: 指定`nginx.pid`的存放路径;
- 默认: `#pid    logs/nginx.pid;`

## nginx.pid(example)
```
/usr/local/nginx/logs/nginx.pid;
```

------

## worker_rlimit_nofile
- 语法: `worker_rlimit_nofile number;`
- 标签: `main`;
- 作用: 指定为`nginx`工作进程改变打开最多**文件描述符**数目的限制。用来在**不重启主进程**的情况下增加限制。
- 默认: `-`;
- 如果不设置的话上限就是系统的`ulimit -n`的数字, 一般设置`worker_connections`的`3-4`倍。

## worker_rlimit_nofile(example)
```
worker_rlimit_nofile 51200;
```

------

## events
- 语法: `events {}`
- 定义: `events`是`nginx`中的一个模块。
- 作用: `events`模块中包含`nginx`中所有处理连接的设置。
- 默认:
```
events {
    worker_connections 1024;
}
```

### use epoll
- 语法: `use epoll;`或者`use kqueue;`;
- 标签: `events`;
- 作用: 使用`epoll`的`I/O`模型或者使用`kqueue`(值得注意的是如果你不知道`nginx`该使用哪种轮询方法的话, 它会选择一个最适合你操作系统的)。
- 默认: `-`;
- 补充说明: 与`Apache`相类似, `nginx`针对与不同的操作系统, 有不同的事件模型;
- **标准事件模型**:
    - `select`、`poll`属于标准事件模型, 如果当前系统不存在更有效的方法, `nginx`会选择`select`或者`poll`;
- **高效事件模型**:
    - `kqueue`: 使用于`FreeBSD 4.1+`, `OpenBSD 2.9+`, `NetBSD 2.0`和`MacOS X`。使用双处理器的`MacOS X`系统使用`kqueue`可能会造成内核崩溃;
    - `epoll`: 使用于`linux`内核2.6版本以及以后的系统;
    - `/dev/poll`: 使用于`Solaris 7 11/99+`, `HP/UX 11.22+ (eventport)`, `IRIX 6.5.15+`和`Tru64 UNIX 5.1A+`;
    - `eventport`: 使用于`Solaris 10`。为了防止出现内核崩溃的问题, 有必要安装安全补丁;

### worker_connenctions 
- 语法: `worker_connections number;`;
- 标签: `events`;
- 作用: 工作进程的最大连接数量。理论上每台`nginx`服务器的最大连接数为`worker_processes * worker_conenctions`, `worker_processes`为我们在`nginx`的`main`中开启的进程数;
- 默认: `worker_connections 1024;`;

### multi_accept
- 语法: `multi_accept on;`或者`multi_accept off;`;
- 标签: `events`;
- 作用: 
    - 设置为`on`后, 多个`worker`按串行方式来处理连接, 也就是一个连接只有一个`worker`被唤醒, 其他的处于休眠状态。
    - 设置为`off`后, 多个`worker`按并行方式来处理连接, 也就是一个连接会唤醒所有的`worker`, 知道连接分配完毕, 没有取得连接的继续休眠。
    - 当你的服务器连接数不多时, 开启这个参数会让负载均衡有一定程度的降低。但是当服务器的吞吐量很大时, 为了效率, 请关闭这个参数。
- 默认: `multi_accept on;`;

------

## http模块


### client_header_buffer_size
- 语法: `client_header_buffer_size size;`; (szie为存储大小)
- 标签: `events`;
- 作用: 客户端请求头部的缓冲区大小, 这个可以根据你的系统分页来设置, 一般一个请求头的大小不会超过`1K`, 不过由于一般系统分页都要大于`1K`, 所以这里设置为系统分页大小。查看系统分页可以使用`getconf PAGESIZE`命令。
- 默认: `-`;







