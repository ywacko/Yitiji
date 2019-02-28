import datetime
import Domain
from Helper import Helper
from Reserve import Reserve
import pymysql
from pymongo import MongoClient
import pymongo


# db = pymysql.connect(
#             host = "10.200.187.88",
#             user = "root",
#             passwd = "123",
#             db = "edu")
# cursor = db.cursor()
# sql = """SELECT d.mac, d.shop_name FROM tb_andatong_09 d
# ORDER BY d.mac, d.time_stamp, d.shop_name;"""
# cursor.execute(sql)
# a = cursor.fetchall()
# l = len(a)
# OK = False
# for i in range(1,l):
#     if a[i][0] == a[i - 1][0]:
#         if a[i][1] == a[i - 1][1]:
#             OK = True
#         else:
#             if OK:
#                 sql = """insert into hahah values
#                      ('{}', '{}', {})""".format(a[i - 1][0], a[i - 1][1],i)
#                 cursor.execute(sql)
#                 db.commit()
#                 OK = False
# if OK:
#     sql = """insert into hahah values
#             ('{}', '{}', {})""".format(a[l - 1][0], a[l - 1][1], l)
#     cursor.execute(sql)
#     db.commit()



# sql = """SELECT (MAX(time_stamp)-MIN(time_stamp))/60 as a, mac
# FROM tb_andatong_09
# GROUP BY mac
# HAVING (MAX(time_stamp)-MIN(time_stamp)) / 3600 < 8
# ORDER BY a DESC"""
# cursor.execute(sql)
# a = cursor.fetchall()
# client = MongoClient(host = "localhost", port = 27017)
# dbb = client.edu
# co = dbb.abc
# b = {}
# c = [0 for i in range(22)]
# for rows in a:
#     r = float(rows[0])
#     if b.get(r):
#         b[r] += 1
#     else:
#         b[r] = 1
# for rows in b:
#     if rows == 0:
#         c[0] += b[rows]
#     elif rows <= 1:
#         c[1] += b[rows]
#     elif rows <= 1.5:
#         c[2] += b[rows]
#     elif rows <= 2:
#         c[3] += b[rows]
#     elif rows <= 3.7:
#         c[4] += b[rows]
#     elif rows <= 6.1:
#         c[5] += b[rows]
#     elif rows <= 11.6:
#         c[6] += b[rows]
#     elif rows <= 24.83:
#         c[7] += b[rows]
#     elif rows <= 56.35:
#         c[8] += b[rows]
#     elif rows <= 69.05:
#         c[9] += b[rows]
#     elif rows <= 122.6:
#         c[10] += b[rows]
#     elif rows <= 218:
#         c[11] += b[rows]
#     else: c[12] += b[rows]
# data = {}
# for i in range(13):
#     data[str(i)] = c[i]
# co.insert(data)


# b = {}
# if b.get(1.2): print(123)
# b[1.2] = 1
# if b[1.2]: print(456)
# print(b[1.2])
# for rows in b:
#     print(rows)
# now = datetime.datetime.now().strftime("%d")
# print(now)
#
# a = datetime.datetime.now().strftime("%H")
# print(int(a))
# #time.sleep(5)
#
# now2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
# print(now < now2)
#
# print("""SELECT COUNT(DISTINCT d.mac) AS NumberOfPeople
#                  FROM tb_andatong_25 d
#                  WHERE d.dt_day = {} and d.dt_hour = {} and d.dt_min = {};""".format(1, 2, 3))

# sec = int(datetime.datetime.now().strftime("%S"))
# print(sec)
# print(int(sec/10))
# day = 1
# hour = 20
# min = 0
# sec = 0
#
# data = {'$and': [{'day': day},
#                  {'$or': [{'dt_hour': {'$lt': hour}},
#                           {'$and': [{'dt_hour': hour}, {'dt_min': {'$lt': min}}]},
#                           {'$and': [{'dt_hour': hour}, {'dt_min': min}, {'dt_sec': {'$lte': sec}}]}]}]}
#
# client = MongoClient(host = "10.200.187.88", port = 27017)
# db = client.edu
# co = db.edu_guiding
# r = co.find(data).sort([('dt_hour',pymongo.ASCENDING),('dt_min',pymongo.ASCENDING),('dt_sec',pymongo.ASCENDING)])
# res = []
# for rows in r:
#     print(rows)

