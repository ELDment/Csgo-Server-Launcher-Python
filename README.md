# CSGO服务器启动器
**前言：**<br />
**我花了大约12个小时来写这个很烂的项目**<br />
**这个项目还有很多不足之处，所以源码仅供参考**<br />
**感谢茶糜的赞助以及波波的帮助（波波的接口真的很实用！）**<br />
**请您耐心读完本Readme，如未解决请发起Issue或者加我QQ（文章末尾处）！**<br />
## 现有功能
**本项目虽已经有了许多功能，但是相对来说本项目还不够成熟，所以本项目强烈欢迎二改！**<br />
**目前已有功能：**<br />
**1.新版本检测**<br />
**2.服务器离线公告**<br />
**3.查询服务器状态以及在线玩家**<br />
**4.加入游戏**<br />
**5.检测与服务器链接**<br />
**6.查询LevelRank数据库前100名玩家**<br />
**7.查询自己的LevelRank数据**<br />
**8.下载服务器资源**<br />
**9.多线程**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Server%26Player.png)<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Top100.png)<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Self.png)<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Ant.png)<br />
## 准备工作
**0.下载Background.png、Backmuisc.mp3、Kequeen.ico以及Launcher.py**<br />

**1.制作在线文档（我这里使用的是石墨文档）**<br />
**一定不要忘记分享文档！！！**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/ShiMoShare.png)<br />
**然后在石墨文档中编写你的公告（每行末尾需加上\eld否则会出现 读取公告时全部混成一行的现象）**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/ShiMo.png)<br />
**当然你也可以在每行末尾加上自定义换行表示而不是'\eld'，你只需要修改②即可**<br />
**①处需替换成你自己的在线文档地址**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Code.png)<br />

**2.制作云端版本**<br />
**在你的web目录下放置一个txt里面写入版本信息**<br />
**并在源码中替换成它的地址**<br />
**访问时预期效果：**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Serverver.txt.png)<br />

**3.制作服务器下载资源**<br />
**制作一个压缩包，将maps,models,sounds等文件夹压缩至其中（注意必须压缩成zip格式），然后将安装包像server.txt一样放置在web目录下**<br />
**并在源码中替换成它的地址**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Download.png)<br />
**zip结构如下**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/ZIPIN.png)<br />
**访问时预期效果：**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/DownloadZip.png)<br />

**4.修改数据库连接**<br />
**将下图圈红的地方换成你自己的数据库（数据库需允许所有人访问）**<br />
**其实我这个方法不是很好，开启所有人访问存在一定的安全隐患！**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Mysql1.png)<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Mysql2.png)<br />

**5.修改IP及端口**<br />
**将下图圈红的地方换成你服务器ip以及端口**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/GetServer.png)<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/Connect.png)<br />
## 报错解决
**如出现以下报错，说明缺少背景文件【你可以自己制作一个名为Background.png的图像文件，最佳分辨率为300*600】**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/EB.png)<br />
**如出现以下报错，说明缺少图标文件【你可以自己制作一个名为Kequeen.ico的图标文件，最佳分辨率为128*128】**<br />
![image](https://github.com/ELDment/Csgo-Server-Launcher-Python/blob/main/ScreenShot/EI.png)<br />
**如缺少音乐文件，不会报错，但是gui打开后无法播放音乐**<br />
## 问题反馈&交流
**请不要加我的QQ大号了！！！真的看不过来！！！**<br />
**新号：3612903372**<br />
**或者您可以直接在Issue中提问！**
