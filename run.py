#! /usr/bin/env python
# -*- coding:utf-8 -*-
#====#====#====#====
# __author__ = "renys"
#weixin:ysongren
#QQ:774113517
#FileName: *.py
#Version:1.0.0
#====#====#====#====
import threading
import time

import traceback
import logging

from app.appDazhihui import Dazhihui
from app.appDongfangcaifu import Dongfangcaifu
from app.appFutuniuniu import Futuniuniu
from app.appTonghuashun import Tonghuashun
from app.webFutuniuniu import WebFutuniuniu
from util.timeUtil import TimeUtil

logging.basicConfig(filename='log.log')

class Run(object):

    def startTask(self, configInfo, st, index):
        self.configInfo = configInfo
        self.startTime = st
        self.timesIndex = index
        if configInfo.futuniuniuPcCheckbox == 1:
            self.startApp(WebFutuniuniu(configInfo.futuniuniuPcPage))
        if configInfo.dazhihuiCheckbox == 1:
            self.startApp(Dazhihui(configInfo.dazhihuiPage))
        if configInfo.futuniuniuCheckbox == 1:
            self.startApp(Futuniuniu(configInfo.futuniuniuMobPage))
        if configInfo.tonghuashunCheckbox == 1:
            self.startApp(Tonghuashun(configInfo.tonghuashunPage))
        if configInfo.dongfangcaifuCheckbox == 1:
            self.startApp(Dongfangcaifu(configInfo.dongfangcaifuPage))

    def startApp(self, app):
        if self.configInfo.statue == True:
            app.run = self
            self.app = app
            self.app.start(logging)

    def pause(self):
        self.configInfo.statue = False
        thread = threading.Thread(target=self.pauseThread)
        thread.start()

    def pauseThread(self):
        try:
            if self.app:
                self.app.stop()
        except Exception as e:
            s = traceback.format_exc()
            print('停止任务 发生异常 ' + s)

    def start(self, configInfo, auto, printLog):
        self.configInfo = configInfo
        self.auto = auto
        self.printLog = printLog
        thread = threading.Thread(target=self.startThread)
        thread.start()

    def startThread(self):
        configInfo = self.configInfo
        try:
            self.printLog('启动任务')
            ts = configInfo.times
            timeUtime = TimeUtil()
            if ts:
                tt = ts.split('-')
                tm = {}
                for j in range(len(tt)):
                    tm[tt[j]] = False
                flag = True
                bd = timeUtime.getCurDate()
                while flag:
                    cd = timeUtime.getCurDate()
                    if bd != cd:
                        bd = cd
                        for j in range(len(tt)):
                            tm[tt[j]] = False
                    for i in range(len(tt)):
                        st = tt[i]
                        et = st
                        if i == len(tt) - 1:
                            et = '21:00'
                        else:
                            et = tt[i + 1]
                        if tm[st]:
                            continue
                        checkIn = timeUtime.checkInTime(st, et)
                        if self.configInfo.statue == False:
                            return
                        if checkIn:
                            index = i + 1 if i == 0 else (i * 2 + 1)
                            self.startTask(configInfo, st, index)
                            if self.configInfo.statue == False:
                                return
                            tm[st] = True
                            self.fragmentTimesCallback(st, i == len(tt) - 1)
                            if i == len(tt) - 1:
                                if configInfo.everyDayCropCheckbox == 0:
                                    return
                                if self.auto == False:
                                    return
                        else:
                            slp = 1
                            if i == len(tt) - 1:
                                slp = 60
                                if self.auto == True:
                                    slp = 180
                            time.sleep(slp)
                    if self.auto == True:
                        time.sleep(180)
        except Exception as e:
            s = traceback.format_exc()
            self.printLog('启动任务 发生异常 ' + s)
            logging.error('启动任务 发生异常: ' + s)
        finally:
            self.printLog('退出任务')