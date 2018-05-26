## dashboard

#### 启动实例
- 启动一台实例, 您必须至少指定一个类型、镜像名称、网络、安全组、密钥和实例名称。

- 1. 在控制节点上, 获得`admin`凭证来获取只有管理员能执行的命令的访问权限。
```
$ source demo-openrc.sh
```

- 2. 一个实例指定了虚拟机资源的大致分配, 包括处理器、内存和存储。
- 列出可用类型:

```
$ nova flavor-list
+-----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
| ID  | Name      | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+-----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
| 1   | m1.tiny   | 512       | 1    | 0         |      | 1     | 1.0         | True      |
| 2   | m1.small  | 2048      | 20   | 0         |      | 1     | 1.0         | True      |
| 3   | m1.medium | 4096      | 40   | 0         |      | 2     | 1.0         | True      |
| 4   | m1.large  | 8192      | 80   | 0         |      | 4     | 1.0         | True      |
| 5   | m1.xlarge | 16384     | 160  | 0         |      | 8     | 1.0         | True      |
+-----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
```

- 这个实例使用``m1.tiny``方案。
> 注解: 您也可以以`ID`引用类型。

- 3. 列出可用镜像:

```
$ nova image-list
+--------------------------------------+--------+--------+--------+
| ID                                   | Name   | Status | Server |
+--------------------------------------+--------+--------+--------+
| 38047887-61a7-41ea-9b49-27987d5e8bb9 | cirros | ACTIVE |        |
+--------------------------------------+--------+--------+--------+
```

- 这个实例使用``cirros``镜像。        

- 4. 列出可用网络:

```
$ neutron net-list
+--------------------------------------+---------+----------------------------------------------------+
| id                                   | name    | subnets                                            |
+--------------------------------------+---------+----------------------------------------------------+
| 0e62efcd-8cee-46c7-b163-d8df05c3c5ad | public  | 5cc70da8-4ee7-4565-be53-b9c011fca011 10.3.31.0/24  |
| 7c6f9b37-76b4-463e-98d8-27e5686ed083 | private | 3482f524-8bff-4871-80d4-5774c2730728 172.16.1.0/24 |
+--------------------------------------+---------+----------------------------------------------------+
```

- 这个实例使用``private``项目网络。您必须使用ID而不是名称才可以引用这个网络。

- 5. 列出可用的安全组:

```
$ nova secgroup-list
+--------------------------------------+---------+-------------+
| Id                                   | Name    | Description |
+--------------------------------------+---------+-------------+
| ad8d4ea5-3cad-4f7d-b164-ada67ec59473 | default | default     |
+--------------------------------------+---------+-------------+
```

- 这个实例使用`default`安全组。

- 6. 启动实例:
- 使用``private``项目网络的`ID`替换`PRIVATE_NET_ID`。

```
$ nova boot --flavor m1.tiny --image cirros --nic net-id=PRIVATE_NET_ID \
  --security-group default --key-name mykey private-instance
+--------------------------------------+-----------------------------------------------+
| Property                             | Value                                         |
+--------------------------------------+-----------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                        |
| OS-EXT-AZ:availability_zone          | nova                                          |
| OS-EXT-STS:power_state               | 0                                             |
| OS-EXT-STS:task_state                | scheduling                                    |
| OS-EXT-STS:vm_state                  | building                                      |
| OS-SRV-USG:launched_at               | -                                             |
| OS-SRV-USG:terminated_at             | -                                             |
| accessIPv4                           |                                               |
| accessIPv6                           |                                               |
| adminPass                            | oMeLMk9zVGpk                                  |
| config_drive                         |                                               |
| created                              | 2015-09-17T22:36:05Z                          |
| flavor                               | m1.tiny (1)                                   |
| hostId                               |                                               |
| id                                   | 113c5892-e58e-4093-88c7-e33f502eaaa4          |
| image                                | cirros (38047887-61a7-41ea-9b49-27987d5e8bb9) |
| key_name                             | mykey                                         |
| metadata                             | {}                                            |
| name                                 | private-instance                              |
| os-extended-volumes:volumes_attached | []                                            |
| progress                             | 0                                             |
| security_groups                      | default                                       |
| status                               | BUILD                                         |
| tenant_id                            | f5b2ccaa75ac413591f12fcaa096aa5c              |
| updated                              | 2015-09-17T22:36:05Z                          |
| user_id                              | 684286a9079845359882afc3aa5011fb              |
+--------------------------------------+-----------------------------------------------+
```

- 7. 检查实例的状态:

```
$ nova list
+--------------------------------------+------------------+--------+------------+-------------+----------------------+
| ID                                   | Name             | Status | Task State | Power State | Networks             |
+--------------------------------------+------------------+--------+------------+-------------+----------------------+
| 113c5892-e58e-4093-88c7-e33f502eaaa4 | private-instance | ACTIVE | -          | Running     | private=172.16.1.3   |
| 181c52ba-aebc-4c32-a97d-2e8e82e4eaaf | public-instance  | ACTIVE | -          | Running     | public=203.0.113.103 |
+--------------------------------------+------------------+--------+------------+-------------+----------------------+
```
- 当构建过程全部成功后, 状态会从`BUILD`变为`ACTIVE`。 

#### 使用虚拟控制台访问实例
- 1. 获取您势力的`Virtual Network Computing(VNC)`会话`URL`并从`web`浏览器访问它:

