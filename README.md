# database description

## MySQL

## MongoDB
### Install
- [mongodb_install][1]windows的mongoDB下载地址。

![windows_install][2]

- **MongoDB for Windows 64-bit**适合64位的Windows Server 2008 R2, Windows 7, 及最新版本的Windows系统。
- **MongoDB for Windows 32-bit** 适合32位的Windows系统以及最新的Windows Vista。32位系统上MongoDB的数据库最大为2GB。
- **MongoDB for Windows 64-bit Legacy**适合64位的Windows Vista, Windows Server 2003, 以及Windows Server 2008。

- 根据下载的Windows系统下载的32位或者64位的`.msi`文件，下载后双击该文件，按操作提示安装即可。

![accept_license][3]

- 安装过程中，可以通过点击`"Custom"`(自定义)按钮来设置你的安装目录。

![custom_type][4]

- 自定类型的设置(`Custom_Setup`)

![custom_setup][5]

- `Browse ...` 自定义自己的MongoDB的安装路径。

![browse][6]

- `Install MongoDB Compass`: MongoDB的图形管理工具。

![mongodb_compass][7]

- 如果是跟JackDan一样的命令行爱好者就不用选中`install`了。如果比较欣赏图形化界面，那就选中`Install`。

![installed][8]

- 点击`installed`进行`mongodb`安装。

![install_status][9]

- 创建数据目录:
	- `MongoDB`将数据目录存储在`db`目录下。但是这个数据目录不会主动创建，在安装完成后需要创建它。数据目录应该放在根目录下(如: `C:\`或者`D:\`等)。
- 已经在`C`盘安装了`mongodb`，现在让我们创建一个`data`的目录然后在`data`目录里创建`db`目录。

```
c:\>cd c:\

c:\>mkdir data

c:\>cd data

c:\data>mkdir db

c:\data>cd db

c:\data\db>
```

- 可以通过`window`的资源管理器中创建这些目录，而不一定通过**命令行**。

- 命令行下运行`MongoDB`服务器:
- 为了从命令提示符下运行 MongoDB 服务器，你必须从 MongoDB 目录的 bin 目录中执行 mongod.exe 文件。
```
C:\mongodb\bin\mongod --dbpath c:\data\db
```

- 如果执行成功，会输出如下信息:
```
2018-04-30T18:59:19.589-0700 I CONTROL  [initandlisten] MongoDB starting : pid=5752 port=27017 dbpath=C:\software\MongoDB\MONGODB\Server\3.6\data\db 64-bit host=JackDan9-PC
2018-04-30T18:59:19.590-0700 I CONTROL  [initandlisten] targetMinOS: Windows 7/Windows Server 2008 R2
2018-04-30T18:59:19.591-0700 I CONTROL  [initandlisten] db version v3.6.4
2018-04-30T18:59:19.592-0700 I CONTROL  [initandlisten] git version: d0181a711f7e7f39e60b5aeb1dc7097bf6ae5856
2018-04-30T18:59:19.593-0700 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2o-fips  27 Mar 2018
2018-04-30T18:59:19.594-0700 I CONTROL  [initandlisten] allocator: tcmalloc
2018-04-30T18:59:19.595-0700 I CONTROL  [initandlisten] modules: none
2018-04-30T18:59:19.596-0700 I CONTROL  [initandlisten] build environment:
2018-04-30T18:59:19.597-0700 I CONTROL  [initandlisten]     distmod: 2008plus-ssl
2018-04-30T18:59:19.598-0700 I CONTROL  [initandlisten]     distarch: x86_64
2018-04-30T18:59:19.599-0700 I CONTROL  [initandlisten]     target_arch: x86_64
2018-04-30T18:59:19.602-0700 I CONTROL  [initandlisten] options: { storage: { dbPath: "C:\software\MongoDB\MONGODB\Server\3.6\data\db" } }
2018-04-30T18:59:19.628-0700 I -        [initandlisten] Detected data files in C:\software\MongoDB\MONGODB\Server\3.6\data\db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
2018-04-30T18:59:19.630-0700 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=372M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),cache_cursors=false,log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
2018-04-30T18:59:20.285-0700 I STORAGE  [initandlisten] WiredTiger message [1525139960:285506][5752:140731415552336], txn-recover: Main recovery loop: starting at 1/13312
2018-04-30T18:59:20.649-0700 I STORAGE  [initandlisten] WiredTiger message [1525139960:648751][5752:140731415552336], txn-recover: Recovering log 1 through 2
2018-04-30T18:59:20.914-0700 I STORAGE  [initandlisten] WiredTiger message [1525139960:913923][5752:140731415552336], txn-recover: Recovering log 2 through 2
2018-04-30T18:59:21.145-0700 I STORAGE  [initandlisten] WiredTiger message [1525139961:145078][5752:140731415552336], txn-recover: Set global recovery timestamp: 0
2018-04-30T18:59:21.289-0700 I CONTROL  [initandlisten]
2018-04-30T18:59:21.289-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-04-30T18:59:21.292-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-04-30T18:59:21.294-0700 I CONTROL  [initandlisten]
2018-04-30T18:59:21.296-0700 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2018-04-30T18:59:21.298-0700 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2018-04-30T18:59:21.300-0700 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2018-04-30T18:59:21.305-0700 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2018-04-30T18:59:21.307-0700 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2018-04-30T18:59:21.308-0700 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2018-04-30T18:59:21.310-0700 I CONTROL  [initandlisten]
2018-04-30T18:59:21.312-0700 I CONTROL  [initandlisten]
2018-04-30T18:59:21.314-0700 I CONTROL  [initandlisten] ** WARNING: The file system cache of this machine is configured to be greater than 40% of the total memory. This can lead to increased memory pressure and poor performance.
2018-04-30T18:59:21.318-0700 I CONTROL  [initandlisten] See http://dochub.mongodb.org/core/wt-windows-system-file-cache
2018-04-30T18:59:21.319-0700 I CONTROL  [initandlisten]
2018-05-01T09:59:22.754+0800 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory 'C:/software/MongoDB/MONGODB/Server/3.6/data/db/diagnostic.data'
2018-05-01T09:59:22.759+0800 I NETWORK  [initandlisten] waiting for connections on port 27017
2018-05-01T09:59:34.316+0800 I NETWORK  [listener] connection accepted from 127.0.0.1:55779 #1 (1 connection now open)
2018-05-01T09:59:34.321+0800 I NETWORK  [conn1] received client metadata from 127.0.0.1:55779 conn1: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "3.6.4" }, os: { type: "Windows", name: "Microsoft Windows 10", architecture: "x86_64", version: "10.0 (build 16299)" } }
...

