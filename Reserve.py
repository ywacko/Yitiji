
#@author Panda

from pymongo import MongoClient

KEY = 0.699693


class Reserve:

    """
    MongoDB主体，把SQL中提取的数据转存入MongoDB以及调用
    """
    def __init__(self):
        self.client = MongoClient(host = "10.200.187.88", port = 27017)
        self.db = self.client.edu

    #平均停留时间和总人数
    def clearAverage(self):
        co = self.db.average
        co.drop()

    def storeAverage(self, day, hour, min, res):
        co = self.db.average
        data = {"day":day,"hour":hour,"min":min,"total":int(int(res[0]) * KEY),"average":res[1]}
        co.insert(data)

    def getAverage(self, day, hour, min):
        co = self.db.average111
        data = {"day":day,"hour":hour,"min":min}
        res = co.find_one(data)
        return res

    #今日实时人流
    def clearNum(self):
        co = self.db.number
        co.drop()

    def storeNumOfPeople(self, day, hour, min, res):
        co = self.db.number
        for rows in res:
            dt_hour = rows[0]
            dt_min = rows[1]
            num = rows[2]
            data = {"day":day,"hour":hour,"min":min,"dt_hour":dt_hour,"dt_min":dt_min,"number":int(int(num) * KEY)}
            co.insert(data)

    def getNumOfPeople(self, day, hour, min):
        co = self.db.number111
        data = {"day":day,"hour":hour,"min":min}
        r = co.find(data)
        res = []
        for rows in r:
            res.append(rows)
        return res

    #品牌人流排行
    def clearRanking(self):
        co = self.db.rank
        co.drop()

    def storeRanking(self, day, hour, min, res):
        co = self.db.rank
        i = 0
        for rows in res:
            name = rows[0]
            num = rows[1]
            data = {"day":day,"hour":hour,"min":min,"name":name,"number":int(int(num) * KEY),"rank": i + 1}
            co.insert(data)
            i += 1
            if i == 10: break

    def getRanking(self, day, hour, min):
        co = self.db.rank111
        res = []
        for i in range(1, 11):
            data = {"day":day,"hour":hour,"min":min,"rank":i}
            r = co.find_one(data)
            if r:
                res.append(r)
        return res

    #品牌热力图
    def clearThermodynamic(self):
        co = self.db.thermodynamic
        co.drop()

    def storeThermodynamic(self, day, hour, min, res):
        co = self.db.thermodynamic
        for rows in res:
            posx = rows[0]
            posy = rows[1]
            num = rows[2]
            data = {"day":day,"hour":hour,"min":min,"posx":posx,"posy":posy,"number":num}
            co.insert(data)

    def getThermodynamic(self, day, hour, min):
        co = self.db.thermodynamic111
        data = {"day": day, "hour": hour, "min": min}
        r = co.find(data)
        res = []
        for rows in r:
            res.append(rows)
        return res

    #品牌导流图
    def clearGuiding(self):
        co = self.db.guiding
        co.drop()

    def storeGuiding(self, day, hour, min, res):
        co = self.db.guiding
        for rows in res:
            fromTo = rows.split("_")
            num = res.get(rows)
            data = {"day":day,"hour":hour,"min":min,"from":fromTo[0],"to":fromTo[1],"number":num}
            co.insert(data)

    def getGuiding(self, day, hour, min, place):
        co = self.db.guiding111
        data = {"day":day,"hour":hour,"min":min,"from":place}
        r = co.find(data)
        res = []
        for rows in r:
            res.append(rows)
        return res

    #购买转化潜力
    def clearBuy(self):
        co = self.db.buy
        co.drop()

    def storeBuy(self, day, hour, min, res):
        co = self.db.buy
        for rows in res:
            if rows[0]:
                if rows[1]: a = float(rows[1])
                else: a = 0
                if rows[2]: b = float(rows[2])
                else: b = 0
                data = {"day":day,"hour":hour,"min":min,"type":rows[0],"a":a,"b":b}
                co.insert(data)

    def getBuy(self, day, hour, min):
        co = self.db.buy111
        data = {"day":day,"hour":hour,"min":min}
        r = co.find(data)
        res = []
        for rows in r:
            res.append(rows)
        return res

    #客户画像
    def clearPi(self):
        co = self.db.pi
        co.drop()

    def storePi(self, day, hour, min, res):
        co = self.db.pi
        for rows in res:
            feature = rows[0]
            if rows[1]:
                value = int(rows[1])
            else:
                value = 0
            data = {"day":day,"hour":hour,"min":min,"feature":feature,"value":value}
            co.insert(data)

    def getPi(self, day, hour, min):
        co = self.db.pi111
        data = {"day":day,"hour":hour,"min":min}
        r = co.find(data)
        res = []
        for rows in r:
            res.append(rows)
        return res
