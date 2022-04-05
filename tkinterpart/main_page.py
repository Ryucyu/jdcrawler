import tkinter as tk
from tkinterpart.phone_page import ShowFrame

class MainPage:
    def __init__(self,master):
        self.window = master
        self.window.title('京东商城手机数据管理')
        self.window.geometry('980x880')
        self.create_page()

    def create_page(self):
        self.info_frame = ShowFrame(self.window)

        menubar = tk.Menu(self.window)
        menubar.add_command(label='显示数据',command=self.show_frame)

        self.window['menu'] = menubar

    def show_frame(self):
        self.info_frame.pack()


if __name__ == '__main__':
    window = tk.Tk()
    main = MainPage(window)
    window.mainloop()


