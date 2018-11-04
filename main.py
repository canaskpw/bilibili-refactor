# https://www.bilibili.com/video/av15478453
        # q = QPixmap()
        # q.loadFromData(requests.get("https://i0.hdslb.com/bfs/bangumi/67f27e01bea099e46b8bdb48133d0e767c3ee4ed.jpg@352w_469h.webp").content)
        # self.label.setPixmap(q)
        # self.label.setScaledContents(True)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from ui import *
import time
import pyperclip
import re
import ssl
import urllib.request
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from platform import system
import hashlib
import urllib.parse
import time

appkey = "1d8b6e7d45233436"
app_secret = "560c52ccd288fed045859ed18bffd973"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400",
    "Cookie": "CURRENT_QUALITY=64; DedeUserID=227050458; "
}


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        # self.show_web()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        
        self.run_dir = os.getcwd()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.input_url)
        # self.timer.start(1000)
        self.display_table.setColumnWidth(0, 60)
        self.display_table.setColumnWidth(1, 250)
        self.display_table.setColumnWidth(2, 70)
        self.display_table.setColumnWidth(3, 70)
        self.display_table.setColumnWidth(4, 250)
        self.display_table.setColumnWidth(5, 100)
        self.worksearch = Worksearch()
        self.worksearch.done.connect(self.search_done)
        self.workjiexi = Workjiexi()
        self.workjiexi.done.connect(self.jiexi_done)
        self.workjiexi.finished.connect(self.jiexi_finshed)
        self.workdownload = Workdownload()
        self.workdownload.update.connect(self.update_progress)
        self.workdownload.para_update.connect(self.para_done)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested[QtCore.QPoint].connect(self.video_rightMenuShow)
        self.tableWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_2.customContextMenuRequested[QtCore.QPoint].connect(self.fanju_rightMenuShow)
        self.list_ = []
        self.title = ''
        self.m_flag = False
        self.page = 1
        self.donghua_time = 100
        self.view_type = "video"
        self.search_video_list = []
        self.search_fanju_list = []

    def mousePressEvent(self, event):
        x = (event.globalPos()-self.pos()).x()
        y = (event.globalPos()-self.pos()).y()
        if event.button() == Qt.LeftButton and x < 915 and y < 40:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def before_page(self):
        current_rect = QRect(90, 50, 870, 570)
        next_rect = QRect(-920, 50, 870, 570)
        pre_rect = QRect(1700, 50, 870, 570)

        if self.page == 1:
            self.move_frame(self.search_frame,self.setting_frame,current_rect,pre_rect,next_rect)
            self.page = 3
        elif self.page == 2:
            self.move_frame(self.download_frame,self.search_frame,current_rect,pre_rect,next_rect)
            self.page = 1
        elif self.page == 3:
            self.move_frame(self.setting_frame,self.download_frame,current_rect,pre_rect,next_rect)
            self.page = 2


    def next_page(self):
        current_rect = QRect(90, 50, 870, 570)
        next_rect = QRect(1700, 50, 870, 570)
        pre_rect = QRect(-920, 50, 870, 570)
        if self.page == 1:
            self.move_frame(self.search_frame,self.download_frame, current_rect,pre_rect,next_rect)
            self.page = 2
        elif self.page == 2:
            self.move_frame(self.download_frame,self.setting_frame, current_rect,pre_rect,next_rect)
            self.page = 3
        elif self.page == 3:
            self.move_frame(self.setting_frame,self.search_frame, current_rect,pre_rect,next_rect)
            self.page = 1


    def move_frame(self,fram1, fram2,current_rect,pre_rect,next_rect):
            fram1.animation = QPropertyAnimation(
                fram1, b'geometry')
            fram1.animation.setDuration(self.donghua_time)
            fram1.animation.setStartValue(
                 current_rect)
            fram1.animation.setEndValue(
               pre_rect)
            fram1.animation.start()

            fram2.animation = QPropertyAnimation(
                fram2, b'geometry')
            fram2.animation.setDuration(self.donghua_time)
            fram2.animation.setStartValue(
                next_rect)
            fram2.animation.setEndValue(
                current_rect)
            fram2.animation.start()



    def input_url(self):

        try:
            if re.match(r'^https://www.bilibili.com/video/av', pyperclip.paste()):
                if self.url_edit.text() == "":
                    self.url_edit.setText(pyperclip.paste())

        except Exception as e:
            print()

    def jiexi(self):
        self.list_ = []
        while self.display_table.rowCount():
            self.display_table.removeRow(0)
        if self.url_edit.text():
            self.workjiexi.url = self.url_edit.text()
            # self.workjiexi.url = "https://www.bilibili.com/bangumi/play/ep232520"
            # self.workjiexi.url ="https://www.bilibili.com/video/av15478453"
            # self.workjiexi.url = "https://www.bilibili.com/bangumi/play/ep131738"
            self.workjiexi.start()

    def jiexi_done(self, list_, title):
        self.title = title
        self.list_.append(list_)

        rowcount = self.display_table.rowCount()
        # if rowcount != 0:
        #     if int(list_[0]) >= rowcount:
        #         self.insert_table(rowcount,list_)
        #     else:
        #         for i in range(rowcount):
        #             if int(list_[0]) < int(self.display_table.item(i,1).text().split('.')[0]):
        #                 self.insert_table(i,list_)
        #                 break

        # else:
        self.insert_table(rowcount, list_)
        # self.display_table.setItem(rowcount,3,content)

    def insert_table(self, index, list_):
        check_radio = QCheckBox()
        progress = QProgressBar()
        self.display_table.insertRow(index)
        self.display_table.setCellWidget(index, 0, check_radio)
        self.display_table.setItem(index, 1, QTableWidgetItem(list_[1]))
        self.display_table.setItem(index, 2, QTableWidgetItem(list_[2]))
        self.display_table.setItem(
            index, 3, QTableWidgetItem(str(list_[3])+" M"))
        self.display_table.setCellWidget(index, 4, progress)
        self.display_table.setItem(
            index, 5, QTableWidgetItem("0/"+str(len(list_[4]))))

    def jiexi_finshed(self):
        pass


    def download(self):
        if not os.path.exists(self.title):
            os.makedirs(self.title)
        self.workdownload.num = []
        self.workdownload.title = self.title
        self.workdownload.list_ = self.list_
        for i in range(self.display_table.rowCount()):
            if self.display_table.cellWidget(i, 0).isChecked():
                self.workdownload.num.append(i)
        self.workdownload.start()

    def all_select(self, v):
        for i in range(self.display_table.rowCount()):
            self.display_table.cellWidget(i, 0).setChecked(v)

    def update_progress(self, percent, num):
        self.display_table.cellWidget(num, 4).setValue(percent)

    def para_done(self, num, para):
        self.display_table.setItem(num, 5, QTableWidgetItem(
            para+'/'+self.display_table.item(num, 5).text().split('/')[1]))

    def close_click(self):
        self.close()

    def min_click(self):
        self.showMinimized()

    def conver_done(self):
        QMessageBox.information(self, '提示', '转换成功！！')

    def start_search(self):
        self.page_change(1)

    def search_done(self,list):
        self.total_page_label.setText("共"+str(list['pageinfo']['video']['pages'])+"页")

        list = list['result']
        self.search_video_list = list['video']
        self.search_fanju_list = list['bangumi']
        for i in list['video']:
            rowcount = self.tableWidget.rowCount()
            self.insert_search_video_table(rowcount,i)

        for i in list['bangumi']:
            rowcount = self.tableWidget_2.rowCount()
            self.insert_search_fanju_table(rowcount,i)

    def insert_search_video_table(self, index, list_):
        self.tableWidget.insertRow(index)

        pbdatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(list_['pubdate']))
        title = list_['title']
        up = list_['author']
        duration = list_['duration']
        brief = list_['description']
        view = list_['play']
        self.tableWidget.setItem(index, 0, QTableWidgetItem(title))
        self.tableWidget.setItem(index, 1,QTableWidgetItem(brief))
        self.tableWidget.setItem(index, 2,QTableWidgetItem(duration))
        self.tableWidget.setItem(index,3,QTableWidgetItem(pbdatetime))
        self.tableWidget.setItem(index,4,QTableWidgetItem(up))
        self.tableWidget.setItem(index,5,QTableWidgetItem(str(view)))

    def insert_search_fanju_table(self, index, list_):
        self.tableWidget_2.insertRow(index)
        pbdatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(list_['pubdate']))
        title = list_['title']
        brief = list_['evaluate']
        total_ji = list_['total_count']
        current_ji = list_['newest_ep_index']
        if list_['is_finish']:
            is_wanji =  "是"
        else:
            is_wanji = '否'
        view = list_['play_count']
        str_ = f'{str(current_ji)}/{str(total_ji)}'
        self.tableWidget_2.setItem(index, 0, QTableWidgetItem(title))
        self.tableWidget_2.setItem(index, 1,QTableWidgetItem(brief))
        self.tableWidget_2.setItem(index, 2,QTableWidgetItem(pbdatetime))
        self.tableWidget_2.setItem(index,3,QTableWidgetItem(str_))
        self.tableWidget_2.setItem(index,4,QTableWidgetItem(is_wanji))
        self.tableWidget_2.setItem(index,5,QTableWidgetItem(str(view)))


    def page_change(self,page):
        self.page_label.setText(f"第{str(page)}页")
        if self.search_input.text():
            while self.tableWidget.rowCount():
                self.tableWidget.removeRow(0)
            while self.tableWidget_2.rowCount():
                self.tableWidget_2.removeRow(0)
            self.worksearch.key = self.search_input.text()
            self.worksearch.page = page
            self.worksearch.start()

    def search_next_page(self):
        page = int(self.page_label.text()[1:-1])
        total_page = int(self.total_page_label.text()[1:-1])
        if page < total_page:
            page += 1
            self.page_change(page)

    def search_before_page(self):
        page = int(self.page_label.text()[1:-1])
        if page > 1:
            page -= 1
            self.page_change(page)

    def view_search_video(self):
        if self.view_type != 'video':
            current_rect = QRect(70,90,770,420)
            pre_rect = QRect(880,90,770,420)
            next_rect = QRect(-790,90,770,420)
            self.move_frame(self.tableWidget_2,self.tableWidget,current_rect,pre_rect,next_rect)
            self.view_type = "video"

    def view_search_fanju(self):
        if self.view_type != 'fanju':
            current_rect = QRect(70,90,770,420)
            pre_rect = QRect(-790,90,770,420)
            next_rect = QRect(880,90,770,420)
            self.move_frame(self.tableWidget,self.tableWidget_2,current_rect,pre_rect,next_rect)
            self.view_type = "fanju"

    def video_rightMenuShow(self):
        rightMenu = QMenu(self.tableWidget)
        removeAction = QAction("下载", self, triggered=self.download_video) # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
        rightMenu.addAction(removeAction)
        # addAction = QAction("添加", self,)       # 也可以指定自定义对象事件
        # rightMenu.addAction(addAction)
        rightMenu.exec_(QCursor.pos())

    def fanju_rightMenuShow(self):
        rightMenu = QMenu(self.tableWidget)
        removeAction = QAction("下载", self, triggered=self.download_fanju) # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
        rightMenu.addAction(removeAction)
        # addAction = QAction("添加", self,)       # 也可以指定自定义对象事件
        # rightMenu.addAction(addAction)
        rightMenu.exec_(QCursor.pos())

    def download_video(self):
        index = self.tableWidget.currentIndex().row()
        current_video = self.search_video_list[index]
        self.title = current_video['title']
        self.url_edit.setText(current_video['arcurl'])
        self.next_page()
        self.jiexi()

    def download_fanju(self):
        index = self.tableWidget_2.currentIndex().row()
        current_video = self.search_fanju_list[index]
        self.title = current_video['title']
        self.url_edit.setText(current_video['typeurl'])
        self.next_page()
        self.jiexi()
        
