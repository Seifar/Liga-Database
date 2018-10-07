import GLOBAL

def tounamentExists(name, kind, bow, date):
    return False

def writeTournament(name, kind, bow, date):
    sqltext = "INSERT INTO TOURNAMENTS ({t[0]}, {t[1]}, {t[2]}, {t[3})".format(t=GLOBAL.TABLE_tournaments)+\
              "\nVALUES ('{:s}', '{:s}', '{:s}', {:s}".format(name, kind, bow, __qtDatetoSQLDate__(date))

def __qtDatetoSQLDate__(date):
    return '{:04d}-{:02d}-{:02d}'.format(date.year(), date.month(), date.day())