# -*- coding: utf-8 -*-
"""yacalendar.py
    - yet another calendar
"""
import os,sys,calendar

if __name__ == '__main__':      # this way the module can be
    if 3 != len(sys.argv):
        print """ %s usage::
python yacalendar.py yyyy mm[比如说:2009 10 说明想看哪年哪月的]
        """
    else:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        print calendar.month(year,month)


