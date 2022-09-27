####################################################################################################
############################################## >前言< ##############################################
####################################################################################################
#本源码直接使用pymysql远程连接数据库进行查询，数据库允许所有人访问存在一定隐患，
#如果您有精力的话，我建议您使用mysql等数据库所在的服务器本地转发请求，
#也就是由你的转发服务器本地访问数据库（不需要开放所有人访问权限）
#然后由你的转发服务器返回数据库查询结果给你的启动器，
#这样**应该**可以避免数据库被爆破的隐患！
#############################################彩虹猫
###░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░###
'''░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░'''
'''░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░'''
'''░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░'''
'''░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░'''
'''░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░'''
'''░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░'''
'''░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░'''
'''░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░'''
'''░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░'''
'''░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░'''
'''░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░'''
'''░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░'''
###░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░###
#############################################NYAN CAT
import requests, time, os, pygame, json, pymysql, threading, urllib.request, winreg, zipfile
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tcping import Ping
from bs4 import BeautifulSoup
root = tk.Tk()
root.title('CSGO Server Launcher') #标题
root.geometry("900x600") #默认weight, height
root.resizable(False, False) #x,y均不允许拉伸
combo_var = StringVar() #tk全局变量
chebut_var = StringVar() #tk全局变量
checkin = StringVar() #tk全局变量
chebut_var.set("T") #默认播放音乐
localver = '1.1.2' #声明本地版本号
def get_server():
    textOut.delete('1.0','end') #先清空输出
    try:
        if combo_var.get() == '鸟狙魔怔①服': #以下这些代码只需要把ip和端口换成你的服务器的即可，其他的不需要改
            get = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27100&type=info') #这个查询接口是波波给我的
            pget = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27100&type=player')
        elif combo_var.get() == '鸟狙魔怔②服':
            get = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27200&type=info') #这个查询接口是波波给我的
            pget = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27200&type=player')
        elif combo_var.get() == '鸟狙魔怔③服':
            get = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27300&type=info') #这个查询接口是波波给我的
            pget = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27300&type=player')
        elif combo_var.get() == '鸟狙魔怔④服':
            get = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27400&type=info') #这个查询接口是波波给我的
            pget = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27400&type=player')
        elif combo_var.get() == '干拉魔怔服':
            get = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27500&type=info') #这个查询接口是波波给我的
            pget = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27500&type=player')
        elif combo_var.get() == '纯净魔怔服':
            get = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27600&type=info') #这个查询接口是波波给我的
            pget = requests.get('http://202.189.5.83:8998/index.php?method=xPaw&host=202.189.7.59&port=27600&type=player')
        else:
            textOut.delete('1.0','end') #先清空输出
            textOut.insert('insert', "你没有选择要服务器！\n", "color") #输出
            textOut.insert('insert', "程序&调试：ELDment\n") #输出
            textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
            textOut.insert('insert', "技术援助：波波\n") #输出
            textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
            textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
            textOut.insert('insert', "\n") #输出
            textOut.insert('insert', "2022 © ELDment") #输出        
            return
        pget.encoding = 'utf-8' #转码
        get.encoding = 'utf-8' #转码
        getjson = json.loads(get.text) #加载json
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "与查询服务器丢失连接/服务器并未开启！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出  
        tkinter.messagebox.showinfo('CSGO Server Launcher', '状态查询失败，请检测与服务器连接！', parent=root)
        return
    getp = (((str(pget.text)).replace(',{"Id"', ',\n{"Id"')).replace('[', '')).replace(']', '') #这里就强制处理了，不急吧读取json了，多行读取json气死我了
    textOut.insert('insert', "API服务器成功返回查询！\n", "color") #输出
    textOut.insert('insert', "服务器名称:\n» " + str(getjson["HostName"]) + "\n") #输出
    textOut.insert('insert', "当前地图:\n» " + getjson["Map"] + "\n") #输出
    textOut.insert('insert', "玩家数量:\n» " + str(getjson["Players"]) + "/" + str(getjson["MaxPlayers"]) + "\n") #输出
    textOut.insert('insert', "机器人:\n» " + str(getjson["Bots"]) + "\n") #输出
    textOut.insert('insert', "是否有密码:\n» " + str(getjson["Password"]) + "\n") #输出
    hgplayer = []
    if str(getjson["Players"]) != '0':
        try:
            textOut.insert('insert', ">>>>>>>>>>>>>>>O 玩家[" + str(getjson["Players"]) + "/" + str(getjson["MaxPlayers"]) + "] O<<<<<<<<<<<<<<<\n") #输出
            for pline in getp.split('\n'):
                pstring = (((pline.split('Name":"')[1]).split('","Frags')[0]).encode('utf-8')).decode("unicode_escape") #Unicode转utf-8
                if pstring != '':
                    hgplayer.append(pstring) #把所有有效名字加入数组
            iplayer = 0
            for iplayer in range(len(hgplayer)): #循环输出数组
                playernumber = iplayer + 1
                textOut.insert('insert', str(playernumber) + '» ' + hgplayer[iplayer] + '\n') #输出
                iplayer = iplayer + 1
        except:
            textOut.delete('1.0','end') #先清空输出
            tkinter.messagebox.showinfo('CSGO Server Launcher', '处理玩家信息失败！', parent=root)
            textOut.insert('insert', "处理玩家信息失败！\n", "color") #输出
            textOut.insert('insert', "程序&调试：ELDment\n") #输出
            textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
            textOut.insert('insert', "技术援助：波波\n") #输出
            textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
            textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
            textOut.insert('insert', "\n") #输出
            textOut.insert('insert', "2022 © ELDment") #输出 
            return
    