# data = {"day": day, "hour": hour, "min": min, "sec": sec}
# res = co.find_one(data)
# print(res)
# minute1 = int(datetime.datetime.now().strftime("%M"))
# second1 = int(datetime.datetime.now().strftime("%S"))
# res = []
# # data = {"day": day, "hour": hour, "min": min, "sec": sec}
# data = {"day":day,"hour":hour,"min":min,"sec":sec,"from":"OMEGA"}
# r = co.find(data)
# for rows in r:
#     print(rows)
import time
time1 = time.time()
for i in range(0, 1000):
    for j in range (0, 1000):
        for k in range(0, 1000):
            s = i * j * k
time2 = time.time()
print(time2 - time1)
# minute2 = int(datetime.datetime.now().strftime("%M"))
# second2 = int(datetime.datetime.now().strftime("%S"))
# print(minute1,second1,minute2,second2)

# for rows in r:
#     print(rows)

#
# time1 = datetime.datetime.now()
# time.sleep(5)
# time2 = datetime.datetime.now()
# print(type(time2-time1))
# a = {"222":2}
# if "222" in a:
#     a["222"] += 1
# print(a.get("222"))
# a["333"] = 1
# print(a["333"])
# print(a)
# a["444"] = 1
# print(a)
# c = "1111_2222"
# print(c.split("_"))
# for rows in a:
#     print(a[rows])
#
# a = time.time()
# time.sleep(5)
# b = time.time()
# print(b - a)
# print(int(b - a) == 5)

# sqlDb = Helper()
# mongoDb = Reserve()
# res = sqlDb.guiding("26", "20", "25")
# mongoDb.storeGuiding("26", "20", "25", res)
# a = mongoDb.getGuiding("26", "20", "25")
# for rows in a:
#     print(rows)
# db = Helper()
# a = db.numberOfPeople("25", "24", "55")
# print(a[0][0])
# a = db.ranking("26", "24","55")
# print(a)
# a = db.thermodynamic("26", "10", "21")
# print(a)
# db.prepare("26")
# print(len(db.fromTo))
# dd = Reserve()
# a = dd.getRanking("29", "10", "56")
# print(a)
# dd.storeThermodynamic("26", "10", "21", a)
# a = dd.getThermodynamic("26", "10", "21")
# print(a)

# ddd = Reserve()
# a = ddd.getRanking(1,2,3)
# print(a)

# # ddd.storeNumOfPeople(25,18,55,666)
# a = ddd.getNumOfPeople(25,18,55)
# print(a)
# co = ddd.db.number
# data = {"day":25,"hour":18,"min":55}
# a = co.find_one(data)
# print(int(a.get("number")))
# for i in range(1,5):
#     print(i)

# a = {"bi_value":{"1":1}}
# a["bi_value"] = {"2":2}
# a["ccc"] = 1
# print(a)
#
# sql = Helper()
# mongo = Reserve()
# a = sql.pi(25,20,25)
# print(a)
# mongo.storePi(25, 20, 25, a)
# b = mongo.getPi(25, 20, 25)
# for rows in b:
#     print(rows.get("feature"), rows.get("value"))
# # mongo.storeAverage(25,20,25,a)
# # b = mongo.getAverage(25,20,25)
# # print(b.get("total"))
# a = sql.buy(25,10,25)
# print(float(a[1][1]))
# print(a)
# mongo.storeBuy(25,10,25,a)
# b = mongo.getBuy(25,10,25)
# data = []
# for rows in b:
#     data.append({"type": rows.get("type"), "a": rows.get("a"), "b": rows.get("b")})
# print(data)

from dateutil.parser import parse

# a = "{'a':1}"
# b = dict(a)
# print(b)
# a = 1
# print(str(a))
# a = "0" + str(a)
# print(a)
# day = int(datetime.datetime.now().strftime("%d"))
# b = "aaaaaa{}".format(a)
# print(b)
# print("0" + str(day))
# print(Domain.GUIDE_TIME)
# Domain.GUIDE_TIME = 2
# print(Domain.GUIDE_TIME)

# def aaa():
#     return False
# print(5 % 2)
# a = False
# if aaa():
#     print(1)
# for i in range(0, 50, 2):
#     print(i)