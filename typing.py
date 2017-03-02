import requests, time, fblogin, re, find
requests.packages.urllib3.disable_warnings()
def assign(filename):
        file = open(filename,"r");
        info = {}
        data = file.read()
        for lines in data.split("\n"):
            if "=" in lines:
                vals = lines.strip().split('=', 1)
                info[vals[0]]=vals[1];
        return info

def typing(receiver):
    data = {
        "typ":"1",
        "to":receiver,
        "fb_dtsg":fb_dtsg,
    }
    resp = requests.post("https://www.facebook.com/ajax/messaging/typ.php?dpr=1",data=data,headers=REQUEST_HEADERS, allow_redirects=True,verify=False)

def scrape(json):
    keys = json['session_cookies']
    result = ''
    for key in keys:
        result+=key["name"]+"="+key["value"]+'; '    
    token = json['access_token']
    return {'token':token,'cookie':result}

def do_full():
    friends_count = friends['friends']['summary']['total_count']
    friendlist_json = requests.get('https://graph.facebook.com/v1.0/me?fields=friends&access_token='+info['token'],verify=False).json()
    global friendlist
    friendlist = friendlist_json['friends']['data']
    print('Fetching friend list: Successful')
    try:
        while (1>0):
            for friend in friendlist:
                typing(friend['id'])
                print("Typed: "+friend['id'])
            print('Sleeping '+str(sleeptime)+'s')
            time.sleep(sleeptime)
    except Exception as e:
        print(e)
        pass

def do_list():
    f = open("list.txt","r")
    friendlist = f.read().strip().split("\n")
    print('Fetching list: Successful')
    try:
        while (1>0):
            for friend in friendlist:
                typing(friend)
                print("Typed: "+friend)
            print('Sleeping '+str(sleeptime)+'s')
            time.sleep(sleeptime)
    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    account_info = assign("account_info.txt")
    if not ('login' or 'pass' or 'mode' in account_info.keys()):
        print("Login data not specified")
        exit
    print('Fetching account info: Successful')
    session = fblogin.login(account_info['login'],account_info['pass'])
    json = session.json()
    if ('error_data' in json.keys()):
        print(json['error_data']['error_title'])
        exit
    print('Login: Successful')
    info = scrape(json)
    #global friends
    friends = requests.get('https://graph.facebook.com/v2.8/me?fields=friends.limit(0).summary(total_count)&access_token='+info['token'],verify=False).json()
    if ('friends' in friends):
        REQUEST_HEADERS = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, sdch',
        'accept-language': 'en-US,en;q=0.8,en-AU;q=0.6',
        'cookie': info["cookie"],
        'dnt': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
        }
        html = requests.get('https://m.facebook.com/',headers=REQUEST_HEADERS,verify=False)
        fb_dtsg = find.find_between(html.text,'"token":"','"')
        if (fb_dtsg):
            print('Fetching session: Successful')
            sleeptime=25
            if (account_info['mode'] == 'list'):
                do_list()
            else:
                do_full()               
