# Openstack
- `Openstack`项目是一个支持所有云环境的开源云计算平台。该项目旨在提升易用性, 支持大规模扩展和提供更多优秀的特性。全球的云计算专家都在为`Openstack`项目做出贡献。`Openstack`通过一系列服务, 形成了一个`IaaS`解决方案, 每一个服务都提供了相应的`API`来更好地使用。

## Open Source —— Apache 2.0许可, 企业友好.
## Open Design —— 六个月一次, 基本与unbutu同步.
## Open Development —— 社会化研发, Launchpad & github.
## Open Community —— lazy consensus model(懒人原则), OpenStack 基金会.

## `Openstack`架构
- `Openstack`由一系列的子项目组成, 形成一个完整的`IaaS`解决方案. 如下图所示:

### Dashboard
- 该服务的工程名为`Horizon`, 目的是提供基于`Web`的自服务门户, 来实现用于与底层服务的交互, 比如启动实例, 分配IP地址, 配置访问控制策略等等。

------

### Compute
- 该服务的工程名为`Nova`。目的是管理运行在`Openstack`环境中的计算实例, 比如按需创建, 调度和销毁虚拟机。

------

### Networking
- 该服务的工程名为`Neutron`。目的是为`Openstack`的服务, 比如计算服务, 提供网络连接服务。提供了`API`供用户定义网络及其相关内容。基于"插件式"的架构, 支持众多主流的网络提供商和技术。

-----

### Object Storage
- 该服务的工程名为`Swift`。目的是通过`REST API`的形式存储和检索**非结构化数据**。由于采用了数据复制和高扩展性架构, 所以具有很高的容错性。该项目的实现并不像具有可挂载目录的文件服务器, `Object Storage`通过写对象和文件到多个驱动器的实现方式, 确保了数据能够在群集之间复制。

------

### Block Storage
- 该服务的工程名为`Cinder`。提供一个**持久化的块存储**来运行实例。该服务的"可插拔驱动器"模式, 提升了创建和管理块存储的能力。

------

### Identity Service
- 该服务的工程名为`Keystone`。为`OpenStack`服务提供认证和授权, 为`Openstack`服务提供了服务端点目录。

------

### Image Service
- 该服务的工程名为`Glance`。存储和检索虚拟机磁盘镜像, `Openstack`计算服务在实例配置的过程中会使用到这个服务。

------

### Telemetry
- 该服务的工程名为`Ceilometer`。监控和计量`Openstack`云服务, 为`Openstack`提供计费, 阀值管理, 扩展和分析等服务。

------

### Orchestration
- 该服务的工程名为`Heat`。通过本地的`HOT`模板格式或者`AWS CloudFormation`模板格式, 甚至`Openstack`本地`REST API`和兼容`CloudFormation`的`Query API`, 来编排多个混合的基于云的应用。

------

### Database Service
- 该服务的工程名为`Trove`。为数据库引擎提供了可靠的, 高扩展性的"云数据库即服务"。

-----

### Data Processing Service
- 该服务的工程名为`Sahara`。提供了在Openstack中配置和扩展`Hadoop`群集的能力, 而实现这个一点只需要传`Hadoop`版本, 群集拓扑结构和节点的硬件信息即可。

------

## 部署过程
- 在部署过程中, 最精简的架构需要四个节点组成:
    - **控制节点(Controller)**;
    - **计算节点(Compute)**;
    - **网络节点(Networking)**;
    - **存储节点(Storage)**;

### 控制节点(Controller)
- 安装`Identity Service`, `Image Service`, 计算和网络服务的管理部分, 网络部分的插件及`Dashboard`。

### 计算节点(Compute)
- 安装`KVM`作为`Hpervisor`, 部分网络服务。

### 网络节点(Networking)
- 安装`Networking`服务及相关的`Agent`来配置网络, 分配交换机, 路由器, 提供`NAT`, `DHCP`服务。

### 存储节点(Storage)
- 安装`Storage`服务。



