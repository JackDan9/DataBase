# database description

## MySQL
### Install

- [mysql_install][1]windows的mysql下载地址。

![mysql_install][2]

- 进入官网后，显示的应该是最新的版本，选择第二个(如图片所示)；
- 下载完成后，直接解压到**自定义**目录，**解压目录**就是**安装目录**。

- **配置环境变量**
- 1、新增环境变量, 例:
    - 变量名: MYSQL_HOME
    - 变量名: D:\mysql\mysql5.8.0-winx64
- 2、修改环境变量PATH
    - 在PATH后面加入%MYSQL_HOME%\bin，注: 加入新的变量值需要用`;`隔开

- **添加`my.ini`配置文件**
- 下载的压缩文件中没有`my.ini`配置文件和`data`文件夹，需要手动在`bin`目录下新建文本`my.ini`，如果放在根目录下，`data`不能自动生成。`my.ini`文件内容如下:
```
[client]  
default-character-set=utf8  
[mysqld]  
#解压目录   
basedir = %MYSQL_HOME%   
#解压目录   
datadir = %MYSQL_HOME%\data  
port = 3306   
default-character-set=utf8  
```

- **初始化`mysql`，启动`mysql`服务**
- 1.以管理员身份运行命令行`cmd`，进入`bin`目录（一定要进入bin目录），如下图所示:

![windows_admin][3]

- 例如: `cd D:\mysql\mysql5.9.0-winx64\bin`

- 2.输入命令 (生成无密码的root用户)：`mysqld --initialize-insecure`
- 会在根目录下生成一个`data`文件夹，里面有文件，表示初始化成功。


- 3.`mysqld --install` 安装`mysql`文件。

- 4.启动服务：`net start mysql`，停止服务：`net stop mysql` 出现mysql服务已启动说明成功。

- 5.设置mysql密码
```
mysqladmin -u root password 你的密码
```
- 6.使用密码登录mysql
```
mysql -u root -p
```
会提示你输入密码，输入即可。
- 7.退出mysql服务
```
exit
```
- 8.如果想移除mysql服务，
```
mysql --remove
```

------

## MongoDB
### Install
- [mongodb_install][4]windows的mongoDB下载地址。

![windows_install][5]

- **MongoDB for Windows 64-bit**适合64位的Windows Server 2008 R2, Windows 7, 及最新版本的Windows系统。
- **MongoDB for Windows 32-bit** 适合32位的Windows系统以及最新的Windows Vista。32位系统上MongoDB的数据库最大为2GB。
- **MongoDB for Windows 64-bit Legacy**适合64位的Windows Vista, Windows Server 2003, 以及Windows Server 2008。

- 根据下载的Windows系统下载的32位或者64位的`.msi`文件，下载后双击该文件，按操作提示安装即可。

![accept_license][6]

- 安装过程中，可以通过点击`"Custom"`(自定义)按钮来设置你的安装目录。

![custom_type][7]

- 自定类型的设置(`Custom_Setup`)

![custom_setup][8]

- `Browse ...` 自定义自己的MongoDB的安装路径。

![browse][9]

- `Install MongoDB Compass`: MongoDB的图形管理工具。

![mongodb_compass][10]

- 如果是跟JackDan一样的命令行爱好者就不用选中`install`了。如果比较欣赏图形化界面，那就选中`Install`。

![installed][11]

- 点击`installed`进行`mongodb`安装。

![install_status][12]

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
  [3]: ./images/windows_admin.png "windows_admin.png"
  [4]: https://www.mongodb.com/download-center#community
  [5]: ./images/install_windows.png "install_windows"
  [6]: ./images/accept_license.png "accept_license"
  [7]: ./images/custom_type.png "custom_type"
  [8]: ./images/custom_setup.png "custom_setup"
  [9]: ./images/browse.png "browse"
  [10]: ./images/mongodb_compass.png "mongodb_compass"
  [11]: ./images/installed.png "installed"
  [12]: ./images/install_status.png "install_status"