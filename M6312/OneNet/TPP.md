# Third-party platform

## 数据接收服务程序开发详述

### URL以及token验证
- 在用户提交与修改第三方配置时, OneNet平台会向填写URL地址发送http GET请求进行"URL和token"的验证, 当平台接收到期望的请求响应时则配置会保存成功并且能接收到相应的数据推送消息。平台发送的"URL以及token"请求形式如`http://ip:port/test?msg=xxx&nonce=xxx&signature=xxx`, `http://ip:port/test`为我们在平台配置的URL。用户数据接收服务程序在接收到OneNet平台发送的"URL以及token"验证请求时, 常规的验证流程如下:
    - 1. 在请求中获取参数"nonce"、"msg"、"signature"的值, 将"token"(如下图所示配置参数token的值)、"nonce"、"msg"的值计算MD5(token+nonce+msg)加密值, 并且编码为Base4字符串值。
    - 2.将上一步中Base4字符串值通过URL Decode计算后的值与请求参数"signature"的值进行对比, 如果相等则表示token验证成功。
    - 3. 如果token验证成功, 返回"msg"参数值, 否则返回其他值。
> 注意: 如果用户不想验证token的有效性, 可以选择忽略上述验证。

![connect][1]

### 数据接收
- 当用户成功在OneNet配置了第三方开发平台服务器地址后, OneNet平台在收到相关项目下设备数据时, 会推送到推送的服务器地址。在开发数据接收服务程序, 要注意:
    - 1. OneNet平台为了保证数据不丢失, 有重发机制, 如果重复数据对业务有影响, 数据接受端需要对重复数据进行排除重复处理。
    - 2. OneNet每一次post数据请求后, 等待客户端的响应都没有时限(目前是2秒), 在规定时限内没有收到响应会认为发送失败。接收程序接收到数据时, 尽量缓存起来, 再做业务逻辑处理。
    - 3. OneNet平台在规定时限内收到http 200的响应, 才会认为数据推送成功, 否则会重发。
    - 4. 同一产品下数据推送失败次数达到2000次, 平台会停止向该产品接收数据的URL推送数据, 第三方推送会被置为停用状态。
- 推送的数据会根据用户的配置被分为加密模式、明文模式、加密模式下要先解密, 才能看到对应的数据消息格式, 数据消息格式如下:

#### 1.1 数据消息格式
- 平台以HTTP POST请求形式向第三方平台注册地址推送数据, 推送数据相关信息以JSON串的形式置于HTTP请求中的body部分。
- 第三方平台在接受数据时, 根据加密选择, 会接收到数据的明文消息或者密文消息。
- **明文格式**:
- 1. 数据点消息(type=1)
- 示例:
```
{
    "msg": {
        "type": 1,
        "dev_id": 2016617,
        "ds_id": "datastream_id",
        "at": 1466133706841,
        "value": 42
    },
    "msg_signature": "message signature",
    "nonce": "abcdefgh"
}
```
- 2. 数据点消息批量形式(type=1)
- 示例:
```
{
    "msg": [
        {
            "type": 1,
            "dev_id": 2016617,
            "ds_id": "datastream_id",
            "at": 1466133706841,
            "value": 42
        },
        {
            "type": 1,
            "dev_id": 2016617,
            "ds_id": "datastream_id",
            "at": 1466133706842,
            "value": 43
        },
        ...
    ],
    "msg_signature": "messagesignature",
    "nonce": "abcdefgh"
}
```
- 3. 设备上下线消息(type=2)
- 示例:
```
{
    "msg": {
        "type": 2,
        "dev_id": 2016617,
        "status": 0,
        "login_type": 1,
        "at": 1466133706841
    },
    "msg_signature": "message signature",
    "nonce": "abcdefgh"
}
```

- **密文格式**
```
{
    "enc_msg": "xxxx",
    "msg_signature": "message signature",
    "nonce": "abcdefgh"
}
```

