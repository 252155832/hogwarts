from test_requests.api.tagname import TagName
from test_requests.api.wework import WeWork


class Testtagname():
    #定义setup方法，用例执行前先执行实例化方法
    def setup_class(self):
        wework = WeWork()
        self.token = wework.get_token()
        self.tagname = TagName()
    def test_creat_tagname(self):
        #调用创建标签方法，并传入token值与id
        self.tagname.creat_tagname(self.token,3)
        list = self.tagname.get_tagname_list(self.token)
        assert list["taglist"][0]["tagname"] == "测试1"
    def test_update_tagname(self):
        #调用更新标签方法，并传入token值与id
        self.tagname.update_tagname(self.token,3)
        list = self.tagname.get_tagname_list(self.token)
        assert list["taglist"][0]["tagname"] == '测试2'
    def test_delete_tagname(self):
        #调用删除标签方法，并传入token值与id
        self.tagname.delete_tagname(self.token,3)
        list = self.tagname.get_tagname_list(self.token)
        assert len(list["taglist"]) == 0
    def test_get_tagname(self):
        #调用获取标签列表方法，并传入token值
        list = self.tagname.get_tagname_list(self.token)



