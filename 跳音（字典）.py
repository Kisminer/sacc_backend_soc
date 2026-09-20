print('欢迎来到跳音流量观察台')
print('当前身份：后端组SOC实习生')
print('负责人：菲比啾比')
operate={1:'添加一条内容数据',
        2:'查看所有内容数据',
        3:'计算并展示流量等级',
        4:'搜索制定标题或作者',
        0:'退出系统'}
num=2                    #记录视频编号
input('继续请按回车')      #顿一下，别一下闪出来
load=True    #是否处于登录状态
msg={1:{'name':'三分钟看懂后端',    #初始数据
        'author':'xiao_ming',
        'platform':'top_tip',
        'play_count':12000,
        'like':800,
        'comment':120,
        'tip':['后端','学习','新人']}
     ,2:{'name':'后端练习',
         'author':'xiao_ming',
         'platform':'top_tip',
         'play_count':1200,
         'like':800,
         'comment':120,
         'tip':[]}}

def inter(i):                          #i是提示语
    """
    定义一个函数防止自然数据，如播放量、点赞量为负数
    """
    n=input(i)
    try:
        n=int(n)
        if n<0:
            print('闹鬼了，吓死菲比啾比了')#报错
            n=inter(i)                   #用递归直到数据正常
        else:
            return n
    except ValueError:
        print('输入数字，哥们儿：')
        n=inter(i)

while load:                             #登录成功，所有代码建立在此基础上
    for key,value in operate.items():  #遍历字典
        print(f'{key}:{value}')
    ope=inter('请输入你要进行的操作:')
    if ope==0:      #退出登录
        load=False  #更改登录状态，结束当前if的同时，使得while也结束
    elif ope==1:  #添加数据
        num+=1
        msg[num] = {}  # 在字典里建新字典
        msg[num]['name'] = input('新视频名称') .strip() # 然后狸猫换太子
        msg[num]['author'] = input('作者名称').strip()
        msg[num]['platform'] = input('平台').strip()
        msg[num]['play_count'] =inter('播放量')
        msg[num]['like'] =inter('点赞数')
        msg[num]['tip']=[]
        def add_tips():
            new_tip=input('新建标签(为空则结束)：').strip()
            new_tip=new_tip.strip()
            while new_tip!='':
                msg[num]['tip'].append(new_tip)
        add_tips()
    elif ope==2:
        if msg!={}:#数据非空
            for outer_key,inner_dict in msg.items():#先把外层编号打出来
                print(f"视频编号{outer_key}")
                for inner_key, inner_value in inner_dict.items():#再进入内层把数据带出来
                    print(f"____{inner_key}: {inner_value}")#来几格缩进看的明白
        else:
            print('菲比啾比没这玩意，不鸡道你要啥')#报错
    elif ope==3:                               #因为设计上界问题，所以不用自定义的inter
        numbe=inter('视频编号：')
        if numbe>num:                          #下面两个是防joker
                print('菲比啾比没这玩意，不鸡道你要啥')
        else:                                  #正片开始
            p=msg[numbe]['play_count']
            l=msg[numbe]['like']
            c=msg[numbe]['comment']
            print('流量分数为：',p*2+l/2+c*3)
            if msg[numbe]['play_count'] <= 999:
                    print('无人问津')
            elif 1000 <= msg[numbe]['play_count']<= 9999:
                print('有点水花')
            elif 9999 < msg[numbe]['play_count']<= 49999:
                print('小爆一下')
            elif 49999 < msg[numbe]['play_count']<= 199999:
                print('大爆预备')
            else:
                print('爆款候选')
    elif ope==4:
        key_word=input('搜索').strip()
        for i in range(1,num):
            if key_word in msg[i]['name']:
                print(msg[i]['name']+'————'+msg[i]['auther'])
            elif key_word in msg[i]['author']:
                print(msg[i]['name']+'————'+msg[i]['auther'])
            else:
                print('抱歉，没有相关内容')
    else:
        print("菲比啾比不知道你要干什么")
print('感谢使用')
