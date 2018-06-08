# AT Command Set
- 此文描述了M6312平台所支持的`AT`命令集。使用该命令集可以控制和管理与`GSM`网络相关的各种业务, 如**呼叫业务**、**短信息业务**、**各种附加业务**、**GPRS数据业务**等等; 也可以控制与`ME`相关的功能, 如读取`IMEI`, **操作电话**等等。

## MD6312风格



## MD6312术语

| 名称 | 描述 |
| --- | --- |
| AT | AT命令 |
| TE | 终端设备 |
| TA | 终端适配器 |
| MT | 移动终端 |
| MT Message | 移动终端消息 |
| MO Message | 移动台发起的消息 |
| SMS | 短消息服务 |
| USSD | 非结构化补充业务数据 |
| CC | 呼叫服务 |
| SS | 补充业务 |
| CRSS | 呼叫相关服务 |
| ID | 认证 |
| NW | 网络 |

- 此外:
    - 状态表中的`"T"`指`AT`命令类型是"测试"。
    - 状态表中的`"R"`指`AT`命令类型是"读取"。
    - 状态表中的`"S"`指`AT`命令类型是"设置"。
    - 状态表中的`"E"`指`AT`命令类型是"可执行"。
    - 状态表中的`"Y"`表示`AT`指令已经执行完毕。
    - 状态表中的`"N"`表示`AT`指令尚未执行。
    - 状态表中的`"P"`表示`AT`指令一部分完成, 有一部分尚未执行。

## 指令语法格式

| 指令格式 | 描述 |
| --- | --- |
| <center>测试指令</center><br/>[如果这个指令支持`"test"`, 就应该在这里输入实例。] | Description<br/>...<br/><br/>Response<br/>...<br/><br/>Parameter<br/>... |
| <center>读取指令</center><br/>[如果这个指令支持`"read"`, 就应该在这里输入实例。] | Description<br/>...<br/><br/>Response<br/>...<br/><br/>Parameter<br/>... |
| <center>设置指令</center><br/>[如果这个指令支持`"set"`, 就应该在这里输入实例。] | Description<br/>...<br/><br/>Response<br/>...<br/><br/>Parameter<br/>... |
| <center>可执行指令</center><br/>[如果这个指令支持`"exe"`, 就应该在这里输入实例。] | Description<br/>...<br/><br/>Response<br/>...<br/><br/>Parameter<br/>... |


## AT语法格式
- 所有的指令必须以`AT`或者`at`开头。输入`<CR>`可终止指令, 输入指令后通常会有类似`"<CR><LF><response><CR><LF>"`格式的响应。`<CR><LF>`换行符此处不做介绍, 换行作用。

## 命令和响应类型如下

| AT指令 | 描述 | 功能 |
| --- | --- | --- |
| 测试指令 | 注意命令 | 终端返回由指令或者是内部进程设置的参数的值和范围。 |
| 读指令 | 终端设备 | 此命令返回一个或者多个参数的设置值。 |
| 设置指令 | 终端适配器 | 该命令设置用户定义的参数值。 |
| 可执行指令 | 网络 | 读取内部进程中的非变量参数。|


## 语法规则
- 除了`"A /"`和`"+++"`开头的特殊指令, 其他所有命令行必须以`"AT"`或者`"at"`开头, 否则将被视为无效的命令, 以`"aT"`或者`"At"`开头的指令也被视为无效指令。
- 若一条指令包含多条`AT`指令, 只需要在开头添加`"AT"`或者`"at"`。
- 基本命令后可以接基本命令或者扩展命令, 但是需要在同一指令行。扩展命令也是这样, 不同的是, 需要在扩展命令和其他指令之间用`","`隔开。
- 最大指令长度为`200`字节。
- 最大参数长度为`80`字节。
- 单个指令行最大长度不超过`256`字节, 包括`S3`和`S5`定义的字符。