def get_server_ping():
    textOut.delete('1.0','end') #先清空输出
    ping = Ping('202.189.5.83',8998,3) #这里需要换成你的api服务器的ip和端口（也可以是你csgo服务器端服务器）
    try:
        ping.ping(2) #ping两次服务器
    except:
        textOut.delete('1.0','end') #先清空输出
        tkinter.messagebox.showinfo('CSGO Server Launcher', '与服务器丢失连接！', parent=root)
        textOut.insert('insert', "与服务器丢失连接！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        return
    textOut.insert('insert', "与服务器连接状态正常！\n", "color") #输出
    textOut.insert('insert', "程序&调试：ELDment\n") #输出
    textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
    textOut.insert('insert', "技术援助：波波\n") #输出
    textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
    textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
    textOut.insert('insert', "\n") #输出
    textOut.insert('insert', "2022 © ELDment") #输出 
    tkinter.messagebox.showinfo('CSGO Server Launcher', '与服务器连接状态正常！', parent=root)

def get_top100():
    textOut.delete('1.0','end') #先清空输出
    try:
        database = pymysql.connect(host='202.189.5.83', user='testdb', password='GWPS5XBzP3Ayi3mE', database='testdb') #连接数据库
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "连接数据库失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '获取数据库失败，请检测与服务器连接！', parent=root)
        return
    textOut.insert('insert', "现在你查询的是9月24日20时的LevelRank数据\n", "color") #输出（这句话是我给demo使用者留的，和现在在看我源码的各位无关 XDD）
    textOut.insert('insert', "（也就是说本程序链接的为Tea主服务器导出的数据，而不是真正的主服务器数据库）\n", "color") #输出
    textOut.insert('insert', "要是你想爆破我的数据库，我也不拦着你，毕竟这并不会对我/Tea社区造成什么实质伤害...\n", "color") #输出
    #这里连接我的lr数据库，你需要换成lr数据库***注意你的lr数据库需要开启全体访问
    cursor = database.cursor() #游标
    topsql = 'SELECT name, value FROM lvl_base WHERE steam != "STEAM_1:1:712580525" ORDER BY value DESC Limit 100'
    #这里我只获取名字和积分，然后剔除了玩家（芮子）并且排序后截取前十
    try:
        cursor.execute(topsql) #执行sql指令
        results = cursor.fetchall() #获取返回值
        toplist = ((((str(results).replace(", ('", "\n('")).replace("', ", "  \t\t\t\t\t\t\t\t\t ")).replace("('", "")).replace("(", "")).replace(")", "") #转处理下获取到的数据
        topnum = 1
        for line in toplist.split('\n'):
            textOut.insert('insert', str(topnum) + '» ' + line + '\n') #输出
            topnum = topnum + 1
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "数据库读取失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '获取数据库失败，请检测与服务器连接！', parent=root)
        return

def check_self():
    textOut.delete('1.0','end') #先清空输出
    try:
        regpath = r'SOFTWARE\Valve\Steam'
        reghandle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regpath, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ)) #获取注册表中自己的名字
        steamname, _type = winreg.QueryValueEx(reghandle, "LastGameNameUsed")
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "注册表读取失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '注册表读取失败！', parent=root)
        return    
    decodename = steamname.encode('ansi').decode('utf-8') #Unicode转utf-8
    try:
        database = pymysql.connect(host='202.189.5.83', user='testdb', password='GWPS5XBzP3Ayi3mE', database='testdb') #连接数据库
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "连接数据库失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '获取数据库失败，请检测与服务器连接！', parent=root)
        return
    #这里连接我的lr数据库，你需要换成lr数据库***注意你的lr数据库需要开启全体访问
    cursor = database.cursor() #游标
    lplayersql = 'SELECT * FROM lvl_base WHERE name = "' + str(decodename) + '"' #查询语句
    try:
        cursor.execute(lplayersql) #执行sql指令
        selfresults = cursor.fetchall() #获取返回值
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "服务器数据查询失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '玩家[' + decodename + ']未出现在服务器数据库中？', parent=root)
        return
    lhandel = ((((str(selfresults).replace(' ', '\n')).replace(',', '')).replace('(', '')).replace(')', '')).replace("'", '') #处理一下获取到的数据
    selfline = 0
    try:
        for sline in lhandel.split('\n'): #处理亿下获取到的数据
            if selfline == 0:
                selfsteam = str(sline)
            elif selfline == 2:
                selfvalue = str(sline)
            elif selfline == 3:
                selfrank = str(sline)
            elif selfline == 4:
                selfkills = int(sline)
            elif selfline == 5:
                selfdeaths = int(sline)
            elif selfline == 6:
                selfshoots = int(sline)
            elif selfline == 7:
                selfhits = int(sline)
            elif selfline == 8:
                selfheadshots = int(sline)
            elif selfline == 9:
                selfassists = int(sline)
            elif selfline == 10:
                selfrwin = int(sline)
            elif selfline == 11:
                selfrlose = int(sline) 
            selfline = selfline + 1
        level = float((((((int(selfvalue) * 0.005 + selfkills * 2 + selfdeaths * -2.5 + selfshoots * 0.8 + selfhits * 1.2 + selfheadshots * 1.7 + selfassists * 1.6) / int(selfrank)) / (selfrlose + selfrwin)) * 100) + (selfrwin / (selfrlose + selfrwin)) * 100) / 2)
        #没错，上面是我瞎几把写的一个大粪算法...
        if level >= 50.0 and level < 100.0:
            selflevel = 'S'
        elif level >= 40.0 and level < 50.0:
            selflevel = 'A'        
        elif level >= 30.0 and level < 40.0:
            selflevel = 'B'        
        elif level >= 20.0 and level < 30.0:
            selflevel = 'C'     
        elif level >= 10.0 and level < 20.0:
            selflevel = 'D'        
        elif level >= 0.0 and level < 10.0:
            selflevel = 'E' 
        else:
            selflevel = 'Unknow'
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "数据处理失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '数据处理失败！', parent=root)
        return
    textOut.delete('1.0','end') #先清空输出
    textOut.insert('insert', "查询成功！\n", "color") #输出
    textOut.insert('insert',  decodename + '[' + selfsteam + ']的数据:\n')
    textOut.insert('insert', '积分» ' + selfvalue + '\n')
    textOut.insert('insert', '等级» ' + selfrank + '\n')
    textOut.insert('insert', '总赢场» ' + str(selfrwin) + '\n')
    textOut.insert('insert', '总输场» ' + str(selfrlose) + '\n')    
    textOut.insert('insert', '获胜率» {:.2f}%\n'.format((selfrwin / (selfrlose + selfrwin)) * 100))
    textOut.insert('insert', '个人评级» ' + selflevel)
    