class Worksearch(QThread):
    """docstring for WorkThread"""
    done = pyqtSignal(dict)
    def __init__(self):
        super(Worksearch, self).__init__()

    def run(self):
        page = self.page
        k = urllib.parse.quote(self.key)
        str = f'appkey={appkey}&keyword={k}&page={page}'+app_secret
        sign = hashlib.md5(str.encode('utf-8')).hexdigest()
        search_url = f"https://api.bilibili.cn/search?appkey={appkey}&keyword={k}&page={page}&sign={sign}"
        print(search_url)
        result = requests.get(search_url).json()

        self.done.emit(result)


class Workjiexi(QThread):
    """docstring for WorkThread"""
    done = pyqtSignal(list, str)
    all_done = pyqtSignal()
    error = pyqtSignal()

    def __init__(self):
        super(Workjiexi, self).__init__()

    def run(self):            
        executor = ThreadPoolExecutor(60)
        if re.findall('av\d+$',self.url):
            cid = re.findall('av(\d+$)',self.url)[0]
            self.is_ep = False
        else:
            self.is_ep = True

        
        if not self.is_ep:
            url = f'https://api.bilibili.com/view?appkey={appkey}&batch=1&id={cid}&page=1&type=json'
            response = requests.get(url, headers=headers).json()
            self.title = response['title'].replace(' ', '-')
            all_list = response['list']
            executor.map(self.thread_jiexi, [i["cid"] for i in all_list], [
                         i['page'] for i in all_list], [i['part'] for i in all_list])

        else:
            response = requests.get(self.url, headers=headers)
            title_zz = '''"chn_name":"(.*?)","copyright"'''
            self.title = re.findall(title_zz,response.text)[0].replace(' ', '-')
            print(self.title)
            zz = '''"episodes":(\[\{.*?\}\]),"evaluate":'''
            result = re.findall(zz, response.text)
            all_list = eval(result[0])
            executor.map(self.thread_jiexi, [i["cid"] for i in all_list], [
                             i['index'] for i in all_list], [i['index_title'] for i in all_list])

            
    def thread_jiexi(self, cid, index, title):
        self.jiexi_xunhuan(cid, index, title,1)

    def jiexi_xunhuan(self, cid, index, title, season_type):
        if 'windows' in system().lower():
            if self.is_ep:
                url = os.popen('node.exe index_ep.js %s %s' % (cid, str(season_type))).read().strip()
            else:
                url = os.popen('node.exe index_av.js %s %s' % (cid, str(season_type))).read().strip()
        else:
            if self.is_ep:
                url = os.popen('./node index_ep.js %s %s' % (cid, str(season_type))).read().strip()
            else:
                url = os.popen('./node index_av.js %s %s' % (cid, str(season_type))).read().strip()
        respond2 = requests.get(url, headers=headers).json()

        time = str(sum([int(i['length']) for i in respond2['durl']])//60000) + ":"+str(
            int((sum([int(i['length']) for i in respond2['durl']]) % 60000)//1000))
        size = round(sum([int(i['size'])
                          for i in respond2['durl']])/1024/1024, 1)
        # for i in respond2['durl']:

        url = [i['url'] for i in respond2['durl']]
        if not title:
            result3 = [index, index]
        else:
            if re.match('^\d', title):
                result3 = [index, title]
            else:
                result3 = [index, str(index)+'.'+title]

        result3.extend([time, size, url])
        # print(result3)
        self.done.emit(result3, self.title)





class Workdownload(QThread):
    """docstring for WorkThread"""
    update = pyqtSignal(int, int)
    para_update = pyqtSignal(int, str)
    all_done = pyqtSignal()
    error = pyqtSignal()

    def __init__(self):
        super(Workdownload, self).__init__()

    def run(self):
        self.before = 0
        list_thread = []
        for i in self.num:
            title = self.list_[i][1].replace(" ", "-")
            url = self.list_[i][4]
            t1 = threading.Thread(
                target=self.download_thread, args=(url, title), name=str(i))
            list_thread.append(t1)

        self.threadLock = threading.Lock()
        for j in list_thread:
            j.start()

    def download_thread(self, url, title):
        ssl._create_default_https_context = ssl._create_unverified_context
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('Host', 'tx.acgvideo.com'),
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
            ('Accept', '*/*'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Range', 'bytes=0-'),  # Range 的值要为 bytes=0- 才能下载完整视频
            ('Referer', 'https://www.bilibili.com/video/av14543079/'),
            ('Origin', 'https://www.bilibili.com'),
            ('Connection', 'keep-alive'),
        ]
        urllib.request.install_opener(opener)
        for i in enumerate(url):
            self.para_update.emit(
                int(threading.current_thread().name), str(i[0]+1))
            if not os.path.exists(os.path.join(run_dir, self.title)+"/" + title+"__"+str(i[0]+1)+'.flv'):
                urllib.request.urlretrieve(i[1], filename=os.path.join(
                    run_dir, self.title)+"/" + title+"__"+str(i[0]+1)+'.flv', reporthook=self.report)
            else:
                print('已经存在!')
        else:
            self.threadLock.acquire()
            self.hecheng(title)
            self.threadLock.release()

    def hecheng(self, title):
        os.chdir(self.title)
        title_list = os.listdir('.')
        title_list = [i.split("__")[0] for i in title_list]
        c = Counter()
        for ch in title_list:
            c[ch] = c[ch] + 1

        if c[title] != 1:
            title_name_list = []
            for num in range(c[title]):
                path_filename = title+'__'+str(num+1)
                os.system('''ffmpeg -i %s.flv -c copy -bsf:v h264_mp4toannexb -f mpegts %s.ts''' %
                          (path_filename, path_filename))
                title_name_list.append(path_filename)

            add_list = "|".join([j+'.ts' for j in title_name_list])
            del_list = " ".join([j+'.ts' for j in title_name_list])
            del2_list = " ".join([j+'.flv' for j in title_name_list])
            os.system(
                '''ffmpeg -i "concat:%s" -c copy -bsf:a aac_adtstoasc -movflags +faststart %s.mp4''' % (add_list, title))
            if 'windows' in system().lower():
                os.system('''del %s %s''' % (del_list, del2_list))
            else:
                os.system('''rm -f %s %s''' % (del_list, del2_list))

        elif c[title] == 1:
            os.system(
                '''ffmpeg -i %s.flv -c copy -bsf:a aac_adtstoasc -movflags +faststart %s.mp4''' % (title+"__1", title))
            if 'windows' in system().lower():
                os.system('''del %s.flv''' % (title+"__1"))
            else:
                os.system('''rm -f %s.flv''' % (title+"__1"))
        os.chdir(run_dir)

    def report(self, count, blockSize, totalSize):
        downloadedSize = count * blockSize
        percent = int(downloadedSize * 100 / totalSize)
        if not self.before == percent:
            self.before = percent
            self.update.emit(percent, int(threading.current_thread().name))
        # sys.stdout.write(f"\rDownloaded: {downloadedSize} bytes, Total: {totalSize} bytes, {percent} % complete")
        # sys.stdout.flush()


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    run_dir = os.getcwd()
    path = ''
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec())