## AT+CPIN

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 用来输入或者修改PIN码 |
| 设置命令 | AT+CPIN=<pin>[,<newpin>] |
| 返回 | OK<br/> ERROR <br/> +CME ERROR:`<err>` |
| 读取命令 | AT+CPIN? |
| 返回 | +CPIN:`<code>`<br /> OK <br /> ERROR <br /> +CME ERROR: <err> |
| 测试命令 | AT+CPIN=? |
| 返回 | OK |
| 参数说明 | pin: 4-8个数字<br/> new pin: 4-8个数字 <hr /> puk: 8个数字 <hr /> code: <br /> READY: 不需要输入<br /> SIM PIN: 输入PIN码ME is waiting for SIM PIN <br /> SIM PUK: 输入PUK码ME is waiting for SIM PUK <br /> SIM PIN2: 输入PIN2码ME is waiting for SIM PIN2 <br /> SIM PUK2: 输入PUK2码ME is waiting for SIM PUK2 <br /> BLOCK: 被锁定 |

## AT+CPIN(Example)
```
AT+CPIN="1234"
OK
AT+CPIN="5678"
+CME ERROR: 3
AT+CPIN="00000000","2134"
+CME ERROR: 16
AT+CPIN="12345678","1234"
OK
AT+CPIN?
+CPIN:READY
```

## AT+CREG

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 设置自动报告网络状态 |
| 设置命令 | AT+CREG=`<mode>` |
| 返回 | OK/ERROR |
| 读取命令 | AT+CREG? |
| 返回 | +CREG: `<mode>`,`<stat>`[,`<lac>`,`ci`] |
| 测试命令 | AT+CREG=? |
| 返回 | +CREG:(0-2) <br /> OK |
| 参数说明 | mode: 缺省值为0 <br /> 0: 取消网络注册报告 <br /> 1: 激活网络注册报告 <br /> 2: 激活网络注册和本地信息报告 |

- 返回信息说明如下:

| 参数名称 | 含义 |
| --- | --- |
| state | 0: 没有注册网络, ME没有搜索新的网络 <br /> 1: 成功注册本地网络 <br /> 2: 没有注册网络, ME正在搜索新的网络 <br /> 3: 网络注册被拒绝 <br /> 4: 未知 <br /> 5: 成功注册漫游网络 <br /> 8: 紧急呼叫状态 |
| lac | 小区位置代码 |
| ci | 小区ID号 |
| AcT | access technology of the registered network <br /> 0: GSM <br /> 1: GSM Compact <br /> 2: UTRAN <br /> 3: GSM w/EGPRS (3GPP TS 44.060 [71] specifies the System Information messages) |

## AT+CREG(Example)
```
AT+CREG=1
OK
AT+CREG?
+CREG: 1,1
OK
AT+CREG=2
+CREG: 2,1,"3394","9DE7",2
OK
AT+CREG=0
OK
```

## AT+CSQ

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 用来读取当前服务小区的信号强度 |
| 执行命令 | AT+CSQ |
| 返回 | +CSQ:`<rssi>`,`<ber>`<br /> +CME ERROR:`<err>` |
| 测试命令 | AT+CSQ=? |
| 返回 | +CSQ:(list of supported `<rssi>`s),(list of supported `<ber>`s) |
| 参数说明 | rssi: <br /> 0: -110db <br /> 1-30: ...... <br /> 31: -48db <br /> ber: <br /> 0~7: RXQUAL值(GSM) <br /> 99: 无效值 |

## AT+CSQ(Example)
```
AT+CSQ
+CSQ:23,99
OK
```

