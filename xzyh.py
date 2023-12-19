"""
new Env('小猪惠选');
注册链接http://xiaozhu.tuesjf.cn/qrcode/NickBai5943341ac69104937493a7e2644d0208e688b.png
和火锅一样的自己看着玩变量名xzyc填token(自己看着定时任务未做全)
北渡大佬修改了应该可以跑了
"""
import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor

BF = False
yc = int(os.environ.get("xzyc", "10"))

class XZHX:
    def __init__(self, ck1):
        self.token = ck1
        self.ua = "Mozilla/5.0 (Linux; Android 14; 23078RKD5C Build/UP1A.230905.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/106/YM-RT/"
        self.hd = {
            'Host': 'xiaozhu.tuesjf.cn',
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'content-type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'http://m.xiaozhu.tuesjf.cn',
            'X-Requested-With': 'cn.tll.yyjx.xzdsp',
            'Referer': 'http://m.xiaozhu.tuesjf.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }

    ##登录
    def login(self):
        url = f'http://xiaozhu.tuesjf.cn/apis/v1/user_info?token={self.token}'
        r = requests.get(url, headers=self.hd).json()
        code = r["msg"]
        if code == "获取成功":
            name = r["data"]["info"]["nickname"]
            balance = r["data"]["info"]["balance"]
            gold = r["data"]["info"]["gold"]
            rname = r["data"]["info"]["rank_name"]
            print(f"[{name}]登录成功，账户类型[{rname}]--储蓄金[{gold}]--零钱余额[{balance}]")
            return name
        else:
            print(f'登录失败: {r["msg"]}')
            return None

    ##获取任务id
    def ids(self):
        url = f'http://xiaozhu.tuesjf.cn/apis/v1/updateActive?token={self.token}'
        r = requests.get(url, headers=self.hd).json()
        code = r["code"]
        if code == 1:
            id_list = [item['id'] for item in r['data']['list']]
            hbid = r["data"]["red_order"]["id"]
            return id_list, hbid
        else:
            print("暂未获取到弹窗广告")
            return []

    ##金币奖励
    def jbjl(self, n, t):
        video_url = 'http://xiaozhu.tuesjf.cn/apis/v1/lookVideo'
        data = {'id': t, 'token': self.token}
        re = requests.post(video_url, headers=self.hd, data=data).json()
        msg = re["msg"]
        print(f"[{n}]领取金币奖励[{t}]: {msg}")
        return msg

    ##广告奖励
    def ggjl(self, u, n):
        url = "http://xiaozhu.tuesjf.cn/apis/v1/saveTankMoney"
        data = {
            'token': self.token
        }
        r = requests.post(url, headers=self.hd, data=data).json()
        msg = r["msg"]
        print(f"[{n}]第{u}领取广告奖励: {msg}")
        return msg

    ##红包奖励
    def hbjl(self, n):
        id_list, hbid = self.ids()
        url = 'http://xiaozhu.tuesjf.cn/apis/v1/LookRed'
        data = {
            'id': hbid,
            'token': self.token
        }
        r = requests.post(url, headers=self.hd, data=data).json()
        msg = r["msg"]
        print(f"[{n}]领取红包奖励: {msg}")

    def start(self):
        aa = self.login()
        if aa:
            id_list, hbid = self.ids()
            for y in id_list:
                time.sleep(yc)
                y = self.jbjl(aa, y)
                if y == "当前已领取请勿重复领取":
                    break
            time.sleep(yc)
            self.hbjl(aa)
            time.sleep(yc)
            for u in range(13):
                time.sleep(yc)
                o = self.ggjl(u, aa)
                if o == "该任务奖励已达上限":
                    break

if __name__ == "__main__":
    def BF1(ck):
        xzhx = XZHX(ck)
        xzhx.start()
    if 'xzhx_token' in os.environ:
        cookie = os.environ.get("xzhx_token")
    else:
        print("变量[xzhx_token]不存在,请设置[xzhx_token]变量后运行")
        exit(-1)
    cookies = cookie.split("&")
    i = 0
    print(f"小猪惠选共获取到{len(cookies)}个账号")

    if BF:
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(BF1, cookies)
    else:
        for ck in cookies:
            XZHX(ck).start()
            if len(cookies) > i + 1:
                print("------6s后运行下一个账号---")
                time.sleep(6)
        i += 1