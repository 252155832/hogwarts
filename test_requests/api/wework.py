import requests


class WeWork():
    #定义获取token方法
    def get_token(self):
        corpid = "ww95b3f1588d81d39c"
        corpsecret = "PtPA7Ck7U6gkkkUrssV54pnSJ9E-PKhghii6qZFEj-Y"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        #返回access_token值，他模块调用token方法时使用
        return r.json()["access_token"]
