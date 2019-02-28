
#@author Panda

import threading
from Helper import Helper
from Reserve import Reserve
import Domain


class CalPi(threading.Thread):
    """
    客户画像线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearPi()
        d = int(self.day)
        for h in range(9, 23):
            Domain.PI_HOUR = h
            for m in range(0, 60):
                res = sqlDb.pi(d, h, m)
                mongoDb.storePi(d, h, m, res)
                Domain.PI_MIN = m
        sqlDb.close()


class CalAverage(threading.Thread):
    """
    平均停留时间和总人数线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearAverage()
        d = int(self.day)
        for h in range(9, 23):
            Domain.AVE_HOUR = h
            for m in range(0, 60):
                res = sqlDb.average(d, h, m)
                mongoDb.storeAverage(d, h, m, res)
                Domain.AVE_MIN = m
        sqlDb.close()

class CalNumber(threading.Thread):
    """
    实时人流线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearNum()
        d = int(self.day)
        for h in range(9, 23):
            Domain.NUM_HOUR = h
            for m in range(0, 60):
                res = sqlDb.numberOfPeople(d, h, m)
                mongoDb.storeNumOfPeople(d, h, m, res)
                Domain.NUM_MIN = m
        sqlDb.close()


class CalRank(threading.Thread):
    """
    品牌人流排行线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearRanking()
        d = int(self.day)
        for h in range(9, 23):
            Domain.RANK_HOUR = h
            for m in range(0, 60):
                res = sqlDb.ranking(d, h, m)
                mongoDb.storeRanking(d, h, m, res)
                Domain.RANK_MIN = m
        sqlDb.close()


class CalThermodynamic(threading.Thread):
    """
    品牌热力图线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearThermodynamic()
        d = int(self.day)
        for h in range(9, 23):
            Domain.THE_HOUR = h
            for m in range(0, 60):
                res = sqlDb.thermodynamic(d, h, m)
                mongoDb.storeThermodynamic(d, h, m, res)
                Domain.THE_MIN = m
        sqlDb.close()


class CalGuiding(threading.Thread):
    """
    品牌导流图线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearGuiding()
        d = int(self.day)
        for h in range(9, 23):
            Domain.GUIDE_HOUR = h
            for m in range(0, 60):
                res = sqlDb.guiding(d, h, m)
                mongoDb.storeGuiding(d, h, m, res)
                Domain.GUIDE_MIN = m
        sqlDb.close()

class CalBuy(threading.Thread):
    """
    购买转化潜力线程
    """
    def __init__(self, day, hour, min):
        threading.Thread.__init__(self)
        self.day = day
        self.hour = hour
        self.min = min

    def run(self):
        sqlDb = Helper()
        mongoDb = Reserve()
        # mongoDb.clearBuy()
        d = int(self.day)
        for h in range(9, 23):
            Domain.BUY_HOUR = h
            for m in range(0, 60):
                res = sqlDb.buy(d, h, m)
                mongoDb.storeBuy(d, h, m, res)
                Domain.BUY_MIN = m
        sqlDb.close()