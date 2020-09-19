import requests


class TagName():
    #定义创建标签方法
    def creat_tagname(self,token,tagname_id):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        data = {
            "tagname": "测试1",
            "tagid": tagname_id
        }
        r = requests.post(url=url, json=data)
        return r.json()
    #定义更新标签方法
    def update_tagname(self,token,tagname_id):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}&tagid={tagname_id}"
        data = {
            "tagid": tagname_id,
            "tagname": "测试2"
        }
        r = requests.post(url=url, json=data)
        return r.json()
    #定义删除标签方法
    def delete_tagname(self,token,tagname_id):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={tagname_id}"
        r = requests.get(url=url)
        return r.json()
    #定义获取标签列表方法
    def get_tagname_list(self,token):
        get_tagname_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        list = requests.get(url=get_tagname_url)
        return list.json()
