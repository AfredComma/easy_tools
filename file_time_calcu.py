#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Nothing
# @Time    : 2019/6/1 上午10:14
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : file_time_calcu.py
# @Software: PyCharm

import os
import sys


def get_dir(argv_one):
    files = os.listdir(argv_one)
    a = ""
    b = ""
    a = [i for i in files if '.sh' in i][0]
    b = [i for i in files if '.log' in i][0]
    return a, b


def get_time(afile, bfile):
    if afile and bfile:
        atime = os.path.getmtime(afile)
        btime = os.path.getmtime(bfile)
        return atime, btime
    else:
        return False


def minus_time(atime, btime):
    interval = (atime - btime)
    interval_seconds = round(interval, 2)
    interval_minutes = round(interval_seconds / 60, 2)
    interval_hours = round(interval_minutes / 60, 2)
    print(interval, interval_minutes, interval_hours)


def main(argv_one='.'):
    a, b = get_dir(argv_one)
    atime, btime = get_time(a, b)
    minus_time(atime, btime)


if __name__ == '__main__':
    main()
