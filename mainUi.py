#! /usr/bin/env python
# -*- coding:utf-8 -*-
#====#====#====#====
# __author__ = "renys"
#weixin:ysongren
#QQ:774113517
#FileName: *.py
#Version:1.0.0
#====#====#====#====

# -*- coding:utf-8 -*-
import logging
import threading
import time
import traceback

import wx

from configInfo import ConfigInfo
from run import Run
from webfornum.webForumMain import WebForumMain


class Frame(wx.Frame):
    test = False
    run = None
    webForum = None

    def __init__(self):
        wx.Frame.__init__(self, None, title='零跑汽车金融|论坛平台截图', size=(829, 610),name='frame',style=541072960)
        self.lipaoCar = wx.Panel(self)
        self.Centre()
        self.appTag = wx.StaticText(self.lipaoCar, size=(80, 24), pos=(154, 1), label='金融平台', name='staticText', style=2321)
        appTag_字体 = wx.Font(11, 74, 90, 700, False, 'Microsoft YaHei UI', 28)
        self.appTag.SetFont(appTag_字体)
        self.cropAppLable = wx.StaticText(self.lipaoCar,size=(75, 24),pos=(6, 75),label='平台选择:',name='staticText',style=529)
        self.tonghuashunCheckbox = wx.CheckBox(self.lipaoCar,size=(80, 24),pos=(96, 18),name='check',label='同花顺',style=16384)
        self.tonghuashunCheckbox.Set3StateValue(1)
        self.futuniuniuCheckbox = wx.CheckBox(self.lipaoCar,size=(80, 24),pos=(96, 46),name='check',label='富途牛牛',style=16384)
        self.futuniuniuCheckbox.Set3StateValue(1)
        self.dazhihuiCheckbox = wx.CheckBox(self.lipaoCar,size=(80, 24),pos=(96, 71),name='check',label='大智慧',style=16384)
        self.dazhihuiCheckbox.Set3StateValue(1)
        self.dongfangcaifuCheckbox = wx.CheckBox(self.lipaoCar,size=(80, 24),pos=(96, 99),name='check',label='东方财富',style=16384)
        self.dongfangcaifuCheckbox.Set3StateValue(1)
        self.futuniuniuPcCheckbox = wx.CheckBox(self.lipaoCar,size=(80, 24),pos=(96, 126),name='check',label='富途牛牛PC',style=16384)
        self.futuniuniuPcCheckbox.Set3StateValue(1)
        self.tonhuashunPageLable = wx.StaticText(self.lipaoCar,size=(80, 24),pos=(239, 20),label='截图页面数：',name='staticText',style=17)
        self.futuniuniuPageLabel = wx.StaticText(self.lipaoCar,size=(80, 24),pos=(239, 48),label='截图页面数：',name='staticText',style=17)
        self.dazhihuiPageLable = wx.StaticText(self.lipaoCar,size=(73, 24),pos=(239, 73),label='截图页面数：',name='staticText',style=17)
        self.dongfangcaifuPageLabel = wx.StaticText(self.lipaoCar,size=(80, 24),pos=(239, 101),label='截图页面数：',name='staticText',style=17)
        self.futuniuniuPcPageLabel = wx.StaticText(self.lipaoCar,size=(80, 24),pos=(240, 128),label='截图页面数：',name='staticText',style=17)
        self.tonghuashunPages = wx.SpinCtrl(self.lipaoCar,size=(38, 24),pos=(310, 16),name='wxSpinCtrl',min=20,max=40,initial=30,style=0)
        self.tonghuashunPages.SetBase(10)
        self.futuniuniuPages = wx.SpinCtrl(self.lipaoCar,size=(38, 24),pos=(310, 43),name='wxSpinCtrl',min=10,max=20,initial=16,style=0)
        self.futuniuniuPages.SetBase(10)
        self.dazhihuiPages = wx.SpinCtrl(self.lipaoCar,size=(38, 24),pos=(311, 70),name='wxSpinCtrl',min=8,max=20,initial=12,style=0)
        self.dazhihuiPages.SetBase(10)
        self.dongfangcaifuPages = wx.SpinCtrl(self.lipaoCar,size=(38, 24),pos=(310, 97),name='wxSpinCtrl',min=20,max=40,initial=30,style=0)
        self.dongfangcaifuPages.SetBase(10)
        self.futuniuniuPcPages = wx.SpinCtrl(self.lipaoCar,size=(38, 24),pos=(310, 124),name='wxSpinCtrl',min=4,max=8,initial=5,style=0)
        self.futuniuniuPcPages.SetBase(10)
        posY = 154
        self.timesLabel = wx.StaticText(self.lipaoCar, size=(75, 24), pos=(6, posY), label='截图时间:', name='staticText', style=529)
        self.times = wx.TextCtrl(self.lipaoCar, size=(280, 22), pos=(96, posY - 3), value='9:30-10:00-11:00-12:00-13:00-14:00', name='text', style=0)
        for line in range(13):
            self.vertical_line = wx.StaticText(self.lipaoCar, size=(4, 14), pos=(411, line * 14 - 2), label='|', name='staticText', style=17)
        self.webFormunTag = wx.StaticText(self.lipaoCar, size=(80, 24), pos=(556, 1), label='论坛', name='staticText', style=2321)
        webFormunTag_字体 = wx.Font(11, 74, 90, 700, False, 'Microsoft YaHei UI', 28)
        self.webFormunTag.SetFont(webFormunTag_字体)
        self.qichezhijia_C01 = wx.CheckBox(self.lipaoCar, size=(36, 24), pos=(466, 44), name='check', label='C01', style=16384)
        self.qichezhijia_C01.SetValue(True)
        self.qichezhijia_C11 = wx.CheckBox(self.lipaoCar, size=(80, 24), pos=(466, 69), name='check', label='C11', style=16384)
        self.qichezhijia_C11.SetValue(True)
        self.qichezhijia_T03 = wx.CheckBox(self.lipaoCar, size=(37, 24), pos=(466, 93), name='check', label='T03', style=16384)
        self.qichezhijia_T03.SetValue(True)
        self.dongchedi_C01 = wx.CheckBox(self.lipaoCar, size=(40, 24), pos=(557, 45), name='check', label='C01', style=16384)
        self.dongchedi_C01.SetValue(True)
        self.dongchedi_C11 = wx.CheckBox(self.lipaoCar, size=(42, 24), pos=(557, 69), name='check', label='C11', style=16384)
        self.dongchedi_C11.SetValue(True)
        self.dongchedi_T03 = wx.CheckBox(self.lipaoCar, size=(44, 24), pos=(557, 93), name='check', label='T03', style=16384)
        self.dongchedi_T03.SetValue(True)
        self.qichezhijiaTag = wx.StaticText(self.lipaoCar, size=(58, 14), pos=(466, 24), label='汽车之家', name='staticText', style=17)
        self.dongchediTag = wx.StaticText(self.lipaoCar, size=(42, 14), pos=(557, 24), label='懂车帝', name='staticText', style=17)
        self.xinchuxingTag = wx.StaticText(self.lipaoCar, size=(43, 14), pos=(656, 24), label='新出行', name='staticText', style=17)
        self.xinchuxing_xinchuxing = wx.CheckBox(self.lipaoCar, size=(60, 24), pos=(657, 54), name='check', label='新出行', style=16384)
        self.xinchuxing_xinchuxing.SetValue(True)
        posY = 138
        self.webForumnTimeTag = wx.StaticText(self.lipaoCar, size=(60, 14), pos=(448, posY), label='截图时间：', name='staticText', style=529)
        self.startHour = wx.SpinCtrl(self.lipaoCar, size=(40, 24), pos=(511, posY - 3), name='wxSpinCtrl', min=8, max=17, initial=8, style=0)
        self.startHour.SetBase(10)
        self.toLine = wx.StaticText(self.lipaoCar, size=(10, 10), pos=(551, posY), label='-', name='staticText', style=2321)
        self.endHour = wx.SpinCtrl(self.lipaoCar, size=(40, 24), pos=(563, posY - 4), name='wxSpinCtrl', min=11, max=23, initial=21, style=0)
        self.endHour.SetBase(10)
        self.minuteTag = wx.StaticText(self.lipaoCar, size=(38, 14), pos=(692, posY), label='分/时', name='staticText', style=2321)
        self.minute = wx.SpinCtrl(self.lipaoCar, size=(40, 24), pos=(655, posY - 4), name='wxSpinCtrl', min=0, max=59, initial=10, style=0)
        self.minute.SetBase(10)
        self.hourTag = wx.StaticText(self.lipaoCar, size=(30, 14), pos=(602, posY), label='小时', name='staticText', style=2321)
        posY = 154
        line = '-'
        for i in range(270):
            line += '-'
        self.horizontal_lin = wx.StaticText(self.lipaoCar, size=(820, 10), pos=(0, posY + 18), label = line, name='staticText', style=2321)
        horizontal_lin_字体 = wx.Font(5, 74, 90, 300, False, 'Microsoft YaHei UI Light', 28)
        self.horizontal_lin.SetFont(horizontal_lin_字体)
        self.unamePswd = wx.StaticText(self.lipaoCar,size=(75, 24),pos=(7, 182),label='用户名-密码:',name='staticText',style=529)
        self.uname = wx.TextCtrl(self.lipaoCar,size=(80, 22),pos=(96, 179),value='123456789',name='text',style=0)
        self.gap = wx.StaticText(self.lipaoCar,size=(10, 24),pos=(181, 179),label='-',name='staticText',style=2321)
        self.pswd = wx.TextCtrl(self.lipaoCar,size=(80, 22),pos=(196, 179),value='123456789',name='text',style=0)
        self.savePathLabel = wx.StaticText(self.lipaoCar,size=(75, 24),pos=(6, 209),label='文件保存路径:',name='staticText',style=529)
        self.savePath = wx.TextCtrl(self.lipaoCar,size=(249, 22),pos=(96, 206),value='',name='text',style=0)
        self.btnSelectFold = wx.Button(self.lipaoCar,size=(80, 32),pos=(347, 199),label='选择文件夹',name='button')
        self.btnSelectFold.Bind(wx.EVT_BUTTON,self.btnSelectFold_click)
        posY = 182
        self.everyDayLabel = wx.StaticText(self.lipaoCar,size=(60, 24),pos=(441, posY),label='每天截图:',name='staticText',style=529)
        self.everyDayCropCheckbox = wx.CheckBox(self.lipaoCar,size=(16, 14),pos=(518, posY),name='check',label='',style=12288)
        self.everyDayCropCheckbox.Set3StateValue(1)  #posY = 194
        self.modulTag = wx.StaticText(self.lipaoCar, size=(60, 14), pos=(441, posY + 28), label='启动模块:', name='staticText', style=529)
        self.appCheckbox = wx.CheckBox(self.lipaoCar, size=(64, 13), pos=(519, posY + 31), name='check', label='金融平台', style=16384)
        self.appCheckbox.SetValue(False)
        self.webForumCheckbox = wx.CheckBox(self.lipaoCar, size=(60, 13), pos=(622, posY + 30), name='check', label='论坛', style=16384)
        self.webForumCheckbox.SetValue(True)
        line = '-'
        for i in range(84):
            line += '-'
        self.rectLineTop = wx.StaticText(self.lipaoCar,size=(100, 13),pos=(114, 228),label=line,name='staticText',style=2304)
        rectLineTop_字体 = wx.Font(8,74,90,400,False,'Microsoft YaHei UI',28)
        self.rectLineTop.SetFont(rectLineTop_字体)
        self.rectLineBottom = wx.StaticText(self.lipaoCar,size=(420, 10),pos=(113, 310),label=line,name='staticText',style=2304)
        for i in range(6):
            offY = i * 14 + 234
            self.rectLineLeft1 = wx.StaticText(self.lipaoCar,size=(4, 14),pos=(111, offY),label='|',name='staticText',style=17)
            self.rectLineRight1 = wx.StaticText(self.lipaoCar,size=(4, 14),pos=(534, offY),label='|',name='staticText',style=0)
        self.btnSaveInfo = wx.Button(self.lipaoCar,size=(80, 32),pos=(15, 259),label='全部 报存',name='button')
        self.btnSaveInfo.Bind(wx.EVT_BUTTON,self.btnSaveInfo_click)
        self.btnHandlerCrop = wx.Button(self.lipaoCar,size=(80, 32),pos=(132, 259),label='手动截图',name='button')
        self.btnHandlerCrop.Bind(wx.EVT_BUTTON,self.btnHandlerCrop_click)
        self.btnAutoCrop = wx.Button(self.lipaoCar,size=(86, 32),pos=(241, 241),label='启动自动截图',name='button')
        self.btnAutoCrop.Bind(wx.EVT_BUTTON,self.btnAutoCrop_click)
        self.btnPauseCrop = wx.Button(self.lipaoCar,size=(86, 32),pos=(242, 276),label='暂停自动截图',name='button')
        self.btnPauseCrop.Bind(wx.EVT_BUTTON,self.btnPauseCrop_click)
        self.btnTips = wx.StaticText(self.lipaoCar,size=(171, 24),pos=(342, 266),label='(手动和自动模式只能选择一种)',name='staticText',style=2321)
        self.btnTips.SetForegroundColour((255, 0, 0, 255))
        self.printBox = wx.TextCtrl(self.lipaoCar,size=(803, 240),pos=(5, 330),value='',name='text',style=wx.TE_MULTILINE | wx.CB_READONLY)
        self.msgLabelApp = wx.StaticText(self.lipaoCar,size=(251, 27),pos=(553, 243),label='13:30 时间段，App截图结束！',name='staticText',style=17)
        self.msgLabelApp.SetForegroundColour((77, 144, 254, 155))
        self.msgLabelApp.SetFont(wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28))
        self.msgLabelForum = wx.StaticText(self.lipaoCar,size=(247, 21),pos=(554, 279),label='13:10 时间段，论坛截图结束！',name='staticText',style=17)
        msgLabelForum_字体 = wx.Font(11,74,90,400,False,'Microsoft YaHei UI',28)
        self.msgLabelForum.SetFont(msgLabelForum_字体)
        self.msgLabelForum.SetForegroundColour((0, 128, 192, 255))
        self.msgLabelApp.SetLabel('')
        self.msgLabelForum.SetLabel('')
        self.initData()

    def initData(self):
        configInfo =  ConfigInfo()
        self.configInfo = configInfo
        self.configInfo.parseConfigFile()
        self.savePath.SetValue(configInfo.savePath)
        self.times.SetValue(configInfo.times)
        self.uname.SetValue(configInfo.uname)
        self.pswd.SetValue(configInfo.pswd)
        self.dongfangcaifuCheckbox.SetValue(self.convertBoolCheckbox(configInfo.dongfangcaifuCheckbox))
        self.dazhihuiCheckbox.SetValue(self.convertBoolCheckbox(configInfo.dazhihuiCheckbox))
        self.tonghuashunCheckbox.SetValue(self.convertBoolCheckbox(configInfo.tonghuashunCheckbox))
        self.futuniuniuCheckbox.SetValue(self.convertBoolCheckbox(configInfo.futuniuniuCheckbox))
        self.futuniuniuPcCheckbox.SetValue(self.convertBoolCheckbox(configInfo.futuniuniuPcCheckbox))
        self.everyDayCropCheckbox.SetValue(self.convertBoolCheckbox(configInfo.everyDayCropCheckbox))
        self.qichezhijia_C01.SetValue(self.convertBoolCheckbox(configInfo.qichezhijia_C01))
        self.qichezhijia_C11.SetValue(self.convertBoolCheckbox(configInfo.qichezhijia_C11))
        self.qichezhijia_T03.SetValue(self.convertBoolCheckbox(configInfo.qichezhijia_T03))
        self.dongchedi_C01.SetValue(self.convertBoolCheckbox(configInfo.dongchedi_C01))
        self.dongchedi_C11.SetValue(self.convertBoolCheckbox(configInfo.dongchedi_C11))
        self.dongchedi_T03.SetValue(self.convertBoolCheckbox(configInfo.dongchedi_T03))
        self.xinchuxing_xinchuxing.SetValue(self.convertBoolCheckbox(configInfo.xinchuxing_xinchuxing))
        self.appCheckbox.SetValue(self.convertBoolCheckbox(configInfo.appModul))
        self.webForumCheckbox.SetValue(self.convertBoolCheckbox(configInfo.webForumModul))
        self.dongfangcaifuPages.SetValue(configInfo.dongfangcaifuPage)
        self.tonghuashunPages.SetValue(configInfo.tonghuashunPage)
        self.dazhihuiPages.SetValue(configInfo.dazhihuiPage)
        self.futuniuniuPages.SetValue(configInfo.futuniuniuMobPage)
        self.futuniuniuPcPages.SetValue(configInfo.futuniuniuPcPage)
        self.startHour.SetValue(configInfo.startHour)
        self.endHour.SetValue(configInfo.endHour)
        self.minute.SetValue(configInfo.minute)

    def clearLog(self):
        self.printBox.SetValue('')

    def printLog(self, msg):
        self.printBox.AppendText(msg + '\n')

    def getActionTag(self):
        return [
            self.everyDayCropCheckbox, self.tonghuashunCheckbox, self.futuniuniuCheckbox, self.futuniuniuPcCheckbox,
            self.dazhihuiCheckbox, self.dongfangcaifuCheckbox,
            self.qichezhijia_C01, self.qichezhijia_C11, self.qichezhijia_T03, self.dongchedi_C01, self.dongchedi_C11,
            self.dongchedi_T03, self.xinchuxing_xinchuxing, self.appCheckbox, self.webForumCheckbox,
            self.dongfangcaifuPages, self.tonghuashunPages, self.futuniuniuPages, self.futuniuniuPcPages,
            self.dazhihuiPages, self.startHour, self.endHour, self.minute,
            self.times, self.uname, self.pswd, self.savePath,
            self.btnSaveInfo, self.btnSelectFold, self.btnAutoCrop, self.btnHandlerCrop,
        ]

    def enable(self):
        tags = self.getActionTag()
        for t in tags:
            t.Enable(True)

    def forbit(self):
        tags = self.getActionTag()
        for t in tags:
            t.Disable()

    def setMinDefaultValueForPages(self, pageSpinCtrl, defaultV, minV):
        pageSpinCtrl.SetMin(minV)
        pageSpinCtrl.SetValue(defaultV)

    def convertBoolCheckbox(self, v):
        return v == '1'

    def convertIntCheckbox(self, v):
        return 1 if v == True else 0


    def fragmentTimesFinish(self, times, allFinish = False):
        self.msgLabelApp.SetLabel(f'时间段:{times}，App截图结束！')
        if allFinish == True and self.auto == False:
            self.enable()

    def fragmentForumTimesFinish(self, times):
        self.msgLabelForum.SetLabel(f'时间段:{times}，论坛截图结束！')

    def btnSelectFold_click(self, event):
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR, message="保存文件夹")
        if folder.ShowModal() == wx.ID_OK:
            folder_path = folder.GetPath()
        folder.Destroy()
        self.savePath.SetLabel(folder_path)

    def btnSaveInfo_click(self,event):
        valid = self.validateForm()
        if valid == False:
            return
        self.doConfigInfo(True)

    def doConfigInfo(self, isSave):
        self.printLog('加载配置信息')
        savePath = self.savePath.GetValue()
        times = self.times.GetValue()
        uname = self.uname.GetValue()
        pswd = self.pswd.GetValue()
        dongfangcaifuCheckbox = self.convertIntCheckbox(self.dongfangcaifuCheckbox.GetValue())
        dazhihuiCheckbox = self.convertIntCheckbox(self.dazhihuiCheckbox.GetValue())
        tonghuashunCheckbox = self.convertIntCheckbox(self.tonghuashunCheckbox.GetValue())
        futuniuniuCheckbox = self.convertIntCheckbox(self.futuniuniuCheckbox.GetValue())
        futuniuniuPcCheckbox = self.convertIntCheckbox(self.futuniuniuPcCheckbox.GetValue())
        everyDayCropCheckbox = self.convertIntCheckbox(self.everyDayCropCheckbox.GetValue())
        qichezhijia_C01Checkbox = self.convertIntCheckbox(self.qichezhijia_C01.GetValue())
        qichezhijia_C11Checkbox = self.convertIntCheckbox(self.qichezhijia_C11.GetValue())
        qichezhijia_T03Checkbox = self.convertIntCheckbox(self.qichezhijia_T03.GetValue())
        dongchedi_C01Checkbox = self.convertIntCheckbox(self.dongchedi_C01.GetValue())
        dongchedi_C11Checkbox = self.convertIntCheckbox(self.dongchedi_C11.GetValue())
        dongchedi_T03Checkbox = self.convertIntCheckbox(self.dongchedi_T03.GetValue())
        xinchuxing_xinchuxingCheckbox = self.convertIntCheckbox(self.xinchuxing_xinchuxing.GetValue())
        appCheckbox = self.convertIntCheckbox(self.appCheckbox.GetValue())
        webForumCheckbox = self.convertIntCheckbox(self.webForumCheckbox.GetValue())
        dongfangcaifuPage = self.dongfangcaifuPages.GetValue()
        tonghuashunPage = self.tonghuashunPages.GetValue()
        dazhihuiPage = self.dazhihuiPages.GetValue()
        futuniuniuMobPage = self.futuniuniuPages.GetValue()
        futuniuniuPcPage = self.futuniuniuPcPages.GetValue()
        startHour = self.startHour.GetValue()
        endHour = self.endHour.GetValue()
        minute = self.minute.GetValue()
        self.configInfo.init(savePath,times,uname,pswd,dongfangcaifuCheckbox,dazhihuiCheckbox,tonghuashunCheckbox,
                        futuniuniuCheckbox,futuniuniuPcCheckbox,everyDayCropCheckbox,dongfangcaifuPage,tonghuashunPage,
                        dazhihuiPage,futuniuniuMobPage,futuniuniuPcPage)
        self.configInfo.initWebForum(qichezhijia_C01Checkbox, qichezhijia_C11Checkbox, qichezhijia_T03Checkbox,
                                     dongchedi_C01Checkbox, dongchedi_C11Checkbox, dongchedi_T03Checkbox,
                                     xinchuxing_xinchuxingCheckbox, startHour, endHour, minute)
        self.configInfo.initModul(appCheckbox, webForumCheckbox)
        self.configInfo.toStr()
        if isSave == True:
            self.printLog('保存配置信息')
            self.configInfo.save()

    def start(self, auto):
        self.auto = auto
        self.clearLog()
        self.printLog('开始 {}截图'.format('手动' if auto == False  else '自动'))
        try:
            self.doConfigInfo(False)
            if self.appCheckbox.GetValue():
                thread = threading.Thread(target=self.startRun)
                thread.start()
            if self.webForumCheckbox.GetValue():
                thread = threading.Thread(target=self.startWebForumMain)
                thread.start()
        except Exception as e:
            s = traceback.format_exc()
            self.printLog(s)
            logging.error(s)

    def startRun(self):
        try:
            self.run = Run()
            self.run.fragmentTimesCallback = self.fragmentTimesFinish
            self.configInfo.statue = True
            self.configInfo.toStr()
            self.run.start(self.configInfo, self.auto, self.printLog)
        except Exception as e:
            s = traceback.format_exc()
            self.printLog(s)
            logging.error(s)

    def startWebForumMain(self):
        try:
            self.webForum = WebForumMain()
            self.webForum.fragmentTimesCallback = self.fragmentForumTimesFinish
            self.webForum.start(self.configInfo, self.printLog)
        except Exception as e:
            s = traceback.format_exc()
            self.printLog(s)
            logging.error(s)

    def btnHandlerCrop_click(self,event):
        valid = self.validateForm()
        if valid == True:
            self.forbit()
        else:
            return
        self.start(False)

    def btnAutoCrop_click(self,event):
        valid = self.validateForm()
        if valid == True:
            self.forbit()
        else:
            return
        self.start(True)


    def btnPauseCrop_click(self, event):
        self.printLog('暂停截图')
        slp = 0
        if self.appCheckbox.GetValue() and self.run:
            self.run.pause()
            slp = 5
        if self.webForumCheckbox.GetValue() and self.webForum:
            self.webForum.pause()
        time.sleep(slp)
        self.enable()


    def validateForm(self):
        times = self.times.GetValue()
        if not times:
            self.dialogTips('时间段不能为空!')
            return False
        savePath = self.savePath.GetValue()
        if not savePath:
            self.dialogTips('保存路径不能为空!')
            return False
        ftnnMob = self.futuniuniuCheckbox.GetValue()
        ftnnPc = self.futuniuniuPcCheckbox.GetValue()
        uname = self.uname.GetValue()
        pswd = self.pswd.GetValue()
        if ftnnMob == True or ftnnPc == True:
            if not uname or not pswd:
                self.dialogTips('用户名和密码，不能为空!')
                return False
        if ftnnMob == True or ftnnPc == True or self.dazhihuiCheckbox.GetValue() == True or \
            self.dongfangcaifuCheckbox.GetValue() == True or self.tonghuashunCheckbox.GetValue() == True:
            return True
        self.dialogTips('请选择平台!')
        return False

    def dialogTips(self, msg):
        toastone = wx.MessageDialog(None, msg, "警告信息提示", wx.YES_DEFAULT | wx.ICON_WARNING)
        if toastone.ShowModal() == wx.ID_YES:
            toastone.Destroy()

# pyinstaller -F -w -i car.ico mainUI.py
class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()