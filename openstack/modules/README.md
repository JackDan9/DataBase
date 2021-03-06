# Openstack的各个组件作用以及关系

## Keystone - 认证服务(Openstack认证服务)
- `Keystone`为所有的OpenStack组件提供**认证和访问策略服务,** 它依赖于**自身`REST`**(基于`Identity API`)系统进行工作, 主要对(但不限于)`Swift`, `Glance`, `Nova`等进行认证与授权。事实上, 授权通过对动作消息来源者请求的合法性进行鉴定。
- 下图显示了身份认证服务流程:

![keystone][1]

- `Keystone`采用两种授权方式, 一种基于**用户名/密码**, 另一种**基于令牌(Token)**。
- 除此之外, `Keystone`提供一下三种服务:
    - 令牌服务: 含有授权用户的授权信息;
    - 目录服务: 含有用户合法操作的可用服务列表;
    - 策略服务: 利用`Keystone`具体指定用户或者群组某些访问权限。

## `Keystone`认证服务注意点
- 服务入口: 如`Nova`、`Swift`和`Glance`一样每个OpenStack服务都拥有一个指定的端口和专属的URL, 称其为**入口(`endpoints`)**。
- 区位: 在某个数据中心, 一个区位**具体指定了一处物理位置**。在典型的云架构中, 如果不是所有的服务都访问分布式数据中心或者服务器的话, 则也称其为区位。
- 用户: Keystone授权使用者(代表一个个体, OpenStack以用户的形式来授权服务给它们。用户拥有证书(credentials), 且可能分配给一个或者多个租户。经过验证后, 会为每个单独的租户提供一个特定的令牌)。
- 服务: 总体而言, **任何通过Keystone进行连接或者管理的组件都被称为服务。**举个例子, 可以称`Glance`为`Keystone`的服务。
- 角色: 为了维护安全限定, 就云内特定用户可执行的操作而言, 该用户关联的角色是非常重要的。(一个角色是应用于某个租户的使用权限集合, 以允许某个指定用户访问或者使用特定操作。角色是使用权限的逻辑分组, 它使得通用的权限可以简单地分组绑定到与某个指定租户相关的用户)。
- 租间: 租间指的是具有全部服务入口并配有特定成员角色的一个项目。(一个租间映射到一个Nova的"project-id", 在对象存储中, 一个租间可以有多个容器。根据不同的安装方式, 一个租间可以代表一个客户、账号、组织或者项目)。

------

## Nova - 计算服务(OpenStack计算设施----Nova)
- `Nova`是OpenStack计算的弹性控制器。OpenStack云实例生命周期所需的各种动作都将由Nova进行处理和支撑, 这就意味着Nova以管理平台的身份登场, 负责管理整个云的计算资源、网络、授权以及测度。虽然Nova本身并不提供任何虚拟能力, 但是它将使用`libvirt API`与虚拟机的宿主机进行交互。Nova通过Web服务API来对外提供处理接口, 而且这些接口与Amazon的Web服务接口是兼容的。

### 功能以及特点:
- 实例生命周期管理;
- 计算资源管理;
- 网络与授权管理;
- 基于REST的API;
- 异步连续通信;
- 支持各种宿主: Xen、XenServer/XCP、KVM、UML、VMware vSphere以及Hyper -V

### Nova弹性云(OpenStack计算部件)包含以下主要部分:
- `API Server`(nova-api);
    - API服务器提供了云设施与外界交互的接口, 它是外界用户对云设施管理的唯一通道。通过使用web服务来调用各种EC2(Elastic Compute Cloud)的API, 接着API服务器便通过消息队列把请求送达至云内目标设施进行处理。作为对EC2-api的替代, 用户也可以使用OpenStack的原生API, 把它叫做"OpenStack API"。

- 消息队列(rabbit-mq server);
    - OpenStack内部在遵循AMQP(高级消息队列协议)的基础上采用消息队列进行通信。Nova对请求应答进行异步调用, 当请求接受后便立即触发一个回调。由于使用了异步通信, 不会有用户的动作被长置于等待状态。例如, 启动一个实例或者上传一份镜像的过程较为耗时, API调用就将等待返回结果而不影响其它操作, 在此异步通信起到了很大的作用, 使整个系统变得更加高效。

- 运算工作站(nova-compute);
    - 运算工作站的主要任务是**管理实例的整个生命周期**。他们通过消息队列请求并执行, 从而对实例进行各种操作。在典型实际生产环境下, 会架设许多运算工作站, 根据调度算法, 一个实例可以在可用的任意一台计算工作站上部署。

- 网络控制器(nova-network);
    - 网络控制器处理主机的网络配置, 例如IP地址分配, 配置项目VLAN, 设定安全群组以及为计算节点配置网络。

- 卷管理(nova-volume);
    - 卷工作站管理基于LVM的实例卷, 它能够为一个实例创建、删除、附加卷, 也可以从一个实例中分离卷。
    - 卷管理为何如此重要？
        - 因为它提供了一种保持实例持续存储的手段, 比如当结束一个实例后, 根分区如果是非持续化的, 那么对其的任何改变都将丢失。可是, 如果从一个实例中将卷分离出来, 或者为这个实例附加上卷的话, 即使实例被关闭, 数据仍然保存其中。这些数据可以通过将卷附加到原实例或者其他实例的方式而重新访问。
        - 因此, 为了日后访问, 重要数据务必要写入卷中。这种应用对于数据服务器实例的存储而言, 尤为重要。

