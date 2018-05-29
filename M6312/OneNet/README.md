# OneNet-AT CommandSet

## AT^ONENETPOST
- 说明: 指令功能是以HTTP协议方式使用平台的API接口发送数据到OneNet平台(大众版), 使用该命令需要先使用[`AT+CMHTTPSET`][1]设置HTTP连接参数。

| 说明 | 状态参数 |
| --- | --- |
| 功能 | 以http方式向云平台发送数据 |
| 设置指令格式: <br /> AT^ONENETPOST=`<post content>`,`<api-key>` | 正确响应: <br /> CONNECT OK <br /> `<mesg>` |
| 参数 | post content: POST请求内容, JSON格式数据流 <br /> api-key: Masterkey或者设备apikey <br /> mesg: 服务器反馈内容 |

> 注意: 
> 1. 当AT^ONENETPOST用于新增设备ID或者设备apikey时, 与该命令用于新增数据流或者数据点时, AT+CMHTTPSET的参数设置不同, 具体如示例所示。
> 2. 使用AT^ONENETPOST时api-key需要按照示例的格式进行配置。当该命令用于新增设备ID或者设备apikey时, api-key为Masterkey; 当该命令用于新增数据流或者数据点时, api-key为Masterkey或者设备apikey均可。
> 3. 当AT^ONENETPOST命令用于申请新增设备ID或者设备apikey时, 若申请成功, 则返回数据中包含`"errno":0`和`"error":"succ"`, 如示例中返回数据为`{"error":0, "data":{"device_id":"20375535"}, "error":"succ"}`, 其中`"20375535"`为申请的设别ID; 若申请失败, 则返回数据包含`"error":*`, 其中`*`为错误码, 且不为0。例如返回数据为`{"error":6,"error":"invalid parameter: auth_info exists::abc12345678"}`, 表示鉴权信息`abc12345678`已经被使用了。

## AT^ONENETPOST(Example)
- 上传数据
```
AT+CMHTTPSET="api.heclouds.com",80,"/devices/4661184/datapoints?type=3"

OK

CONNECT OK
AT^ONENETPOST="{\"temperature\":22.5, \"humidity\":\"95.2%\"}","api-key:q0Jx
hgV8h4qKUVfc1n42z=7OAaY="

CONNNECT OK
HTTP/1.1 200 OK
Date: Tue, 06 Jun 2017 04:42:25 GMT
Content-Type: application/json
Content-Length: 26
Connection: close
Server: Apache-Coyote/1.1
Pragma: no-cache


{"errno":0,"error":"succ"}
OK
```

- 其中


  [1]: https://github.com/JackDan9/DataBase/tree/master/M6312/AT#atcmhttpset