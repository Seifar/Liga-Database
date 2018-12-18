import sqlite3
import threading

__initialised__ = False
__lock__ = None
__con__ = None
__cursor__ = None
__dbName__ = "scores.db"

TABLE_name_tournaments = 'tournaments'
TABLE_tournaments = ["NAME", "KIND", "BOW", "DATE"]


def __init__ ():
    global  __initialised__, __lock__, __con__, __cursor__, __dbName__
    if (__initialised__):
        return
    __lock__ = threading.RLock()
    __con__ = sqlite3.connect(__dbName__)
    __cursor__ = __con__.cursor()

def executeSQL(sqlcode):
    global __cursor__, __con__
    __init__()
    print(sqlcode)
    ret = __cursor__.execute(sqlcode)
    __con__.commit()
    return ret

def QDateToSQL(qdate):
    #YYYY-MM-DD
    return "{:04d}-{:02d}-{:02d}".format(qdate.year(), qdate.month(), qdate.day())
