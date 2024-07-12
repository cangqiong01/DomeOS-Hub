import tkinter as tk
import webbrowser
#import subprocess


print("Made by DomeTechnology")
print("Made on Python3.12.2")
print("version dev 0.1.2")
# 创建主窗口并应用自定义主题


def close_window():
    root.destroy()

class ResizableWindow:
    def __init__(self, master):
        self.master = master
        master.title("DomeOS_Hub") 

        # 设置窗口默认大小  
        master.geometry("350x200")  
        
        root.configure(background='#F3F3F3')  # 类似Windows 11的窗口背景色

        # 允许窗口改变大小  
        master.resizable(False, False)




        # 创建一个标签，用于在窗口中显示一些文本   
        self.label = tk.Label(master, text="Dev v0.1.2                ")
        self.label.grid(row=0, column=0, columnspan=1, pady=0) 
  
        # 创建几个按钮，并使用grid布局管理器放置它们  
        
        # 添加新按钮，用于弹出新窗口  
        self.new_window_button = tk.Button(master, text="装机必备", width=10, height=1,command=self.open_new_window)  
        self.new_window_button.grid(row=5, column=0)   
          
        # 添加按钮，点击创建一个新窗口  
        self.create_window_button = tk.Button(master, text="应用属性", width=10, height=1, command=self.create_new_window)  
        self.create_window_button.grid(row=10, column=5)  
     # 添加新按钮，用于弹出新窗口  
        self.new_window_button = tk.Button(master, text="码农必备", width=10, height=1, command=self.open_new_window2) 
        self.new_window_button.grid(row=10, column=0) 

        # 添加按钮，点击创建一个新窗口  
        self.create_window_button = tk.Button(master, text="说明", width=10, height=1, command=self.start_new_window)  
        self.create_window_button.grid(row=5, column=5) 
        
        # 添加按钮，点击创建一个新窗口  
        self.create_window_button = tk.Button(master, text="DomeOS软件", width=10, height=1, command=self.start_new_window2)  
        self.create_window_button.grid(row=15, column=0)
        # 添加按钮，点击创建一个新窗口
        self.create_window_button = tk.Button(master, text="关闭窗口", width=10, height=1,command=close_window)
        self.create_window_button.grid(row=15, column=5)


    def open_new_window(self):
        # 创建新窗口  
        new_window = tk.Toplevel(self.master)  
        new_window.title("装机必备")  
  
        # 设置新窗口默认大小  
        new_window.geometry("250x200")  
  
        # 允许新窗口改变大小  
        new_window.resizable(False, False)  
  
        # 在新窗口中添加几个按钮，并实现跳转网页的效果  
        new_button = tk.Button(new_window, text=" 360安全卫士极速版 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://down.360safe.com/setupbeta_jisu.exe")) 
        new_button.pack()
        new_button = tk.Button(new_window, text=" 360极速浏览器 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://dl.360safe.com/cse/360cse_official.exe"))   
        new_button.pack()  
        new_button = tk.Button(new_window, text=" 360驱动大师 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://dl.360safe.com/drvmgr/360DrvMgrInstaller_net.exe"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" 火绒安全软件 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://www.huorong.cn/downloadv5.html?status=hrstat&src=19"))  
        new_button.pack()
        new_button = tk.Button(new_window, text=" 火绒商店 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://www.huorong.cn/product/download.php?pro=appstore"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" 图吧工具箱 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://download.tualatin.club/%E5%9B%BE%E5%90%A7%E5%B7%A5%E5%85%B7%E7%AE%B1202403%E7%BB%BF%E8%89%B2%E7%89%88%E8%87%AA%E5%8A%A8%E8%A7%A3%E5%8E%8B%E7%A8%8B%E5%BA%8F_64bit.exe"))  
        new_button.pack()
        
  
    def open_new_window2(self):  
        # 创建新窗口  
        new_window = tk.Toplevel(self.master)  
        new_window.title("码农必备")  
  
        # 设置新窗口默认大小  
        new_window.geometry("250x200")  
  
        # 允许新窗口改变大小  
        new_window.resizable(False, False)  
  
        # 在新窗口中添加几个按钮，并实现跳转网页的效果  
        new_button = tk.Button(new_window, text=" VSCode ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://vscode.download.prss.microsoft.com/dbazure/download/stable/863d2581ecda6849923a2118d93a088b0745d9d6/VSCodeUserSetup-x64-1.87.2.exe"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" Python3.12.2 ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" Visio Studio ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030:8a746c914584417f8dba24a660d05909"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" Visio Basic ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://down-load.lanrar.com/file/?A2UAPgAxADFRWAA4AzZTPwc4Bj5QWVYWCzpUfwG6Uf5V1QGyCekFwgCyBesA+VewA89U1gJzC3sDZQRwAngEYwNqADsAOAALUW4AMgNqU2EHbQY6UDZWZQs1VGcBZVF2VTMBJQlpBWAAbwVkAG1XZwNqVGMCbQsvA3QEcgJjBDcDMwBlAG0Ae1E2AGYDeFNjB2kGLFA2VjULOlRjAWpRaFViAW8JMAUwADQFMgAxV28DbFQyAjgLPANmBDoCPwQ3AzMAYQBvADFRYgBiAzJTYgdsBjFQIVYmC21UIAF7USVVJgEzCSYFOAAyBW4AZ1dvA25UZAJrCzEDIgR2AjcEaANmADEAYABlUTAAZwNmU2oHawY1UDZWbQs9VHwBc1F2VTMBOgkjBWwAZwVkAGVXZwNhVGcCaAs8Az0EMgJ4BHADcwAgAGAAZVExAGYDZVNkB2sGO1A9VmILP1R0AShROVUlAWsJZQVgAGQFfQBsV2cDd1RgAmkLOAMqBDACbgQ9"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" OpenJDK ", width=20, height=0,  
                                command=lambda: webbrowser.open("https://aka.ms/download-jdk/microsoft-jdk-21.0.2-windows-x64.msi"))  
        new_button.pack() 

    def start_new_window(self):  
        # 创建新窗口  
        new_window = tk.Toplevel(self.master)  
        new_window.title("说明")  
  
        # 设置新窗口默认大小  
        new_window.geometry("250x200")  
  
        # 允许新窗口改变大小  
        new_window.resizable(False, False)  
  
        new_label = tk.Label(new_window, text="该程序目前为Dev v0.1.2")
        new_label.pack()
        new_label = tk.Label(new_window, text="调用浏览器下载（基于Python3.12）")  
        new_label.pack()                                                        
        new_label = tk.Label(new_window, text="非商业盈利用途")  
        new_label.pack()
        new_label = tk.Label(new_window, text="可以去我们的B站空间充电赞助，非常感谢")  
        new_label.pack()
        new_button = tk.Button(new_window, text=" 我们的B站空间 ", width=10, height=1,  
                                command=lambda: webbrowser.open("https://space.bilibili.com/1995157657"))  
        new_button.pack()

    def create_new_window(self):  
        # 创建新窗口  
        new_window = tk.Toplevel(self.master)  
        new_window.title("属性")  
  
        # 设置新窗口默认大小  
        new_window.geometry("250x150")  
  
        # 允许新窗口改变大小  
        new_window.resizable(False, False)  
  
        # 在新窗口中添加一个标签  
        new_label = tk.Label(new_window, text="该程序目前为Dev v0.1.2")
        new_label.pack()
        new_label = tk.Label(new_window, text="调用浏览器下载（基于Python3.12）")  
        new_label.pack()
        new_button = tk.Button(new_window, text=" python官网 ", width=10, height=1,  
                                command=lambda: webbrowser.open("https://python.org"))  
        new_button.pack() 
        new_button = tk.Button(new_window, text=" 更新地址1 ", width=10, height=1,  
                                command=lambda: webbrowser.open("https://github.com/Fangkuaicangqiongya/DomeOS_Hub"))  
        new_button.pack() 

    def start_new_window2(self):  
        # 创建新窗口  
        new_window = tk.Toplevel(self.master)  
        new_window.title("说明")  
  
        # 设置新窗口默认大小  
        new_window.geometry("250x200")  
  
        # 允许新窗口改变大小  
        new_window.resizable(False, False)  
  
        new_label = tk.Label(new_window, text="该程序目前为Dev v0.1.2")
        new_label.pack()
        new_label = tk.Label(new_window, text="调用浏览器下载（基于Python3.12）")  
        new_label.pack()                                                        
        new_label = tk.Label(new_window, text="非商业盈利用途")  
        new_label.pack()
        new_label = tk.Label(new_window, text="可以去我们的B站空间充电赞助，非常感谢")  
        new_label.pack()
        new_button = tk.Button(new_window, text=" 我们的B站空间 ", width=10, height=1,  
                                command=lambda: webbrowser.open("https://space.bilibili.com/1995157657"))  
        new_button.pack()






root = tk.Tk()
app = ResizableWindow(root)
root.iconbitmap('app1.ico')
root.mainloop()
 