#### 说明
- 1. 如果通过api上传二进制数据点, 此时value("value": {"indx":"2258292", "bin_data":"7b64613a64617d"})中包括该二进制数据的索引indx和二进制数据bin_data(二进制数据数据限制长度为2048个字节, 如果超过该限制将不存在bin_data字段), bin_data为字符串形式代表二进制数据的十六进制字符;
- 2. 在明文传输时, 存在`msg`、`msg_signature`、`nonce`字段, 分别表示明文传输的数据、msg部分的消息摘要、用于摘要计算的随机字符串; 在加密传输时, 存在`enc_msg`、`msg_signat`。
- 上述格式中, 相关字段的具体意义说明如下:

| 字段 | 字段说明 |
| --- | --- |
| type | 标识数据类型, 当卡版本范围[1,5] |
| dev_id | 设备ID |
| ds_id | 公开协议中的数据流ID |
| at | 平台时间戳, 单位ms |
| value | 具体数据部分, 为设备上传至平台或者触发的相关数据 |
| status | 设备上下线标识 <br /> 0-下线, 1-上线 |
| login_type | 设备登陆协议类型 <br /> 1-EDP, 2-nwx, 3-JTEXT, 5-JT808, 6-MODBUS, 7-MQTT, 8-gr20 |
| cmd_type | 命令响应的类型 <br /> 1-设备收到cmd的ACK响应信息; 2-设备收到cmd的Confirm响应信息 |
| cmd_id | 命令ID |
| msg_signature | 消息摘要 |
| nonce | 用于计算消息摘要的随机串 |
| enc_msg | 加密密文消息体, 对明文JSON串(msg字段)的加密 |

#### 加密算法详述
- 平台基于AES算法提供加解密技术, 具体如下:
    - 1. EncodingAESKey即消息加解密Key的BASE64编码形式, 长度固定为43个字符, 从a-z,A-Z,0-9共62个字符串中选取。由服务开启时填写, 后也可申请修改。
    - 2. AES密钥计算为`AESKey=Base64_Decode(EncodingAESKey + "=")`, `EncodingAESKey`尾部填充一个字符的`"="`, 用`Base64_Decode`生成32个字节的`AESKey`。
    - 3. AES采用`CBC`模式, 秘钥长度为32个字节(256位), 数据采用`PKCS#7`填充 ,初始化`iv`向量取秘钥前16字节; `PKCS#7`: `K`为秘钥字节数(采用32), `buf`为待加密的内容, `N`为其字节数。`Buf`需要被填充为`K`的**整数倍**。在`buf`的尾部填充`(K-N%K)`个字节, 每个字节的内容是`(K- N%K)`。
    - 4. `BASE64`采用MIME格式, 字符包括大小写字母各26个, 加上10个数字, 和加号"+", 斜杠"/", 一共64个字符, 等号"="用作后缀填充;
    - 5. 出于安全考虑, 平台网站提供了修改`EncodingAESKey`的功能(在EncodingAESKey可能泄漏时进行修改, 对应上第三方平台申请时填写的接收消息的加密对称密钥), 所以建议保存当前的和上一次的`EncodingAESKey`, 若当前`EncodingAESKey`生成的`AESKey`解密失败, 则尝试用上一次的`AESKey`的解密。
    - 6. 平台的加密消息部分为`enc_msg= Base64_Encode`(`AES_Encrypt [random(16B)+msg_len(4B)+msg]`), 即以16字节随机字节串拼接4字节表示消息体长度的字节串(此处4字节长度表示为网络字节序),再加上消息本身的字节串作为AES加密的明文,再 以AES算法对明文进行加密生成密文,最后对密文进行BASE64的编码操作生成加密消息体。
    - 7. 对加密消息体的解密流程为：
        - 1) 首先进行加密消息体的BASE64解码操作, `aes_msg=Base64_Decode(enc_msg)`;
        - 2) 对获取的解码内容以AES算法进行解密操作, 获取明文部分, `plain_msg=AES_Decrypt(aes_msg)`, 解密中使用的秘钥由`EncodingAESKey`计算得来, 使用的初始化iv向量为计算出的aes秘钥的前16字节;
        - 3) 去掉`plain_msg`的前16字节, 再以前4字节取出消息体长度, 根据消息体长度获取真实的消息部分(推荐以消息体长度获取真实消息, 以兼容`plain_msg`未来可能出现的结构变更)。表示加密传输的数据, 后两字段与明文传输一致。



  [1]: ./images/connect.png "connect.png"