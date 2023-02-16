#! /usr/bin/env python
# -*- coding:utf-8 -*-
#====#====#====#====
# __author__ = "renys"
#weixin:ysongren
#QQ:774113517
#FileName: *.py
#Version:1.0.0
#====#====#====#====
configPath = 'config_lpcar.ini'

class ConfigInfo(object):
    savePath = ''; times = ''; uname = ''; pswd = ''; dongfangcaifuCheckbox = ''; dazhihuiCheckbox = ''; tonghuashunCheckbox = ''; futuniuniuCheckbox = ''; futuniuniuPcCheckbox = ''; everyDayCropCheckbox = ''; dongfangcaifuPage = ''; tonghuashunPage = ''; dazhihuiPage = ''; futuniuniuMobPage = ''; futuniuniuPcPage = '';
    pVersion = '7.1.2'; statue = True;
    qichezhijia_C01 = 1; qichezhijia_C11 = 1; qichezhijia_T03 = 1; dongchedi_C01 = 1; dongchedi_C11 = 1;
    dongchedi_T03 = 1; xinchuxing_xinchuxing = 1;
    startHour= 8; endHour= 21; minute= 10;
    appModul = 0; webForumModul = 1;

    def init(self, savePath,times,uname,pswd,dongfangcaifuCheckbox,dazhihuiCheckbox,tonghuashunCheckbox,futuniuniuCheckbox,futuniuniuPcCheckbox,everyDayCropCheckbox,dongfangcaifuPage,tonghuashunPage,dazhihuiPage,futuniuniuMobPage,futuniuniuPcPage):
        self.savePath = savePath
        self.times = times
        self.uname = uname
        self.pswd = pswd
        self.dongfangcaifuCheckbox = dongfangcaifuCheckbox
        self.dazhihuiCheckbox = dazhihuiCheckbox
        self.tonghuashunCheckbox = tonghuashunCheckbox
        self.futuniuniuCheckbox = futuniuniuCheckbox
        self.futuniuniuPcCheckbox = futuniuniuPcCheckbox
        self.everyDayCropCheckbox = everyDayCropCheckbox
        self.dongfangcaifuPage = dongfangcaifuPage
        self.tonghuashunPage = tonghuashunPage
        self.dazhihuiPage = dazhihuiPage
        self.futuniuniuMobPage = futuniuniuMobPage
        self.futuniuniuPcPage = futuniuniuPcPage

    def initWebForum(self, qichezhijia_C01, qichezhijia_C11, qichezhijia_T03, dongchedi_C01, dongchedi_C11, dongchedi_T03, xinchuxing_xinchuxing, startHour, endHour, minute):
        self.qichezhijia_C01 = qichezhijia_C01;
        self.qichezhijia_C11 = qichezhijia_C11;
        self.qichezhijia_T03 = qichezhijia_T03;
        self.dongchedi_C01 = dongchedi_C01;
        self.dongchedi_C11 = dongchedi_C11;
        self.dongchedi_T03 = dongchedi_T03;
        self.xinchuxing_xinchuxing = xinchuxing_xinchuxing;
        self.startHour = startHour;
        self.endHour = endHour;
        self.minute = minute;

    def initModul(self, appModul, webForumModul):
        self.appModul = appModul;
        self.webForumModul = webForumModul;
        print('initModul', appModul, webForumModul)

    def parseFagmentPage(self, v):
        fragments = v.split(',')
        for ft in fragments:
            appPage = ft.split('-')
            app = appPage[0]
            page = appPage[1]
            if app == '同花顺':
                self.tonghuashunPage = page
            elif app == '富途牛牛':
                self.futuniuniuMobPage = page
            elif app == '富途牛牛PC':
                self.futuniuniuPcPage = page
            elif app == '大智慧':
                self.dazhihuiPage = page
            elif app == '东方财富':
                self.dongfangcaifuPage = page

    def parseFagmentSwitch(self, v):
        fragments = v.split(',')
        for ft in fragments:
            appOnOff = ft.split('-')
            app = appOnOff[0]
            switch = appOnOff[1]
            if app == '同花顺':
                self.tonghuashunCheckbox = switch
            elif app == '富途牛牛':
                self.futuniuniuCheckbox = switch
            elif app == '富途牛牛PC':
                self.futuniuniuPcCheckbox = switch
            elif app == '大智慧':
                self.dazhihuiCheckbox = switch
            elif app == '东方财富':
                self.dongfangcaifuCheckbox = switch

    def parseUser(self, v):
        sp = v.split('-')
        self.uname = sp[0]
        self.pswd = sp[1]

    def parseHour(self, v):
        sp = v.split('-')
        self.startHour = sp[0]
        self.endHour = sp[1]

    def parseModule(self, v):
        sp = v.split(',')
        for ft in sp:
            appOnOff = ft.split('-')
            app = appOnOff[0]
            switch = appOnOff[1]
            if app == 'app':
                self.appModul = switch
            elif app == 'web':
                self.webForumModul = switch

    def parseWebFagments(self, v):
        sp = v.split(',')
        for ft in sp:
            appOnOff = ft.split('-')
            app = appOnOff[0]
            page = appOnOff[1]
            if app == '汽车之家C01': #汽车之家C01,汽车之家C11,汽车之家T03,懂车帝C01,懂车帝C11,懂车帝T03,新出行
                self.qichezhijia_C01 = page
            elif app == '汽车之家C11':
                self.qichezhijia_C11 = page
            elif app == '汽车之家T03':
                self.qichezhijia_T03 = page
            elif app == '懂车帝C01':
                self.dongchedi_C01 = page
            elif app == '懂车帝C11':
                self.dongchedi_C11 = page
            elif app == '懂车帝T03':
                self.dongchedi_T03 = page
            elif app == '新出行':
                self.xinchuxing_xinchuxing = page

    def toStr(self):
        var = 'savePath,times,uname,pswd,dongfangcaifuCheckbox,dazhihuiCheckbox,tonghuashunCheckbox,futuniuniuCheckbox,futuniuniuPcCheckbox,everyDayCropCheckbox,dongfangcaifuPage,tonghuashunPage,dazhihuiPage,futuniuniuMobPage,futuniuniuPcPage,statue,' \
              'qichezhijia_C01, qichezhijia_C11, qichezhijia_T03, dongchedi_C01, dongchedi_C11, dongchedi_T03, xinchuxing_xinchuxing, startHour, endHour, minute, appModul, webForumModul'
        vs = var.split(',')
        st = 'ConfigInfo '
        for v in range(len(vs)):
            # st += vs[v] + ':{'+str(v)+'}; '
            st += vs[v] + ':{}; '
        print(st.format(self.savePath,self.times,self.uname,self.pswd,self.dongfangcaifuCheckbox,self.dazhihuiCheckbox,self.tonghuashunCheckbox,self.futuniuniuCheckbox,
                        self.futuniuniuPcCheckbox,self.everyDayCropCheckbox,self.dongfangcaifuPage,self.tonghuashunPage,self.dazhihuiPage,self.futuniuniuMobPage,self.futuniuniuPcPage, self.statue,
                        self.qichezhijia_C01, self.qichezhijia_C11, self.qichezhijia_T03, self.dongchedi_C01, self.dongchedi_C11, self.dongchedi_T03, self.xinchuxing_xinchuxing,
                        self.startHour, self.endHour, self.minute,self.appModul, self.webForumModul))

    def toFragmentsPage(self, app):
        return app.format(self.tonghuashunPage, self.futuniuniuMobPage, self.dazhihuiPage, self.dongfangcaifuPage, self.futuniuniuPcPage)

    def toFragmentsSwitch(self, app):
        return app.format(self.tonghuashunCheckbox, self.futuniuniuCheckbox, self.dazhihuiCheckbox, self.dongfangcaifuCheckbox, self.futuniuniuPcCheckbox)

    def toModuleSwitch(self):
        app = 'app-{},web-{}'
        return app.format(self.appModul, self.webForumModul)

    def toWebFragments(self):
        app = '汽车之家C01-{},汽车之家C11-{},汽车之家T03-{},懂车帝C01-{},懂车帝C11-{},懂车帝T03-{},新出行-{}'
        return app.format(self.qichezhijia_C01, self.qichezhijia_C11, self.qichezhijia_T03, self.dongchedi_C01, self.dongchedi_C11, self.dongchedi_T03, self.xinchuxing_xinchuxing)

    def save(self):
        app = '同花顺-{},富途牛牛-{},大智慧-{},东方财富-{},富途牛牛PC-{}'
        content = 'savePath|' + self.savePath + '\n'
        content += 'everyDay|' + str(self.everyDayCropCheckbox) + '\n'
        content += 'times|' + self.times + '\n'
        content += 'usrPswd|' + self.uname + '-' + self.pswd + '\n'
        content += 'fragments|' + self.toFragmentsPage(app) + '\n'
        content += 'switch|' + self.toFragmentsSwitch(app) + '\n'
        content += 'webFragments|' + self.toWebFragments() + '\n'
        content += 'module|' + self.toModuleSwitch() + '\n'
        content += 'hour|' + str(self.startHour) + '-' + str(self.endHour) + '\n'
        content += 'minute|' + str(self.minute) + '\n'
        # tmpPath = configPath.replace('.txt', '-tmp.txt')
        tmpPath = configPath
        print('tmpPath', tmpPath)
        print('write content', content)
        with open(tmpPath, mode='w') as f:
            f.write(content)

    def parseConfigFile(self):
        rFile = open(configPath, "r")
        content = rFile.readlines()
        # print('配置文件内容：{0}'.format(content))
        rFile.close()

        for temp in content:
            sp = temp.split('|')
            k = sp[0]
            v = sp[1].replace('\n', '')
            if k == 'savePath':
                self.savePath = v
            elif k == 'times':
                self.times = v
            elif k == 'fragments':
                self.parseFagmentPage(v)
            elif k == 'switch':
                self.parseFagmentSwitch(v)
            elif k == 'usrPswd':
                self.parseUser(v)
            elif k == 'everyDay':
                self.everyDayCropCheckbox = v
            elif k == 'webFragments':
                self.parseWebFagments(v)
            elif k == 'module':
                self.parseModule(v)
            elif k == 'hour':
                self.parseHour(v)
            elif k == 'minute':
                self.minute = v

        self.toStr()
        # self.save() test

if __name__ == '__main__':
    info = ConfigInfo()
    info.parseConfigFile()