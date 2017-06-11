#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@note:校验18位身份证是否符合国标
'''
import re
import sys

cardnum = str(input("请输入需要校验的身份证号码: ").strip())
cardnumlist = list(cardnum)
if len(cardnumlist)<18 or not re.findall("\d{17}",cardnum):
    print('身份证不符合规则，请确认输入内容，退出校验')
    sys.exit(0)
calclist =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
#print (calclist[1])
sum = 0
for x in range(0,17):
    #print (seq)
    #print(cardnumlist[x],calclist[x])
    result = int(cardnumlist[x]) * int(calclist[x])
    sum += result
    
result = sum % 11 
resultDict ={0:1,1:0,2:'X',3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2}
cardnum_right = cardnum[:-1] + str(resultDict.get(result))
if cardnum != cardnum_right :
    print ( "输入的身份证不符合规则!!!输入的为: %s, 正确应该为: %s" %(cardnum,cardnum_right) )
else:
    print("校验通过!!!")
