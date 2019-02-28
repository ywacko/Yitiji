
#@author Panda
#主程序入口

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import Api
import MyThread
import datetime

def getTime():
    """
    获取当前时间
    :return:
    """
    day = int(datetime.datetime.now().strftime("%d"))
    hour = int(datetime.datetime.now().strftime("%H"))
    minute = int(datetime.datetime.now().strftime("%M"))
    #the sql table is wrong so:
    day = 28
    return day, hour, minute

def makeApp():
    """
    开启服务
    :return:
    """
    app = Application(handlers =
                      [(r"/edu/number", Api.NumHandler),
                       (r"/edu/rank", Api.RankHandler),
                       (r"/edu/guide", Api.GuideHandler),
                       (r"/edu/thermodynamic", Api.TheHandler),
                       (r"/edu/picture", Api.PiHandler),
                       (r"/edu/buy", Api.BuyHandler)])
    httpServer = HTTPServer(app)
    httpServer.listen(9000)
    IOLoop.current().start()

def makeThread():
    """
    启动多线程计算
    :return:
    """
    day, hour, minute = getTime()
    if minute % 2 != 0: minute -= 1
    t1 = MyThread.CalNumber(day, hour, minute)
    t1.start()
    t2 = MyThread.CalRank(day, hour, minute)
    t2.start()
    t3 = MyThread.CalThermodynamic(day, hour, minute)
    t3.start()
    t4 = MyThread.CalGuiding(day, hour, minute)
    t4.start()
    t5 = MyThread.CalAverage(day, hour, minute)
    t5.start()
    t6 = MyThread.CalBuy(day, hour, minute)
    t6.start()
    t7 = MyThread.CalPi(day, hour, minute)
    t7.start()


if __name__ == '__main__':
    # makeThread()
    makeApp()