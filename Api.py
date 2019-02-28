
#@author Panda

from FraHandler import FraHandler
from Reserve import Reserve
import Application
import json
import Domain

def myMax(a, b, c, d):
    if a > c :
        return c, d
    elif a < c :
        return a, b
    else:
        if b >= d:
            return c, d
        else:
            return a, b

def myControl(h, m):
    if m % 2 == 0:
        return h, m
    else:
        return h, m - 1


class NumHandler(FraHandler):

    def post(self):
        # day, hour1, minute1 = Application.getTime()
        # hour, minute = myMax(Domain.AVE_HOUR, Domain.AVE_MIN, Domain.NUM_HOUR, Domain.NUM_MIN)
        # hour, minute = myMax(hour1, minute1, hour, minute)

        # new
        day, hour, minute = Application.getTime()
        if minute >= 0:
            db = Reserve()
            num = db.getNumOfPeople(day, hour, minute)
            data = []
            for rows in num:
                data.append({"dt_hour":rows.get("dt_hour"),"dt_min":rows.get("dt_min"),"count":rows.get("number")})
            ave = db.getAverage(day, hour, minute)
            res = {"code":200,"number":ave.get("total"),"average":ave.get("average"),"data":data,"hour":hour,"min":minute}
            self.write(json.dumps(res))


class RankHandler(FraHandler):

    def post(self):
        # day, hour1, minute1 = Application.getTime()
        # hour, minute = myMax(hour1, minute1, Domain.RANK_HOUR, Domain.RANK_MIN)

        # new
        day, hour, minute = Application.getTime()
        if minute >= 0:
            db = Reserve()
            rank = db.getRanking(day, hour, minute)
            data = []
            Domain.GUIDE_PLACE = rank[0].get("name")
            for rows in rank:
                data.append({"name":rows.get("name"),"value":rows.get("number")})
            res = {"code":200,"data":data,"hour":hour,"min":minute}
            self.write(json.dumps(res))


class TheHandler(FraHandler):

    def post(self):
        # day, hour1, minute1 = Application.getTime()
        # hour, minute = myMax(hour1, minute1, Domain.THE_HOUR, Domain.THE_MIN)

        # new
        day, hour, minute = Application.getTime()
        if minute >= 0:
            db = Reserve()
            thermodynamic = db.getThermodynamic(day, hour, minute)
            data = []
            for rows in thermodynamic:
                data.append({"y":rows.get("posy"),"x":rows.get("posx"),"count":rows.get("number")})
            res = {"code":200,"data":data,"hour":hour,"min":minute}
            self.write(json.dumps(res))


class GuideHandler(FraHandler):

    def post(self):
        # day, hour1, minute1 = Application.getTime()
        # hour, minute = myMax(hour1, minute1, Domain.GUIDE_HOUR, Domain.GUIDE_MIN)

        # new
        day, hour, minute = Application.getTime()
        if minute >= 0:
            # hour, minute = myControl(hour, minute)
            db = Reserve()
            place = Domain.GUIDE_PLACE
            guide = db.getGuiding(day, hour, minute, place)
            total = 0
            for rows in guide:
                total += int(rows.get("number"))
            data = []
            for rows in guide:
                data.append({"bi_value":{"total":total,"to_name":rows.get("to"),
                             "from_name":place,"times":rows.get("number")}})
            res = {"code":200,"data":data,"hour":hour,"min":minute}
            self.write(json.dumps(res))


class PiHandler(FraHandler):

    def post(self):
        # day, hour1, minute1 = Application.getTime()
        # hour, minute = myMax(hour1, minute1, Domain.PI_HOUR, Domain.PI_MIN)

        # new
        day, hour, minute = Application.getTime()
        if minute >= 0:
            # hour, minute = myControl(hour, minute)
            db = Reserve()
            buy = db.getPi(day, hour, minute)
            value = []
            categories = []
            for rows in buy:
                value.append(rows.get("value"))
                categories.append(rows.get("feature"))
            data = {"value":value,"categories":categories}
            res = {"code":200,"data":data,"hour":hour,"min":minute}
            self.write(json.dumps(res))


class BuyHandler(FraHandler):

    def post(self):
        # day, hour1, minute1 = Application.getTime()
        # hour, minute = myMax(hour1, minute1, Domain.BUY_HOUR, Domain.BUY_MIN)

        # new
        day, hour, minute = Application.getTime()
        if minute >= 0:
            # hour, minute = myControl(hour, minute)
            db = Reserve()
            buy = db.getBuy(day, hour, minute)
            data = []
            for rows in buy:
                data.append({"name":rows.get("type"),"data":[rows.get("a"),rows.get("b")]})
            res = {"code":200,"data":data,"hour":hour,"min":minute}
            self.write(json.dumps(res))