## AT+CGDCONT

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 发送PDP上下文激活消息的时候使用这个命令配置PDP上下文参数。系统重新启动后, 该命令所做的设置将不被保存 |
| 设置命令 | AT+CGDCONT=`<cid>` [,`<PDP_type>` [,`<APN>` [,`<PDP_addr>`[,`<d_comp>` [,`<h_comp>`]]]]] |
| 返回 | Success: <br /> OK <br /> Fail: <br /> ERROR <br /> |
| 读取命令 | AT+CGDCONT? |
| 返回 | Success: <br /> +CGDCONT:`<cid>`,`<PDP_type>`,`<APN>`,`<PDP_addr>`,`<d_comp>`,`<h_comp>` |
| 测试命令 | AT+CGDCONT=? |
| 返回 | Success: <br /> +CGDCONT: (range of supported `<cid`s), `<PDP_type>`, (list of supported `<d_comp>`s), (list of supported `<h_comp>`s) <br /> OK <br /> Fail: <br /> ERROR <br /> |
| 参数说明 | cid: (PDP Context Identitfier)整形(范围1-11), 指定PDP上下文的ID号 <hr /> PDP_type: (Packet Data Protocol type), 目前只支持IP(Internet Protocol) <hr /> APN: (Access Point Name)字符串, 用来选择2或者其他的分组数据网络, 请咨询当地的网络运营商, 中国移动为Internet服务的APN为`"cmnet"`, Wap服务的APN为`"cmwap"` <hr /> PDP_address: 字符串, 给定PDP的地址。此值可不填, 由网络动态分配一个地址 <hr /> d_comp: PDP数据是否需要压缩。目前MT、网络都不支持数据压缩。<br /> 0 -不采用压缩 <br /> 1 -采用压缩 <br /> 2 - V.42bis <br /> 3 - V.44bis <br /> 此值不可填, 缺省值为0。 <hr /> h_comp: PDP头部数据是否需要压缩。目前MT、网络都不支持数据压缩。<br /> 0 - 不采用压缩 <br /> 1 - 采用压缩 <br /> 2 - RFC1144 <br /> 3 - RFC2507 <br /> 4 - RFC3095 <br /> 此值不可填, 缺省值为0。 |

## AT+CGDCONT(Example)
```
AT+CGDCONT=?
+CGDCONT:(1..7),(IP,IPV6,PPP),(0..3),(0..4)
OK
AT+CGDCONT=1,"IP","cmnet"
OK
AT+CGDCONT?
+CGDCONT:1,"IP","cmnet",,0,0
OK
```

## AT+CGACT
| 说明 | 状态参数 |
| --- | --- |
| 作用 | 激活(active)或去活(deactive)指定的PDP上下文。如果MT已经在所要求的状态，设置命令被忽视并返回OK; 如果所要求的状态无货获得, 返回ERROR。如果在激活指定PDP上下文命令执行时, MT尚未进行GRRS ATTACH操作失败, 返回ERROR。|
| 设置命令 | AT+CGACT=`<state>`[,`<cid>`[,`<cid>`[,...]]] |
| 返回 | Success: <br /> OK <br /> Fail: <br /> ERROR |
| 读取命令 | AT+CGACT? |
| 返回 | Success: <br /> +CGACT: (`<cid>`, `<state>`) <br /> +CGACT: (`<cid>`, `<state>`)[...] <br /> OK <br /> Fail: <br /> ERROR |
| 测试命令 | AT+CGACT=? |
| 返回 | Success: <br /> +CGACT: (list of supported `<state>`s) <br /> OK <br /> Fail: <br /> ERROR |
| 参数说明 | state: <br /> 0: PDP 上下文去活 <br /> 1: PDP 上下文激活 <hr /> cid: PDP Context Identifier, 指定一个PDP上下文的ID号。整形: 1~11。<br /> 在未指定`<cid>`号时, 激活PDP上下文默认为`cid=1`, 即AT+CGACT=1与AT+CGACT=1,1; 在去活PDP上下文时如未指定`<cid>`, 则默认去活所有活动的PDP上下文。|

## AT+CGACT(Example)
```
AT+CGACT=?
+CGACT:(0,1)
OK

AT+CGACT=1,1
OK

AT+CGACT?
+CGACT:1,1
OK
```

