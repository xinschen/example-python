#!/usr/bin/env  python
# -*- coding: utf-8 -*-
# author: xinschen@foxmail.com
# check app log and pid
# python2.7
import os


#定义全局变量
project_home ='/data/webservers'

#遍历目录下所有文件和目录，不进行递归
def listPath(path):
    path_dict = {}
    root = os.listdir(path)
    path_list = [ line for line in root if os.path.isdir(path+os.sep+line) ]
    file_list = [ line for line in root if os.path.isfile(path+os.sep+line) ]
    for line in path_list:
        path_dict[line] = 1
    return path_dict

# 此处为判断该project是否需要监控的project
def judgeProject(project_dict,project_name):
    project_path = project_home + os.sep +project_name
    '''  此段自定义自动发现规则'''
    return project_dict

def printJsonToZabbix(project_dict):
    #project_dict = json.load(open(json_name, 'r'))
    # 设置自动发现
    tables = []
    for key, value in project_dict.items():
        tables += [{'{#PROGRAM}': key}]
    # 返回zabbix所需data
    print json.dumps({'data': tables}, sort_keys=True, indent=7, separators=(',', ':'))


def main():
    project_dict = listPath(project_home)
    for project in project_dict.keys():
        #获取状态
        project_dict = judgeProject(project_dict,project)
    #返回data到zabbix
    printJsonToZabbix(project_dict)

if __name__ == '__main__':
    main()


