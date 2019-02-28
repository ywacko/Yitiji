
#@author Panda

import pymysql
import datetime

class Helper:
    """
    mySQL主体，计算需要的数据
    """
    def __init__(self):
        self.db = pymysql.connect(
            host = "10.200.187.88",
            user = "root",
            passwd = "123",
            db = "edu")
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    @staticmethod
    def transDay(day):
        """
        把小于10的日期变成两位数格式
        :param day:
        :return:
        """
        if day < 10:
            return "0" + str(day)
        else:
            return day

    def pi(self, day, hour, min):
        """
        客户画像
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT tag, SUM(macnumber) AS total 
              FROM 
              (SELECT dt_year,dt_month,shop_name,COUNT(DISTINCT mac) AS macnumber 
              FROM tb_andatong_{} 
              WHERE (dt_hour < {} OR (dt_hour = {} AND dt_min <= {}))
							AND shop_type IS NOT NULL 
              GROUP BY dt_year,dt_month,shop_name   
			  ORDER BY macnumber DESC
              ) a 
              LEFT JOIN 
              (SELECT * 
              FROM ods_test_brandtype 
              )c 
              ON a.shop_name = c.name 
              WHERE tag IS NOT NULL 
              GROUP BY dt_year,dt_month,tag 
              ORDER BY total DESC
			  LIMIT 4;""".format(self.transDay(day), hour, hour, min)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)


    def buy(self, day, hour, min):
        """
        购买转化潜力
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT g.leixing, avg(f.avgstay) AS ast, avg(f.avgtime) AS ati 
                 FROM (SELECT dt_month, shop_name, avg(e.po)/30 AS avgstay, avg(e.ti)/60 AS avgtime  
                 FROM (SELECT c.dt_day, c.dt_month, c.shop_name, c.macnum/c.mac_total AS po, b.stay_time/c.mac_total AS ti 
                 FROM (SELECT dt_day, dt_month, shop_name , count(mac) AS macnum, count(DISTINCT mac) AS mac_total 
                 FROM tb_andatong_{}
                 WHERE (dt_hour < {} OR (dt_hour = {} AND dt_min <= {})) AND shop_name IS NOT NULL 
                 GROUP BY dt_day, dt_month, shop_name) c 
                 LEFT JOIN 
                 (SELECT dt_day, dt_month, shop_name, sum(tm_end - tm_begin) AS stay_time 
                 FROM (SELECT dt_day, dt_month, shop_name, max(time_stamp) AS tm_end , min(time_stamp) AS tm_begin 
                 FROM tb_andatong_{} 
                 WHERE (dt_hour < {} OR (dt_hour = {} AND dt_min <= {})) AND shop_name IS NOT NULL 
                 GROUP BY dt_day, dt_month,mac,shop_name) a 
                 WHERE tm_end- tm_begin > 30 AND tm_end- tm_begin < 10800 
                 GROUP BY dt_day, dt_month,shop_name) b 
                 ON c.shop_name = b.shop_name AND c.dt_day = b.dt_day)e 
                 GROUP BY dt_month,shop_name ORDER BY avgtime DESC)f 
                 LEFT JOIN 
                 (SELECT name, leixing FROM ods_test_brandtype)g 
                 ON f.shop_name = g.name 
                 GROUP BY f.dt_month, g.leixing;""".format(self.transDay(day), hour, hour, min, self.transDay(day), hour, hour, min)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def guiding(self, day, hour, min):
        """
        导流图
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT d.mac, d.shop_name 
                 FROM tb_andatong_{} d
                 WHERE (d.dt_hour < {} OR (d.dt_hour = {} AND d.dt_min <= {}))
                 AND d.locname = '1F' 
                 AND d.shop_name <> 'null'
                 AND d.shop_name <> '走道'
                 ORDER BY d.mac, d.time_stamp;""".format(self.transDay(day), hour, hour, min)
        try:
            self.cursor.execute(sql)
            pre = self.cursor.fetchall()
            fromTo = []
            if len(pre) > 0:
                for i in range(1, len(pre)):
                    if pre[i][0] == pre[i - 1][0]:
                        if pre[i][1] != pre[i - 1][1]:
                            fromTo.append({"from":pre[i - 1][1],"to":pre[i][1]})
            res = {}
            for rows in fromTo:
                ft = rows.get("from") + "_" + rows.get("to")
                if ft in res:
                    res[ft] += 1
                else:
                    res[ft] = 1
            return res
        except Exception as e:
            print(e)

    def average(self, day, hour, min):
        """
        平均停留时长以及总人数
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT MAX(d.date_time), MIN(d.date_time) FROM tb_andatong_{} d
                 WHERE (d.dt_hour < {} OR (d.dt_hour = {} AND d.dt_min <= {}))
                 AND d.locname = '1F'
                 GROUP BY d.mac;""".format(self.transDay(day), hour, hour, min)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            total = len(res)
            t = datetime.timedelta(seconds=0, minutes=0, hours=0)
            for rows in res:
                t1 = datetime.datetime.strptime(rows[0], "%Y-%m-%d %H:%M:%S")
                t2 = datetime.datetime.strptime(rows[1], "%Y-%m-%d %H:%M:%S")
                t += t1 - t2
            if total > 0:
                average = int((t / total).total_seconds() / 60)
            else:
                average = 0
            return [total, average]
        except Exception as e:
            print(e)

    def numberOfPeople(self, day, hour, min):
        """
        今日实时人流
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT d.dt_hour, d.dt_min, COUNT(DISTINCT d.mac) AS NumberOfPeople 
                 FROM tb_andatong_{} d
                 WHERE (d.dt_hour < {} OR (d.dt_hour = {} AND d.dt_min <= {}))
                 AND d.locname = '1F'
                 GROUP BY d.dt_day, d.dt_hour, d.dt_min;""".format(self.transDay(day), hour, hour, min)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def thermodynamic(self, day, hour, min):
        """
        品牌热力图
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT d.posx, d.posy, COUNT(d.mac) AS Thermodynamic 
                 FROM tb_andatong_{} d 
                 WHERE d.dt_hour = {} 
                 AND d.dt_min = {}
                 AND d.locname = '1F'
                 GROUP BY d.posx, d.posy;""".format(self.transDay(day), hour, min)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def ranking(self, day, hour, min):
        """
        品牌人流排行榜
        :param day:
        :param hour:
        :param min:
        :return:
        """
        sql = """SELECT d.shop_name, COUNT(DISTINCT d.mac) FROM tb_andatong_{} d
                 WHERE (d.dt_hour < {} OR (d.dt_hour = {} AND d.dt_min <= {}))
                 AND d.locname = '1F'
                 AND d.shop_name <> "null"
                 AND d.shop_name <> '走道'
                 GROUP BY d.shop_name
                 ORDER BY COUNT(DISTINCT d.mac) DESC
                 LIMIT 10""".format(self.transDay(day), hour, hour, min)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
