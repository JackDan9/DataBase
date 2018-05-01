# database description

## MySQL
### Install

- [mysql_install][1]windows的mysql下载地址。

![mysql_install][2]

- 进入官网后，显示的应该是最新的版本，选择第二个(如图片所示)；
- 下载完成后，直接解压到**自定义**目录，**解压目录**就是**安装目录**。

------

## MongoDB
### Install
- [mongodb_install][3]windows的mongoDB下载地址。

![windows_install][4]

- **MongoDB for Windows 64-bit**适合64位的Windows Server 2008 R2, Windows 7, 及最新版本的Windows系统。
- **MongoDB for Windows 32-bit** 适合32位的Windows系统以及最新的Windows Vista。32位系统上MongoDB的数据库最大为2GB。
- **MongoDB for Windows 64-bit Legacy**适合64位的Windows Vista, Windows Server 2003, 以及Windows Server 2008。

- 根据下载的Windows系统下载的32位或者64位的`.msi`文件，下载后双击该文件，按操作提示安装即可。

![accept_license][5]

- 安装过程中，可以通过点击`"Custom"`(自定义)按钮来设置你的安装目录。

![custom_type][6]

- 自定类型的设置(`Custom_Setup`)

![custom_setup][7]

- `Browse ...` 自定义自己的MongoDB的安装路径。

![browse][8]

- `Install MongoDB Compass`: MongoDB的图形管理工具。

![mongodb_compass][9]

- 如果是跟JackDan一样的命令行爱好者就不用选中`install`了。如果比较欣赏图形化界面，那就选中`Install`。

![installed][10]

- 点击`installed`进行`mongodb`安装。

![install_status][11]

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


  [1]: http://dev.mysql.com/downloads/mysql/
  [2]: ./images/mysql_install.png "mysql_install.png"
  [3]: https://www.mongodb.com/download-center#community
  [4]: ./images/install_windows.png "install_windows"
  [5]: ./images/accept_license.png "accept_license"
  [6]: ./images/custom_type.png "custom_type"
  [7]: ./images/custom_setup.png "custom_setup"
  [8]: ./images/browse.png "browse"
  [9]: ./images/mongodb_compass.png "mongodb_compass"
  [10]: ./images/installed.png "installed"
  [11]: ./images/install_status.png "install_status"