'''
本脚是API所写请勿频繁调用谢谢
PS:API百度搜索的所有侵权请联系@sylm1删除
'''
import requests
import os
class AC:
    def __init__(self, account, password, step):
        self.Account = account
        self.Password = password
        self.Step = step
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220133 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android"
        }
    def Brushstep(self):
        url = f"https://api.yyink.cn/api/mi?user={self.Account}&password={self.Password}&step={self.Step}"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        if data['code'] == 200:
            userNickname = data['msg']
            print(f"账户 {self.Account} 刷步成功，用户昵称：{userNickname}")
        else:
            msg = data["msg"]
            print(f"账户 {self.Account} 刷步失败：{msg}")
if __name__ == "__main__":
    xmyd = os.environ.get('xmyd')
    if not xmyd:
        print("请设置环境变量 'xmyd' 后再运行")
    else:
        xmyd_list = xmyd.split('#')
        for xmyd_item in xmyd_list:
            try:
                account, password, step = xmyd_item.split('&')
                ac = AC(account, password, step)
                ac.Brushstep()
            except ValueError:
                print(f"请按照'账号&密码&需要刷的步数'的形式多号#隔开")