## AT+CMHTTPSET
| 说明 | 状态参数 |
| --- | --- |
| 作用 | 该命令用于配置HTTP参数 |
| 设置命令 | AT+CMHTTPSET=`<server>`,`<port>`,`<request url>` [, `<download_urc>`] |
| 返回 | 如果成功, 返回: <br /> CONNECT OK <br /> <br /> OK |
| 参数说明 | server 服务器名或者IP地址 <br /> port 服务器端口 <br /> request url GET或者POST请求URL. <br /> download_urc 可选项, 开启后在使用CMHTTPDL命令的时候会提示下载总长度 |

## AT+CMHTTPSET(Example)
```
AT+CMHTTPSET="iot.10086.cn", 80, "/contact-us/"

CONNECT OK

OK
```

> 注意: 
> 1. 如果返回结果不为CONNECT OK, 那么不能使用后续HTTP命令。此外HTTP命令不能和ipstart命令混合使用。
> 2. 只有在单路连接模式下才可以使用HTTP命令, 透传和缓存模式下不可以使用。

## AT+CMHTTPGET

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 该命令用于发送HTTP GET 请求 |
| 执行命令 | AT+CMHTTPGET |
| 返回 | 如果连接成功, 返回: <br /> CONNECT OK <br /> <br /> OK <br /> 服务器响应; <br /> OK |

## AT+CMHTTPPOST

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 该命令用于发送HTTP POST 请求 |
| 设置命令 | AT+CMHTTPPOST=`<post content>` |
| 返回 | 如果连接成功, 返回: <br /> CONNECT OK <br /> <br /> OK <br /> 服务器响应; <br /> OK <br /> |
| 参数说明 | post content: <br /> POST 请求内容 |  

## AT+IPSTART
| 说明 | 状态参数 |
| --- | --- |
| 作用 | 建立TCP或者UDP连接 |
| 设置命令 | AT+IPSTART=[`<index>`,]`<mode>`,`<IPaddress>/`,`<port>` |
| 返回 | 如果连接已经存在, 返回 <br /> +CME ERROR: <br /> 连接成功, 返回: <br /> CONNECT OK <br /> `<TCP连接时会返回连接链路信息>` <br /> OK <br /> 连接失败, 返回: <br /> +CME ERROR |
| 测试命令 | AT+IPSTART=? |
| 返回 | +IPSTART:[(0~4),]("TCP","UDP"),((0-255).(0-255).(0-255).(0-255)),(0-65536) |
| 最大响应时间 | 受网络状态影响 |
| 参数说明 | `<index>` <br /> 0~4 表明连接序号(M6312支持5个SOCKET同时存在)。<br /> 当前仅`AT+CMMUX=1`时, 该参数有效。<br /> 当`AT+CMMUX=0`时, 该参数必须缺省(请参考AT+CMMUX) <br /> `<mode>` <br /> 字符串类型; 表明连接类型 <br /> "TCP"建立TCP连接 <br /> "UDP"建立UDP连接 <br /> `<IP address>` <br /> 字符串类型; 表明远端服务器IP地址 <br /> `<port>` <br /> 远端服务器端口号 |

## AT+IPSTART(Example)
```
AT+IPSTART=3,"TCP","183.230.40.150",36000
CONNECT OK
OK
```

> 注意:
> 如果TCP连接建立成功, 会返回CONNECT OK, 如果连接失败, 会返回CONNECT FAIL。UDP连接建立后, 会返回BIND OK。多路连接模式下最多支持5路连接 