def get_ant(): #说白了这个功能就是备用的，如果真的有一天你的服务器因为不可控原因不能访问，你可以通过石墨文档等在线文档让使用者知道你所遇到的问题（避免失联）
    textOut.delete('1.0','end') #先清空输出
    try:
        req = requests.get(url="https://shimo.im/docs/L9kBMmYDEjcLybqK/read") #这里是我自己的石墨文档，你也可以换成你的石墨文档
        req.encoding = "utf-8" #转码
        html=req.text
        soup = BeautifulSoup(req.text,features="html.parser") #用parser来分析requests得到的html内容
        handle = (soup.find("div",class_="ql-editor")).text.strip() #查找全部标记名是div并且class属性是detail_head的元素
        announcement = handle.replace('\eld', '\n') #因为解析后的文本会合为一行，所以我在文档中每行末尾加上了'\eld'，然后在通过替换'\eld'实现换行
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "读取公告失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '读取公告失败！', parent=root)
        return
    textOut.insert('insert', "成功连接到公告！公告内容如下：\n", "color") #输出
    textOut.insert('insert', announcement) #输出
   
def Schedule(a,b,c):
    textOut.delete('1.0','end') #先清空输出
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    textOut.insert('insert', "正在下载服务器资源！\n", "color") #输出
    textOut.insert('insert', '下载进度» {:.2f}%'.format(per)) #输出
    if per >= 100:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "下载完成！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出
        thread = threading.Thread(target=unzip) #写一个解压线程，防止直接执行后返回母函数
        thread.start()
    
