#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
u'''在python3下通过
'''


def useStyle(string, mode = '', fore = '', back = ''):
    u'''
    终端输出展出，包括字体颜色，背景色，显示模式
    '''
    #颜色参数
    STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },
        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },
        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },

        'default' :
        {
            'end' : 0,
        },
    }
    #设置颜色展示
    mode  = '%s' % STYLE['mode'][mode] if mode in STYLE['mode'] else ''
    fore  = '%s' % STYLE['fore'][fore] if fore in STYLE['fore'] else ''
    back  = '%s' % STYLE['back'][back] if back in STYLE['back'] else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end   = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)



#中英文混合格式化输出对齐--
def alignment(str1, space=25, align = 'left'):
    u'''  中英文混合格式化输出对齐 '''
    str1 =str(str1)
    if True:
        length = len(str1.encode('gb18030'))
        space = space - length if space >=length else 0
        if align == 'left':
            str1 = str1 + ' ' * space
        elif align == 'right':
            str1 = ' '* space +str1
        elif align == 'center':
            str1 = ' ' * (space //2) +str1 + ' '* (space - space // 2)
        return str1.encode('UTF8').decode('UTF8')
    else:
        pass

def formatPrint(title,result):
    u''' 只针对sql取数，计算输出长度，终端管理'''
    sting = '%-20s '
    f_sting = sting * len(title)
    #print(f_sting %tuple(title))
    #输出标题栏
    count = 0
    length = len(title)
    print(useStyle('结果如下，请确认！！',fore='yellow',mode='bold'))
    for x in range(0,length):
        #print(alignment(title[x]),end='')
        print(useStyle(alignment(title[x]),mode='bold',fore='green'),end='')
    for line in result:
        print('')
        for x in range(0,length):
            #print(alignment(line[x]),end='')
            #输出结果
            print(useStyle(alignment(line[x]),mode='bold',fore='yellow'),end='')
        count +=1
        if count > 30:
            print(' ')
            yes_or_not = str(input("数据量过多,只展示30条数据,仍需展示剩余部分(eg:yes): ").strip())
            if yes_or_not in ('y','yes'):
                count = 0
                continue
            else:
                break

