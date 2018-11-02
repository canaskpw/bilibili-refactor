# bilibili-download
一个下载bilibili的视频的软件，用pyqt5结合多线程及线程池写的(可以下载番剧ep及av)  
## 依赖  
PyQt5 python3  

## 运行
### linux  
项目中包含node执行程序，当然如果你在linux上运行你可以将node.exe删除了
但是你要赋予node可执行权限
```bash
sudo chmod +x node
```  
然后安装pip3 以及python的第三方库PyQt5 
```bash
sudo apt-get install python3-pip
pip3 install PyQt5 pyperclip -i https://mirrors.aliyun.com/pypi/simple/
```
确保你的linux电脑中包含ffmpeg,它是用来合成及转换下载的分段视频的  
以上都完成了你可以启动此软件了  
```bash
python3 main.py
```

![1](./readme_img/1.png)
![2](./readme_img/2.png)

