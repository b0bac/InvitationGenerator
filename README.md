# InvitationGenerator
基于Python3.10和Tkinter写的一个用于生成邀请函的图形界面小工具
测试环境MacOS，测试图片来源于图怪兽模版，没有任何含义

## 操作系统及测试环境
+ OS: MacOS 13.2.1 (22D68) Ventura
+ Python: 3.10
+ tkinter
```bash
brew install python-tk@3.10
```
+ PIL
```bash
python3 -m pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```
## 使用方式
```bash
python3 InvitationGenerator.py
```
图形化界面，按照要求填写相关必须的输入项，点击开始生成即可。
![image](https://user-images.githubusercontent.com/11972644/227088807-70fbabfb-92d4-4cdc-b1ea-1adf5d6f32fc.png)
![image](https://user-images.githubusercontent.com/11972644/227088892-3e3606f9-6317-4639-833b-266a5cba712c.png)
![image](https://user-images.githubusercontent.com/11972644/227088944-7341e16a-48a9-41f7-a6d5-81ae2e951ea7.png)
![image](https://user-images.githubusercontent.com/11972644/227089035-98f891ab-70a1-41e7-9707-1cbfd24e7257.png)
![李四](https://user-images.githubusercontent.com/11972644/227089091-9ff747d0-158d-4d18-82ea-06b7485ccc6b.jpg)


## 优化
+ 版本v1.1
  + 优化各类文件选择操作，从输入文件路径优化成文件管理器选择文件
  + 颜色从输入RGB值优化成为颜色选择
