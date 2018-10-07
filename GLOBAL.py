import sqlite3
import threading

__initialised__ = False
__lock__ = None
__con__ = None
__cursor__ = None
__dbName__ = "scores.db"

TABLE_tournaments = ["NAME", "KIND", "BOW", "DATE"]

def __init__ ():
    if (__initialised__):
        return
    __lock__ = threading.RLock()
    __con__ = sqlite3.connect("db")
    __cursor__ = __con__.cursor()

def executeSQL(sqlcode):
    __init__()
    ret = __cursor__.execute(sqlcode)
    __con__.commit()
    return ret