def unzip():
    textOut.delete('1.0','end') #先清空输出
    try:
        regpath = r'SOFTWARE\Valve\Steam'
        reghandle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regpath, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ)) #获取注册表中Steam路径
        steampath, _type = winreg.QueryValueEx(reghandle, "SteamPath")
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "注册表读取失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '注册表读取失败！', parent=root)
        return
    try:
        zippath = zipfile.ZipFile(steampath + '\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\Download.zip')
        zipin = zippath.namelist() #得到压缩包里所有文件
        for file in zipin:
            zippath.extract(file, steampath + '\\steamapps\\common\\Counter-Strike Global Offensive\\csgo') #解压文件到csgo目录
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "解压缩失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '解压缩失败！', parent=root)
        return
    textOut.delete('1.0','end') #先清空输出
    zippath.close() #释放内存
    textOut.insert('insert', "服务器资源下载并解压完成！\n", "color") #输出
    textOut.insert('insert', "程序&调试：ELDment\n") #输出
    textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
    textOut.insert('insert', "技术援助：波波\n") #输出
    textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
    textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
    textOut.insert('insert', "\n") #输出
    textOut.insert('insert', "2022 © ELDment") #输出
    return
    
def download_server():
    textOut.delete('1.0','end') #先清空输出
    try:
        regpath = r'SOFTWARE\Valve\Steam'
        reghandle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regpath, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ)) #获取注册表中Steam路径
        steampath, _type = winreg.QueryValueEx(reghandle, "SteamPath")
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "注册表读取失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '注册表读取失败！', parent=root)
        return
    try:
        url = 'http://202.189.5.83:8998/test.zip' #我的云端文件
        local = os.path.join(steampath + '\\steamapps\\common\\Counter-Strike Global Offensive\\csgo','Download.zip')
        urllib.request.urlretrieve(url,local,Schedule)  
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "服务器资源下载失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '下载失败！', parent=root)
        return 

