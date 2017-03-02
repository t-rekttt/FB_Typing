import requests, hashlib

API_KEY = "882a8490361da98702bf97a021ddc14d"
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
HEADERS = {
    "User-Agent" : "[FBAN/FB4A;FBAV/1.9.9;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]"
}
BASE_URL = "https://api.facebook.com/restserver.php"
CONST_ARRAY = [ 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102]

def login(email, password):
    data = {
        "generate_machine_id" : 1,
        "credentials_type" : "password",
        "method" : "auth.login",
        "email" : email,
        "password" : password,
    }

    default_parameters = {
        "api_key" : API_KEY,
        "format" : "JSON",
        "generate_session_cookies" : 1,
        "locale" : "en_US",
        "migrations_override" : "{'empty_json':true}",
        "return_ssl_resources" : 0,
        "v" : "1.0",
    }

    for k, v in default_parameters.items():
        if k not in data:
            data[k] = v
            
    # Generate message
    keys = sorted(data.keys())
    message = "".join(["%s=%s" % (k, data[k]) for k in keys])
    message = "%s%s" % (message, API_SECRET)

    # Generate signature for message
    message = message.encode("utf-8")
    m = hashlib.md5()
    m.update(message)
    digest_message = m.digest()
    arr = []
    for i in digest_message:
        k = 0xFF & ord(i)
        arr.append(chr(CONST_ARRAY[(k >> 4)]))
        arr.append(chr(CONST_ARRAY[(k & 0xF)]))
    sig = ''.join(arr)
    data["sig"] = sig

    res = requests.post(BASE_URL,data=data,verify=False)
    return res
