
'''
new Env('天瑞地安——共富签');
变量名：共富签抓Authorization(有些号动态验证签到自己看看)
q群：777974608（不定时开关）
'''
import requests
import os
import json


auth_string = os.getenv('gfq')
auth_list = auth_string.split('@')

url = 'https://crm.rabtv.cn/v2/index/signIn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://crm.rabtv.cn',
    'X-Requested-With': 'com.test.android.app.ruian',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://crm.rabtv.cn/sign/index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

counter = 1  

for auth in auth_list:   
    headers['Authorization'] = auth
    
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        code = data['code']
        if code == 0:
            print(f"第 {counter} 个账号签到失败:", data['msg'])
        else:
            score = data['data']['score']
            thumb_url = data['data']['info']['thumb']
            continue_sign_num = data['data']['continue_sign_num']
            print(f"第 {counter} 个账号签到成功，得分为{score}，连续签到次数{continue_sign_num}")
        
        counter += 1  
    else:
        print("请求失败，状态码为:", response.status_code)