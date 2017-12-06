#!/usr/bin/env  python
# -*- coding: utf-8 -*-
# author: xinschen@foxmail.com

import sys,os
import commands
import socket

#定义程序端口参数
project_port_dict={
"project_test1"     :1234,
"project_test2"     :2345
}

    
def monitorPort(host=('127.0.0.1', 20000)):
    s = socket.socket()
    s.settimeout(3)  # timeout
    try:  # Try connection to the host
        s.connect(host)
    except Exception as e:
        print e
        return False
    return True


def monitorPID(projectname):
    cmds = ''' ps -ef|grep {projectname}|egrep -v 'log|grep|python|.py'  -c '''.format(projectname=projectname)
    return commands.getstatusoutput(cmds)


if __name__ == '__main__':
    projectname = sys.argv[1]
    ip = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read().strip()
    if projectname in project_port_dict:
        port = project_port_dict[projectname]
        host = (ip,port)
        portResult = monitorPort(host)
    else:
        portResult = True
    result = monitorPID(projectname+'.jar')
    # print portResult,type(portResult)
    if result[0] == 0 and int(result[1]) == 1 and portResult is True:
        print int(result[1])
    else:
        print 0