```
$ nova get-vnc-console private-instance novnc
+-------+------------------------------------------------------------------------------------+
| Type  | Url                                                                                |
+-------+------------------------------------------------------------------------------------+
| novnc | http://controller:6080/vnc_auto.html?token=2f6dd985-f906-4bfc-b566-e87ce656375b    |
+-------+------------------------------------------------------------------------------------+
```

> 注解: 如果您运行浏览器的主机无法解析``controller``主机名, 可以将``__controller``替换为您控制节点管理网络的`IP`地址。

- `CirrOS`镜像包含传统的用户名/密码认证方式并需在登录提示中提供这些认证。登录到`CirrOS`后, 我们建议您验证使用``ping``验证网络的连通性。

- 2. 验证到``private``网络相关的访问
```
$ ping -c 4 172.16.1.1
PING 172.16.1.1 (172.16.1.1) 56(84) bytes of data.
64 bytes from 172.16.1.1: icmp_req=1 ttl=64 time=0.357 ms
64 bytes from 172.16.1.1: icmp_req=2 ttl=64 time=0.473 ms
64 bytes from 172.16.1.1: icmp_req=3 ttl=64 time=0.504 ms
64 bytes from 172.16.1.1: icmp_req=4 ttl=64 time=0.470 ms

--- 172.16.1.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 2998ms
rtt min/avg/max/mdev = 0.357/0.451/0.504/0.055 ms
```

- 3. 校验互联网访问:
```
$ ping -c 4 openstack.org
PING openstack.org (174.143.194.225) 56(84) bytes of data.
64 bytes from 174.143.194.225: icmp_req=1 ttl=53 time=17.4 ms
64 bytes from 174.143.194.225: icmp_req=2 ttl=53 time=17.5 ms
64 bytes from 174.143.194.225: icmp_req=3 ttl=53 time=17.7 ms
64 bytes from 174.143.194.225: icmp_req=4 ttl=53 time=17.5 ms

--- openstack.org ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3003ms
rtt min/avg/max/mdev = 17.431/17.575/17.734/0.143 ms
```

#### 远程访问实例
- 1. 在`public`网络创建一个`float IP address`
```
$ neutron floatingip-create public
Created a new floatingip:
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| fixed_ip_address    |                                      |
| floating_ip_address | 203.0.113.104                        |
| floating_network_id | 9bce64a3-a963-4c05-bfcd-161f708042d1 |
| id                  | 05e36754-e7f3-46bb-9eaa-3521623b3722 |
| port_id             |                                      |
| router_id           |                                      |
| status              | DOWN                                 |
| tenant_id           | 7cf50047f8df4824bc76c2fdf66d11ec     |
+---------------------+--------------------------------------+
```

- 2. 给实例分配浮动IP地址
```
$ nova floating-ip-associate private-instance 203.0.113.104
```

> 注解: 这个命令执行后没有输出

- 3. 检查这个浮动IP地址的状态:
```
$ nova list
+--------------------------------------+------------------+--------+------------+-------------+-----------------------------------+
| ID                                   | Name             | Status | Task State | Power State | Networks                          |
+--------------------------------------+------------------+--------+------------+-------------+-----------------------------------+
| 113c5892-e58e-4093-88c7-e33f502eaaa4 | private-instance | ACTIVE | -          | Running     | private=172.16.1.3, 203.0.113.104 |
| 181c52ba-aebc-4c32-a97d-2e8e82e4eaaf | public-instance  | ACTIVE | -          | Running     | public=203.0.113.103              |
+--------------------------------------+------------------+--------+------------+-------------+-----------------------------------+
```

- 4. 在控制节点或者任何公共网络上的主机通过浮动IP地址验证到实例的访问:
```
$ ping -c 4 203.0.113.103
PING 203.0.113.104 (203.0.113.104) 56(84) bytes of data.
64 bytes from 203.0.113.104: icmp_req=1 ttl=63 time=3.18 ms
64 bytes from 203.0.113.104: icmp_req=2 ttl=63 time=0.981 ms
64 bytes from 203.0.113.104: icmp_req=3 ttl=63 time=1.06 ms
64 bytes from 203.0.113.104: icmp_req=4 ttl=63 time=0.929 ms

--- 203.0.113.104 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3002ms
rtt min/avg/max/mdev = 0.929/1.539/3.183/0.951 ms
```

- 5. 通过控制节点或者任意公共网络上的主机使用SSH访问您的实例:
```
$ ssh cirros@203.0.113.104
The authenticity of host '203.0.113.104 (203.0.113.104)' can't be established.
RSA key fingerprint is ed:05:e9:e7:52:a0:ff:83:68:94:c7:d1:f2:f8:e2:e9.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '203.0.113.104' (RSA) to the list of known hosts.
$
```

> 注解: 如果您的主机没有包含前面步骤创建的`public/private`密钥对, SSH提示的默认密码是`cirros`用户是`cubswin`

#### IP地址管理
- 每个实例都有一个私有固定IP地址, 也可以有一个公共浮动IP地址。私有IP地址用于实例之间的通信, 公共地址用于与云外的网络通信, 包括互联网。
- 当您创建一个实例时, 其便获得了一个永久不变的私有IP地址直到您明确的终结了该实例。重启一个实例不会影响其私有IP地址。
- 浮动IP地址池在`Openstack`计算节点上由云管理员配置。项目