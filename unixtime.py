#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import time
from optparse import OptionParser 
import sys 
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    if len(value) >10:
        value = int(value[0:10])
    else:
        value = int(value)
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    print (dt)
 
def datetime_timestamp(dt):
     #dt为字符串
     #中间过程，一般都需要将字符串转化为时间数组
     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
     ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
     #将"2012-03-28 06:53:40"转化为时间戳
     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
     print (int(s))
 

def main():  
    p = OptionParser()  
    p.add_option('-s','--stringtime',help='请输入正常时间(2016-08-29 15:20:20)')
    p.add_option('-u','--unixtime',help='请输入unix时间() ')
    options, args = p.parse_args() 
    #print(options)
    if options.stringtime:
        datetime_timestamp(options.stringtime)
    elif options.unixtime:
        timestamp_datetime(options.unixtime)
    else:
        print('Usage: /usr/bin/python3 %s -h' %sys.argv[0])

if __name__ == '__main__':
    main()