## AT+IPSEND
| 说明 | 状态参数 |
| --- | --- |
| 作用 | 发送TCP或者UDP数据 |
| 设置命令 | 1. 单路连接时 (+CMMUX=0) <br /> AT+IPSEND <br /> 响应`">"`, 输入数据, 执行`CTRL+Z`来发送, 执行ESC来终止操作 <br /> 注: 该操作当且仅当AT+CMMUX=0时可执行 <br /> 2. 多路连接时(+CMMUX=1) <br /> AT+IPSEND=`<index>` <br /> 响应`">"`, 输入数据, 执行`CTRL+Z`来发送, 执行`ESC`来终止操作; |
| 返回 | 如果连接存在, 发送成功返回: <br /> SEND OK <br /> OK <br /> 发送失败, 返回: <br /> SEND FAIL <br /> 如果`TCP`或者`UDP`连接主动断开, 返回: <br /> CONNECTION CLOSED |
| 最大响应时间 | 受网络状态影响 |
| 参数说明 | `<index>`数字参数; 表明连接序号; 该参数仅适用于`AT+CMMUX=1`,若`AT_CMMUX=0`, 该参数必须缺省 |

## AT+IPSEND(Example)
```
AT+CMMUX=1
OK
AT+IPSTART=0,"TCP","183.230.40.150",36000
AT+IPSEND=0
>HELLO<CRTL-Z>
Send OK
```

> 注意: 1. 只有在TCP或者UDP连接建立后才可以发送数据;
>       2. TCP连接在发送成功后会返回SEND OK, 如果传输16进制数据包含CTRL+Z和ESC特殊字符, 请使用透传或者配置CMIPMODE。

## AT+IPCLOSE
| 说明 | 状态参数 |
| --- | --- |
| 作用 | 关闭TCP或者UDP连接 |
| 设置命令 | AT+IPCLOSE=[`<index>`] |
| 返回 | 如果关闭连接成功返回; <br /> OK |
| 测试命令 | AT+IPCLOSE=? |
| 返回 | +IPCLOSE: <br /> OK |
| 最大响应时间 | 300ms |
| 参数说明 | `<index>` <br /> 数字参数; 表明连接序号 <br /> 单路连接下该参数必须缺省。 |

> 注意:
> 使用IPSTART命令建立连接, 无论建立是否成功或者超时, 使用完毕后必须使用IPCLOSE释放资源。 
> 如果服务器主动断开连接, 会返回CONNECTION CLOSED: `<index>`, 也需要主动调用IPCLOSE释放资源。

## AT+CDNSGIP

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 域名解析 |
| 设置命令 | AT+CNDSGIP=`<domain name>` |
| 返回 | 返回OK后, 若解析成功: <br /> +CDNSGIP: `<IP address>` <br /> OK |
| 测试命令 | AT+CNDSGIP=? |
| 返回 | OK |
| 最大响应时间 | 14s, 受网络状态影响 |
| 参数说明 | `<domain name>` <br /> 字符串参数; 表明Internet上注册的域名 <br /> `<IP address>` <br /> 字符串参数; 表明IP地址对应的域名 |

> 注意:
> 使用前请先激活PDP, 参考AT+CGACT命令。

## AT+CMPROMPT

| 说明 | 状态参数 |
| --- | --- |
| 作用 | 设置发送数据时是否显示">"和"SEND OK" |
| 设置命令 | AT+CMPROMPT=`<send prompt>` |
| 返回 | 成功: OK <br /> 失败: ERROR |
| 读取命令 | AT+CMPROMPT? |
| 返回 | +CMPROMPT: `<send prompt>` <br /> OK |
| 测试命令 | AT+CMPROMPT=? |
| 返回 | +CMPROMPT:(0,3) <br /> OK |
| 最大响应时间 | 300ms |
| 参数说明 | `<send prompt>`数字参数; 表明AT+IPSEND操作后, 是否显示">"和"SEND OK" <br /> 0 发送成功时不显示">", 返回"SEND OK" <br /> 1 发送成功时显示">", 返回"SEND OK" <br /> 2 发送成功时不显示">", 不返回"SEND OK" <br /> 3 发送成功时显示">", 返回"<index>, SEND OK" |

## AT+CMMODE 
| 说明 | 状态参数 |
| --- | --- |
| 作用 | 打开/关闭TCPIP透传模式 |
| 测试命令 | AT+CMMODE=? |
| 返回 | +CMMODE:(0,1) <br /> OK |






