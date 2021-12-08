import sys
import pygame
import tkinter
# import calendar as ca
# def scream():
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500))
#     pygame.display.set_caption("摆烂")
#     bg_color = (0, 0, 0)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#         screen.fill(bg_color)
#         pygame.display.flip()
#
#
# scream()
from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环