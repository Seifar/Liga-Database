import unittest
import PyQt5.QtCore
import GLOBAL


class TestGlobal(unittest.TestCase):
    def test_QDateToSQL(self):
        qdate = PyQt5.QtCore.QDate(2018, 11, 18)
        self.assertEqual('2018-11-18', GLOBAL.QDateToSQL(qdate))
        qdate = PyQt5.QtCore.QDate(2018, 11, 1)
        self.assertEqual('2018-11-01', GLOBAL.QDateToSQL(qdate))
        qdate = PyQt5.QtCore.QDate(2018, 1, 18)
        self.assertEqual('2018-01-18', GLOBAL.QDateToSQL(qdate))
        qdate = PyQt5.QtCore.QDate(201, 1, 18)
        self.assertEqual('0201-01-18', GLOBAL.QDateToSQL(qdate))


if __name__ == '__main__':
    unittest.main()
