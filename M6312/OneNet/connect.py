# -*- coding: utf-8 -*-

import requests
import json
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# DEVICEID 设备的ID

DEVICEID = '30969606'

# SENDDATAID 是数据流名称

SENDDATAID = 'teet1'

# VALUE 数据流数值

VALUE = 50

# APIKEY 设备的APIKEY

APIKEY = 'Yh=HF66cqSgSOtV3gmLGr0wU3BA='

url = 'http://api.heclouds.com/devices/%s/datapoints' % (DEVICEID)

dict = {"datastreams": [{"id":"teet1", "datapoints": [{"value":"22.5"}]}]}

dict['datastreams'][0]['id'] = SENDDATAID

dict['datastreams'][0]['datapoints'][0]['value'] = VALUE

send_data = json.dumps(dict)

print(send_data)

headers = {
    "api-key":APIKEY,
    "Connection":"close"
}

ret = requests.post(url, headers=headers, data=send_data)

print(ret.headers)
print('1', 20 * '*')
print(ret.text)
print('2',20 * '*')