def check_update():
    textOut.delete('1.0','end') #先清空输出
    try:
        getver = requests.get('http://202.189.5.83:8998/serverver.txt') #这个版本地址换成你自己的
        getver.encoding = 'utf-8' #转码
        serverver = getver.text
    except:
        textOut.delete('1.0','end') #先清空输出
        textOut.insert('insert', "云端版本查询失败！\n", "color") #输出
        textOut.insert('insert', "程序&调试：ELDment\n") #输出
        textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") #输出
        textOut.insert('insert', "技术援助：波波\n") #输出
        textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") #输出
        textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n") #输出
        textOut.insert('insert', "\n") #输出
        textOut.insert('insert', "2022 © ELDment") #输出 
        tkinter.messagebox.showinfo('CSGO Server Launcher', '查询云端版本失败，请检测与服务器连接！', parent=root)
        return
    if localver != str(serverver):
        tkinter.messagebox.showinfo('CSGO Server Launcher', '你的启动器版本已过时! 当前版本[' + localver + '] 预期版本[' + serverver + ']', parent=root)
        
def connect_server():
    if combo_var.get() == '鸟狙魔怔①服':
        os.popen('start "" "steam://rungameid/730//+connect 202.189.7.59:27100"') #ip和端口换成你自己的服务器的
    elif combo_var.get() == '鸟狙魔怔②服':
        os.popen('start "" "steam://rungameid/730//+connect 202.189.7.59:27200"') #ip和端口换成你自己的服务器的
    elif combo_var.get() == '鸟狙魔怔③服':
        os.popen('start "" "steam://rungameid/730//+connect 202.189.7.59:27300"') #ip和端口换成你自己的服务器的
    elif combo_var.get() == '鸟狙魔怔④服':
        os.popen('start "" "steam://rungameid/730//+connect 202.189.7.59:27400"') #ip和端口换成你自己的服务器的
    elif combo_var.get() == '干拉魔怔服':
        os.popen('start "" "steam://rungameid/730//+connect 202.189.7.59:27500"') #ip和端口换成你自己的服务器的
    elif combo_var.get() == '纯净魔怔服':
        os.popen('start "" "steam://rungameid/730//+connect 202.189.7.59:27600"') #ip和端口换成你自己的服务器的
    else:      
        return

def play_music():
    mscfile = 'Backmuisc.mp3' #音乐路径
    pygame.mixer.init()
    track = pygame.mixer.music.load(mscfile) #加载音乐
    pygame.mixer.music.play(-1) #循环播放音乐
    if chebut_var.get() == 'T':
        pygame.mixer.music.unpause() #继续音乐播放
    else:
        pygame.mixer.music.pause() #停止音乐播放
        