```

- 链接MongoDB
- 可以在命令行窗口中运行`mongo.exe`命令即可连接上`MongoDB`, 执行如下命令:
```
C:\mongodb\bin\mongo.exe
```
- 当然也可以将`mongodb`的配置到环境变量中去的

![mongo_home][10]

- `mongo_home`:

![mongo_home_sec][11]

- 配置 MongoDB 服务
- 管理员模式打开命令行窗口
- 创建目录，执行下面的语句来创建**数据库**和**日志文件**的目录
```
mkdir c:\data\db
mkdir c:\data\log
```
- 创建配置文件
- 创建一个配置文件。该文件必须设置`systemLog.path参数，包括一些附加的配置选项更好。
- 例如，创建一个配置文件位于`C:\mongodb\mongod.cfg`, 其中指定`systemLog.path`和`storage.dbPath`。具体配置内容如下:
```
systemLog:
    destination: file
    path: c:\data\log\mongod.log
storage:
    dbPath: c:\data\db
```

- 安装 MongoDB 服务
- 通过执行`mongod.exe`, 使用`--install`选项来安装服务，使用`--config`选项来指定之前创建的配置文件。
```
C:\mongodb\bin\mongod.exe --config "C:\mongodb\mongod.cfg" --install
```
- 要使用备用`dbpath`, 可以在配置文件(例如: `C:\mongodb\mongod.cfg`)或者命令通过`--dbpath`选项指定。
- 如果需要，可以安装`mongod.exe`和`mongos.exe`的多个实例的服务。只需要通过使用`--serviceName`和`--serviceDisplayName`指定不同的实例名。只有当存在足够的系统资源和系统的设计需要这么做。
- 启动`MongoDB`服务
```
net start MongoDB
```
- 关闭`MongoDB`服务
```
net stop MongoDB
```
- 移除`MongoDB`服务
```
C:\mongodb\bin\mongod.exe --remove
```

> **命令行下运行 MongoDB 服务器 和 配置 MongoDB 服务** 任选一个方式启动就可以。

- **MongoDB 后台管理 Shell**
- 如果需要进入MonoDB的后台管理，需要先打开`mongodb`装目录的下的`bin`目录，然后执行`mongo.exe`文件，`MongoDB Shell`是`MongoDB`自带的交互式`Javascript shell`, 用来对`MongoDB`进行操作和管理的交互环境。
- 当你进入`MongoDB`后台后，它默认会链接到`test`文档(数据库):
```
> mongo
MongoDB shell version: 3.0.6
connecting to: test
……
```

- 由于它是一个`Javascript shell`, 可以运行一些简单的算术运算:
```
> 2 + 2
4
>
```

- **db**命令用于查看当前操作的文档(数据库):
```
> db
test
>
```
- 插入一些简单的记录并查找它:
```
> db.runoob.insert({x:10})
WriteResult({ "nInserted" : 1 })
> db.runoob.find()
{ "_id" : ObjectId("5604ff74a274a611b0c990aa"), "x" : 10 }
>
```
- 第一个命令将数字` 10 `插入到` runoob `集合的` x `字段中。

  [1]: https://www.mongodb.com/download-center#community
  [2]: ./images/install_windows.png "install_windows"
  [3]: ./images/accept_license.png "accept_license"
  [4]: ./images/custom_type.png "custom_type"
  [5]: ./images/custom_setup.png "custom_setup"
  [6]: ./images/browse.png "browse"
  [7]: ./images/mongodb_compass.png "mongodb_compass"
  [8]: ./images/installed.png "installed"
  [9]: ./images/install_status.png "install_status"
  [10]: ./images/mongo_home.png "mongo_home"
  [11]: ./images/Mongo_Home_Sec.png "Mongo_Home_Sec"