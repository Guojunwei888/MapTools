'''
一个简单的应用
'''

import tkinter as tk  # 导入tkinter
from tkinter import filedialog

import random
import sys
import os

try:
    import pyi_splash
    import time

    for i in range(100):
        text = f"加载中……进度{i}%"
        time.sleep(0.001)  # 模拟一个速度比较慢的加载过程

        pyi_splash.update_text(text)  # 更新显示的文本

    pyi_splash.close()  # 关闭闪屏

except ImportError:
    pass


def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.normpath(os.path.join(base_path, relative_path))

content = None

def read_txt_file():
    # 弹出文件选择对话框，只显示txt文件
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # 如果用户选择了文件
        try:
            # 读取txt文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # 显示文件内容
                text_label1.config(text=content)

                # 指定要保存内容的本地文件路径
                save_path = 'saved_content.txt'  # 可以根据需要修改文件名和路径

                # 将读取的内容写入到本地文件
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(content)

        except Exception as e:
            print(f"读取文件时发生错误: {e}")

def random_txt_file():
    try:
        # 读取txt文件内容
        with open("saved_content.txt", 'r', encoding='utf-8') as file:
            content = file.read()
            # 显示文件内容
            text_label1.config(text=content)

            # 指定要保存内容的本地文件路径
            save_path = 'saved_content.txt'  # 可以根据需要修改文件名和路径

            # 将读取的内容写入到本地文件
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(content)

            # 将文本按行分割成列表
            lines = content.splitlines()

            # 随机选择三行
            selected_lines = random.sample(lines, 3)

            # 将选中的行转换为一个字符串，并用换行符连接
            display_text = '\n'.join(selected_lines)

            # 显示选中的行
            text_label2.config(text=display_text)
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

root = tk.Tk()  # 创建窗口
root.title("TotalWar HarmmerⅢ地图随机器")  # 更改标题
root.iconbitmap("assets/hammer.ico")
root.geometry("800x600+30+50")
root.resizable(False, False)  # 边框大小限制
# root.config(bg="blue")

# 创建一个标签用于显示全地图内容
text_label1 = tk.Label(root, text="地图A\n地图B", justify=tk.LEFT, font=("黑体", 20, "bold"))
text_label1.pack()

# 创建一个标签用于显示随机地图内容
text_label2 = tk.Label(root, text="随机地图池", justify=tk.LEFT, font=("黑体", 20, "bold"))
text_label2.pack()

# 添加一个按钮，用于触发读取txt文件的功能
read_button1 = tk.Button(root, text="选择TXT文件", command=read_txt_file)
read_button1.pack()

read_button2 = tk.Button(root, text="随机地图池", command=random_txt_file)
read_button2.pack()

image = tk.PhotoImage(file=get_path("assets/giphy.gif"))
label = tk.Label(root, text="你好，用户！", image=image, compound="top")
label.pack()  # 显示图片

root.mainloop()  # 保持窗口运行
