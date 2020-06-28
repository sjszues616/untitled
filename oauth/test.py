class Apirequest():
    pass


class Url_Process():
    def __init__(self):
        pass

    def get_base_info(self):
        """
        获取请求中的 appId 请求的时间戳 token
        :return:
        """
        pass

    # def




class Oauth_Process():
    def __init__(self):
        self.password =None
    def oauthentic(self):
        """
        将获得密码 +appid +时间戳 加密获得 token
        将token比对
        """
        pass
    def createtoke(self):
        """生成token"""
        pass

    def get_password(self,appid):
        """根据appid 获得密码"""
        pass

    def overTime(self):
        """判断是否过期"""
        pass