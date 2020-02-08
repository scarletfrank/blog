import urllib3
import json
import certifi

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
field_type = 'lyric'
field_id = '784198'
r = http.request('GET', 'https://api.imjad.cn/cloudmusic/', fields={'type': field_type, 'id': field_id})

a = json.loads(r.data)
b = a['lrc']['lyric']
lines = b.splitlines()

with open('output.lrc', 'w+') as f:
    for line in lines:
        f.write(line+'\n')

# https://zhuanlan.zhihu.com/p/30246788