- 调度器(nova-scheduler);
    - 调度器负责把nova-API调用送达给目标。调度器以名为"nova-schedule"的守护进程方式运行, 并根据调度算法从可用资源池中恰当地选择运算服务器。有很多因素都可以影响调度结果, 比如负载、内存、子节点的远近、CPU架构等等。强大的是nova调度器采用的是可插入式架构。
    - 目前nova调度器使用了几种基本的调度算法:
        - 随机化: 主机随机选择可用节点;
        - 可用化: 与随机相似, 只是随机选择的范围被指定;
        - 简单化: 应用这种方式, 主机选择负载最小者来运行实例。负载数据可以从别处获得, 如负载均衡服务器。

------

## Glance - 镜像服务(OpenStack镜像服务器---Glance)
- OpenStack镜像服务器是一套虚拟机镜像发现、注册、检索系统, 可以将镜像存储到以下任意一种存储中:
    - 本地文件系统(默认);
    - S3直接存储;
    - S3对象存储(作为S3访问的中间渠道);
    - OpenStack对象存储等等。
- 功能以及特点:
    - 提供镜像相关服务。
- `Glance`构件:
    - `Glance-API`:
        - 主要负责接收响应镜像管理命令的`Restful`请求, 分析消息请求信息并分发其所带的命令(如新增、删除、更新等)。默认绑定端口是`9292`。
    - `Glance_Registry`:
        - 主要负责接收响应镜像元数据命令的`Restful`请求。分析消息请求信息并分发其所带的命令(如获取元数据, 更新元数据等)。默认绑定的端口是`9191`。

------

## Swift - 对象存储服务(OpenStack存储设施---Swift)
- `Swift`为OpenStack提供一种分布式、持续虚拟对象存储, 它类似于`Amazon Web Service`的`S3`简单存储服务。`Swift`具有跨节点百级对象的存储能力。`Swift`内建冗余和失效备援管理, 也能够处理归档和媒体流, 特别是对大数据(千兆字节)和大容量(多对象数量)的测度非常高效。
- `Swift`功能及特点:
    - 海量对象存储;
    - 大文件(对象)存储;
    - 数据冗余管理;
    - 归档能力-----处理大数据集
    - 为虚拟机和云应用提供数据容器;
    - 处理流媒体;
    - 对象安全存储;
    - 备份与归档;
    - 良好的可伸缩性;

- `Swift`组件:
    - `Swift`代理服务器;
        - 用户都是通过`Swift-API`与代理服务器进行交互, 代理服务器正是接收外界请求的门卫, 它检测合法的实体位置并路由它们的请求。
    - `Swift`对象服务器;
        - 对象服务器是一种二进制存储, 它负责处理本地存储中的对象数据的存储、检索和删除。对象都是文件系统中存放的典型的二进制文件, 具有扩展文件属性的元数据(xattr)。
        - 注意: `xattr`格式被Linux中的ext3/4, XFS, Btrfs, JFS和ReiserFS所支持, 但是并没有有效测试证明在`XFS`, `JFS`, `ReiserFS`, `Reiser4`和`ZFS`下也同样能运行良好。不过, `XFS`被认为是当前最好的选择。
    - `Swift`容器服务器
        - 容器服务器将列出一个容器中的所有对象, 默认对象列表将存储为SQLite文件(译者注: 也可以修改为MySQL, 安装中就是以MySQL为例)。容器服务器也会统计容器中包含的对象数量以及容器的存储空间耗费。
    - `Swift`账号服务器
        - 账号服务器与容器服务器类似, 将列出容器中的对象。
    - `Ring`(索引环)
        - `Ring`容器记录着Swift中物理存储对象的位置对象, 它是真实物理存储位置的实体名的虚拟映射, 类似于查找以及定位不同集群的实体真实物理位置的索引服务。这里所谓的实体指账号、容器、对象, 它们都拥有属于自己的不同的`Rings`。

------

## Horizon - UI服务(OpenStack管理的Web接口----Horizon)
- `Horizon`是一个用以管理、控制OpenStack服务的Web控制面板, 它可以管理实例、镜像、创建密钥对, 对实例添加卷、操作Swift容器等。除此之外, 用户还可以在控制面板中使用终端(console)或者VNC直接访问实例。
- 总之, Horizon具有如下一些特点:
    - 实例管理: 创建、终止实例, 查看终端日志, VNC连接, 添加卷等;
    - 访问与安全管理: 创建安全群组, 管理密钥对, 设置浮动IP等;
    - 偏好设定: 对虚拟硬件模板可以进行不同偏好设定;
    - 镜像管理: 编辑或者删除镜像;
    - 用户管理: 查看服务目录、创建用户、管理用户、配额以及项目用途等;
    - 卷管理: 创建卷和快照;
    - 对象存储处理: 创建、删除容器和对象, 为项目下载环境变量。


------

## 组件间的关系图:

![modules_relation][2]



> https://www.cnblogs.com/klb561/p/8660264.html


  [1]: ./images/keystone.png "keystone.png"
  [2]: ./images/modules_relation.png "modules_relation.png"