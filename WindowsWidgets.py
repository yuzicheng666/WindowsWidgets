import tkinter as tk
import pyautogui
import requests
import random
import os

def install():
    url = url_Entry.get()
    img = requests.get(url=url)
    with open('img.png', 'wb') as f:
        f.write(img.content)

def install_():
    global url_Entry
    i_window = tk.Toplevel()
    i_window.title('图片下载工具')
    i_window.geometry('270x70')

    tk.Label(i_window, text='输入下载链接').pack()

    url_Entry = tk.Entry(i_window)
    url_Entry.pack()

    tk.Button(i_window, text='下载', command=install).place(x=220, y=20)

def osk():
    os.system('start osk')

def explorer():
    os.system('taskkill /f /im explorer.exe')
    os.system('start explorer')

def regedit():
    os.system('start regedit')
    
def gpedit_msc():
    os.system('start gpedit.msc')

def cmd():
    os.system('start cmd')

def c():
    os.system('start explorer')

def cleanmgr():
    os.system('start cleanmgr')

def Taskmgr():
    os.system('start Taskmgr')

def msg():
    global ip
    global t
    global msg_window
    msg_window = tk.Toplevel()
    msg_window.geometry('350x250')
    msg_window.title('发送窗口')
    ip = tk.Entry(msg_window)
    ip.pack(pady=10)
    ip_label = tk.Label(msg_window, text='输入要发送的IP地址')
    ip_label.pack(pady=5)

    t = tk.Entry(msg_window)
    t.pack(pady=20)
    t_label = tk.Label(msg_window, text='输入要发送的消息')
    t_label.pack(pady=5)

    button = tk.Button(msg_window, text='发送', command=msg_)
    button.pack(padx=10)

def msg_():
    ip_ = ip.get()
    t_ = t.get()
    os.system(f'msg /server {ip_} * "{t_}"')
    msg_window.destroy()

def extract():
    number.set(random.randint(1, 49))
    label2.update()

def random_():
    global label2, number
    w_r = tk.Toplevel()
    w_r.title('点名程序1.0')
    w_r.geometry('300x200+600+600')

    number = tk.StringVar()
    number.set('')

    title_label = tk.Label(w_r, text='点击按钮开始抽取', font='font.ttf 20')
    title_label.pack()

    tk.Button(w_r, text='开始抽取', command=extract).pack()

    label = tk.Label(w_r, text='抽到的号数是：', font='font.ttf 12')
    label.place(x=30,y=100)

    label2 = tk.Label(w_r, textvariable=number, font='font.ttf 12')
    label2.place(x=150,y=100)

def pyautogui_m():
    global _x,_y,m,x,y
    m = tk.Toplevel()
    m.geometry('350x250')
    m.title('移动鼠标')
    x = tk.Entry(m)
    x.pack(pady=10)
    x_label = tk.Label(m, text='移动到的x坐标')
    x_label.pack(pady=5)

    y = tk.Entry(m)
    y.pack(pady=20)
    y_label = tk.Label(m, text='移动到的y坐标')
    y_label.pack(pady=5)

    button = tk.Button(m, text='发送', command=move)
    button.pack(padx=10)

def move():
    _x = x.get()
    _y = y.get()
    print(_x,_y)
    pyautogui.moveTo(x=_x, y=_y, duration=0.001)
    m.destroy()
     
root = tk.Tk()
root.resizable(0,0)
root.title('windows小工具')
root.geometry('600x400')

title_label = tk.Label(root, text='windows小工具', font='font 25')
title_label.pack()

osk_button = tk.Button(root, text='屏幕键盘',command=osk)
osk_button.place(x=20, y=50)

explorer_button = tk.Button(root, text='重启资源管理器',command=explorer)
explorer_button.place(x=100, y=50)

regedit_button = tk.Button(root, text='注册表编辑器',command=regedit)
regedit_button.place(x=220, y=50)

gpedit_msc_button = tk.Button(root, text='组策略编辑器(家庭版不可用)',command=gpedit_msc)
gpedit_msc_button.place(x=320, y=50)

cmd_button = tk.Button(root, text='命令提示符',command=cmd)
cmd_button.place(x=500, y=50)

c_button = tk.Button(root, text='资源管理器',command=c)
c_button.place(x=20, y=100)

cleanmgr_button = tk.Button(root, text='磁盘清理',command=cleanmgr)
cleanmgr_button.place(x=120, y=100)

Taskmgr_button = tk.Button(root, text='任务管理器',command=Taskmgr)
Taskmgr_button.place(x=220, y=100)

msg_button = tk.Button(root, text='发送窗口',command=msg)
msg_button.place(x=320, y=100)
  
install_img_button = tk.Button(root, text='下载图片',command=install_)
install_img_button.place(x=420, y=100)

random_button = tk.Button(root, text='随机程序',command=random_)
random_button.place(x=520, y=100)

pyautogui_m_button = tk.Button(root, text='控制鼠标',command=pyautogui_m)
pyautogui_m_button.place(x=20, y=150)

root.mainloop()