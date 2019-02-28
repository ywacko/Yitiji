#coding:utf-8
__author__ = 'Xiaodong.Yang'

"""
CopyRight(c)  FraPlus.Corp 2017
Date : 2017-06-15
"""
import json
import datetime
from tornado.web import RequestHandler

class FraHandler(RequestHandler):  # , SessionMixin):
    """
    为了能够更好地使用RequestHandler,方便定制个性化内容
    派生出该类，主要特性包括:
    1. 覆盖 options方法，支持客户端options请求
    2. 设置HTTP头，支持跨域访问
    """
    def options(self, *args, **kwargs):
        pass

    # 跨域访问
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "Origin, X-Requested-With, Content-Type")
        self.set_header("Access-Control-Allow-Methods",
                        "PUT,GET,POST,DELETE,OPTIONS")
        self.set_header("Access-Control-Allow-Credentials", "true")

    # 获取时间
    def get_date(self):
        now = datetime.datetime.now()
        paydate = now.strftime("%Y-%m-%d %H:%M:%S")
        return paydate

    def send_error(self, code=-1, msg='error'):
        ret = {}
        ret['code'] = code
        ret['msg'] = msg
        self.write(json.dumps(ret))

    def get_argument(self, name, default=object(), strip=True):
        '''
        获取网络传输参数，原始函数在无法获取参数时会抛出异常，
        重载该函数以处理异常
        :param name:
        :param default:
        :param strip:
        :return:
        '''
        rets = ''
        try:
            rets = super().get_argument(name)
        except Exception as e:
            rets = None
        return rets

