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
	- MongoDB将数据目录存储在`db`目录下。但是这个数据目录不会主动创建，在安装完成后需要创建它。数据目录应该放在根目录下(如: `C:\`或者`D:\`等)。
  


  [1]: https://www.mongodb.com/download-center#community
  [2]: ./images/install_windows.png "install_windows"
  [3]: ./images/accept_license.png "accept_license"
  [4]: ./images/custom_type.png "custom_type"
  [5]: ./images/custom_setup.png "custom_setup"
  [6]: ./images/browse.png "browse"
  [7]: ./images/mongodb_compass.png "mongodb_compass"
  [8]: ./images/installed.png "installed"
  [9]: ./images/install_status.png "install_status"