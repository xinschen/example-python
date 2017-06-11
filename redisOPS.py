#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
__author__ = 'xinschen@foxmail.com'
@note:
python3.5 操作redis
redisOPS.py
'''
import redis


class pRedis():
    """docstring for pRedis"""
    def __init__(self,dnconfig):
        self.host = dbconfig['host']
        self.port = dbconfig['port']
        self.db = dnconfig['db']
        self.password = dbconfig['password']
        self.r = redis.Redis(host = self.host, port = self.port, db = self.db,password =decry_byte(self.password) )
    #获取指定 key 的 value 值的子字符串
    def get(self,key):
        return self.r.get(key)
    #获取指定 key 的 value 值的子字符串
    def hget(self,key,id):
        return self.r.hget(key,id)
    #删除
    def remove(self, key):
        return self.r.delete(key)

