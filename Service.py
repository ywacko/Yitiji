
#@author Panda
#this is a test file

from Reserve import Reserve
import MyThread
import datetime
import time


def getTime():
    day = int(datetime.datetime.now().strftime("%d"))
    hour = int(datetime.datetime.now().strftime("%H"))
    minute = int(datetime.datetime.now().strftime("%M"))
    return day, hour, minute


if __name__ == '__main__':
    day, hour, minute = getTime()
    day = 26
    t1 = MyThread.CalNumber(day, hour, minute)
    t1.start()
    t2 = MyThread.CalRank(day, hour, minute)
    t2.start()
    t3 = MyThread.CalThermodynamic(day, hour, minute)
    t3.start()
    t4 = MyThread.CalGuiding(day, hour, minute, "顺风大酒店")
    t4.start()

    time.sleep(60)
    db = Reserve()
    day, hour, minute = getTime()
    day = 26

    while True:
        print("实时：{}号{}时{}分".format(day, hour, minute))

        print("当前实时人流：{}".format(db.getNumOfPeople(day, hour, minute)))

        print("下面是品牌排行")
        res = db.getRanking(day, hour, minute)
        for rows in res:
            print("rank:{} name:{} number:{}".format(rows.get("rank"), rows.get("name"), rows.get("number")))

        print("下面是热力图")
        res = db.getThermodynamic(day, hour, minute)
        for rows in res:
            print("posx:{} posy:{} number:{}".format(rows.get("posx"), rows.get("posy"), rows.get("number")))

        print("下面是导流图")
        res = db.getGuiding(day, hour, minute)
        for rows in res:
            print("到:{} 人数:{}".format(rows.get("to"), rows.get("number")))

        time.sleep(60)
        day, hour, minute = getTime()
        day = 26