def shitgui(): #这里面这一大坨都是UI，就不一一注释了
    scrollText = Scrollbar(frmLT, width = 305)
    scrollText.grid(row = 0,column = 0, sticky = SE + NE)
    textOut['yscrollcommand'] = scrollText.set
    scrollText['command'] = textOut.yview
    textOut.tag_config("color", backgroun="yellow", foreground="red")
    servers = ['请选择服务器', '鸟狙魔怔①服', '鸟狙魔怔②服', '鸟狙魔怔③服', '鸟狙魔怔④服', '干拉魔怔服', '纯净魔怔服']
    comboboxServer = ttk.Combobox(frmLC, values=servers, textvariable=combo_var, state="readonly")
    comboboxServer.grid(row = 0, column = 0)
    comboboxServer.current(0)
    textOut.bind("<Key>", lambda a: "break")
    textOut.insert('insert', "程序运行中...[此程序只是个测试程序，并不是Tea社官方启动器！]\n", "color")  
    textOut.insert('insert', "程序&调试：ELDment\n") 
    textOut.insert('insert', "赞助：茶糜(Tea社服主)\n") 
    textOut.insert('insert', "技术援助：波波\n")
    textOut.insert('insert', "本源码仅发布在Github平台,\n其他平台均为盗版！\n") 
    textOut.insert('insert', "本项目完全开源！请谨防倒卖狗！\n")
    textOut.insert('insert', "\n")
    textOut.insert('insert', "2022 © ELDment")
    btnServer = Button(frmLC, text='查询服务器状态', width = 15, bg = 'white', command = trmgetserver)
    btnServer.grid(row = 0, column = 1)
    btnConnect = Button(frmLC, text='加入选中服务器', width = 15, bg = 'white', command = connect_server)
    btnConnect.grid(row=1, column=1, sticky=E, padx = 10, pady = 5)
    btnTop = Button(frmLC, text='查询积分Top100', width = 15, bg = 'white', command = trtop100)
    btnTop.grid(row=0, column=2, sticky=E, padx = 10, pady = 5)
    btnPing = Button(frmLC, text='检测与服务器连接', width = 15, bg = 'white', command = trping)
    btnPing.grid(row=1, column=2, sticky=E, padx = 10, pady = 5)
    cbnMusic = Checkbutton(frmLC, text="播放背景音乐", bg = 'white', variable = chebut_var, onvalue = "T", offvalue="F", command = play_music)
    cbnMusic.grid(row=0, column=3, sticky=E, padx = 10, pady = 5)
    btnCheckPlayer = Button(frmLC, text='查询自己', width = 15, bg = 'white', command = trcheckself)
    btnCheckPlayer.grid(row=1, column=3, sticky=E, padx = 10, pady = 5)
    btnDown = Button(frmLC, text='下载服务器资源', width = 15, bg = 'white', command = trdown)
    btnDown.grid(row=2, column=3, sticky=E, padx = 10, pady = 5)
    btnAnt = Button(frmLC, text='查看公告', width = 15, bg = 'white', command = trant)
    btnAnt.grid(row=3, column=3, sticky=E, padx = 10, pady = 5)
    imgInfo = PhotoImage(file = "Background.png")
    lblImage = Label(frmRT, image = imgInfo)
    lblImage.image = imgInfo
    lblImage.grid()
    root.protocol('WM_DELETE_WINDOW', exit)
    root.iconbitmap('Kequeen.ico')
    root.mainloop()

def exit():
    os._exit(0) #结束

def trping(): #写多线程防止卡死
    thread = threading.Thread(target=get_server_ping)
    thread.start()
    
def trmusic(): #写多线程防止卡死
    thread = threading.Thread(target=play_music)
    thread.start()

def trtop100(): #写多线程防止卡死
    thread = threading.Thread(target=get_top100)
    thread.start()

def trcheckself(): #写多线程防止卡死
    thread = threading.Thread(target=check_self)
    thread.start()

def trmgetserver(): #写多线程防止卡死
    thread = threading.Thread(target=get_server)
    thread.start()
    
def trmusic(): #写多线程防止卡死
    thread = threading.Thread(target=play_music)
    thread.start()

def trant(): #写多线程防止卡死
    thread = threading.Thread(target=get_ant)
    thread.start()
    
def trdown(): #写多线程防止卡死
    thread = threading.Thread(target=download_server)
    thread.start()
    
if __name__ == '__main__':
    frmLT = Frame(width = 600, height = 345, bg = 'white')
    frmRT = Frame(width = 300, height = 600)
    frmLC = Frame(width = 600, height = 245, bg = 'white')
    frmLT.grid(row = 0, column = 0, padx = 0,pady = 1)
    frmRT.grid(row = 0, column = 1, rowspan = 3,padx = 0,pady = 1)
    frmLC.grid(row = 1, column = 0, padx = 0,pady = 1)
    frmLT.grid_propagate(0)
    frmRT.grid_propagate(0)
    frmLC.grid_propagate(0)
    textOut = Text(frmLT, width = 600) 
    textOut.grid(row=0, column = 0, sticky = NE + NW)
    check_update()
    trmusic()
    shitgui()
