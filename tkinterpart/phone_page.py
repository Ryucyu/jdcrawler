import tkinter as tk
from tkinter import ttk
from tkinterpart.db import db
import webbrowser as web
from tkinter import messagebox
from PIL import Image, ImageTk
from itertools import combinations
import requests,os,time

class ShowFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.price = tk.StringVar()
        self.ram = tk.StringVar()
        self.rom = tk.StringVar()
        self.atp = tk.StringVar()
        self.resolution= tk.StringVar()
        self.CPU = tk.StringVar()
        self.S5G = tk.StringVar()
        self.name = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
            'Referer':'https://search.jd.com/'
        }

    def treeview_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: int(t[0].split('.')[0]), reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                tv.move(k, '', index)
            tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))
        except:
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)
            tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def create_page(self):
        self.price.set('1362-3573')
        tk.Label(self, text='价格区间').grid(row = 0, column = 0, sticky = "W", pady = 5)
        price1 = tk.Radiobutton(self, value ='0-349',text="0-349", variable=self.price).grid(row = 0, column = 1, sticky = "W", pady = 5)
        price2 = tk.Radiobutton(self, value ='349-1362',text="349-1362", variable=self.price).grid(row = 0, column = 2, sticky = "W", pady = 5)
        price3 = tk.Radiobutton(self, value='1362-3573', text="1362-3573", variable=self.price).grid(row=0, column=3,sticky="W", pady=5)
        price4 = tk.Radiobutton(self, value='3573-8096', text="3573-8096", variable=self.price).grid(row=0, column=4,sticky="W", pady=5)
        price5 = tk.Radiobutton(self, value='8096-36999', text="8096-36999", variable=self.price).grid(row=0, column=5,sticky="W", pady=5)

        self.ram.set('8GB')
        values = ('4GB', '6GB', '8GB', '12GB', '其他', '未知运行内存')
        texts = ('4GB', '6GB', '8GB', '12GB', '其他', '未知运行内存')
        tk.Label(self, text='内存').grid(row = 1, column = 0, sticky = "W", pady = 5)
        i = 1
        for value, text in zip(values, texts):
            b = tk.Radiobutton(self, value=value,text=text, variable=self.ram).grid(row = 1, column = i, sticky = "W", pady = 5)
            i = i + 1

        self.rom.set('128GB')
        tk.Label(self, text='储存').grid(row=2, column=0, sticky="W", pady=5)
        values = ('16GB','32GB','64GB','128GB','256GB','其他','未知机身内存')
        texts = ('16GB','32GB','64GB','128GB','256GB','其他','未知机身内存')
        i = 1
        for value,text in zip(values,texts):
            b = tk.Radiobutton(self, text=text, variable=self.rom, value=value).grid(row = 2, column = i, sticky = "W", pady = 5)
            i = i + 1

        self.atp.set('2400万像素')
        tk.Label(self, text='后置像素').grid(row=3, column=0, sticky="W", pady=5)
        values = ('1600万像素', '2400万像素', '4800万像素', '6400万像素', '10000万像素', '其他', '未知后摄像素')
        texts = ('1600万像素', '2400万像素', '4800万像素', '6400万像素', '10000万像素', '其他', '未知后摄像素')
        i = 1
        for value, text in zip(values, texts):
            b = tk.Radiobutton(self, text=text, variable=self.atp, value=value).grid(row=3, column=i, sticky="W",pady=5)
            i = i + 1

        self.resolution.set('全高清FHD+')
        tk.Label(self, text='屏幕').grid(row=4, column=0, sticky="W", pady=5)
        values = ('全高清FHD+', '高清HD+', 'QHD+及以上', '标清SD', '其他', '未知分辨率')
        texts = ('全高清FHD+', '高清HD+', 'QHD+及以上', '标清SD', '其他', '未知分辨率')
        i = 1
        for value, text in zip(values, texts):
            b = tk.Radiobutton(self, text=text, variable=self.resolution, value=value).grid(row=4, column=i, sticky="W",pady=5)
            i = i + 1

        self.CPU.set('暂无型号')
        tk.Label(self, text='CPU').grid(row=5, column=0, sticky="W", pady=5)
        values = ('麒麟990','骁龙855plus','骁龙888','紫光展锐','骁龙8 Gen 1','天玑900','其他','暂无型号')
        texts = ('麒麟990','骁龙855plus','骁龙888','紫光展锐','骁龙8 Gen 1','天玑900','其他','暂无型号')
        i = 1
        for value, text in zip(values, texts):
            b = tk.Radiobutton(self, text=text, variable=self.CPU, value=value).grid(row=5, column=i, sticky="W",pady=5)
            i = i + 1

        self.S5G.set('支持5G')
        tk.Label(self, text='支持5G').grid(row=6, column=0, sticky="W", pady=5)
        values = ('支持5G', '不支持5G')
        texts = ('支持5G', '不支持5G')
        i = 1
        for value, text in zip(values, texts):
            b = tk.Radiobutton(self, text=text, variable=self.S5G, value=value).grid(row=6, column=i, sticky="W",pady=5)
            i = i + 1

        tk.Label(self, text='通过名字查询').grid(row=7, column=0, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=7, column=1, pady=10)
        tk.Button(self, text='查询', command=self.search).grid(row=7, column=2, sticky="W", pady=2)

        tk.Button(self, text='清空选项', command=self.clear).grid(row=8, column=8, sticky="W", pady=2)
        tk.Button(self, text='确认查询', command=self.confirm).grid(row = 8, column = 9, sticky = "W", pady = 2)
        tk.Label(self, text='双击即可进入商品页面！').grid(row=9, column=0, columnspan=2, sticky="W", pady=2)
        tk.Label(self, text='选中后右键单击可下载并显示商品图片！').grid(row=9, column=3, columnspan=2, sticky="W", pady=2)
        tk.Label(self, text='单击商品属性可排序！').grid(row=9, column=6, columnspan=2, sticky="W", pady=2)
        tk.Label(self, textvariable=self.status).grid(row = 9, column = 8, columnspan=3,sticky = "W", pady = 2)

        columns = ('name','price','inner_href','RAM','ROM','After_taken_pixel','resolution','CPU','S5G')
        columns_values = ('名称','价格', '商品地址', '内存', '储存','后置像素','屏幕','CPU','5G支持')
        self.tree_view = ttk.Treeview(self,show='headings',columns=columns)
        self.tree_view.bind('<Double-1>',self.onDBClick)
        self.tree_view.bind('<Button-3>', self.onTRClick)

        for column in columns:
            self.tree_view.column(column, width=100, anchor='center')

        for column,columns_value in zip(columns,columns_values):
            self.tree_view.heading(column, text=columns_value)

        for col,columns_value in zip(columns,columns_values):
            self.tree_view.heading(col, text=columns_value, command=lambda _col=col: self.treeview_sort_column(self.tree_view, _col, False))

        self.show_data_frame()
        self.tree_view.grid(row=10, column=0, columnspan=10,sticky='nsew')

    def search(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        jdphone = db.all()
        index = 0
        for info in jdphone:
            if info['name'] == self.name.get():
                self.tree_view.insert('', index + 1, values=(
                    info['name'], info['price'], info['inner_href'], info['RAM'], info['ROM'], info['After_taken_pixel'],
                    info['resolution'], info['CPU'], info['S5G']
                ))

    def clear(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        self.price.set('None Selected')
        self.ram.set('None Selected')
        self.rom.set('128GB')
        self.atp.set('2400万像素')
        self.resolution.set('全高清FHD+')
        self.CPU.set('暂无型号')
        self.S5G.set('None Selected')

    def onTRClick(self, event):
        item = self.tree_view.selection()[0]
        info = self.tree_view.item(item, "values")
        url = info[2]
        jdphone = db.all()
        for info in jdphone:
            pic_href = info['pic']
            if url == info['inner_href']:
                r = requests.get(pic_href,headers=self.headers)
                open('../img/'+pic_href.split('/')[-1], 'wb').write(r.content)
                # time.sleep(2)
                global photo
                photo = ImageTk.PhotoImage(file='../img/'+pic_href.split('/')[-1])  # 用PIL模块的PhotoImage打开
                imglabel = tk.Label(self, image=photo).grid(row=11, column=0, columnspan=10, sticky='nsew')

    def confirm(self):
        i = 0
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        jdphone = db.all()
        index = 0
        for info in jdphone:
            min_price = int(self.price.get().split('-')[0])
            max_price = int(self.price.get().split('-')[1])
            info_price = int(info['price'].split('.')[0])

            # c1 = "info['RAM'] == self.ram.get()"
            # c2 = "info_price >= min_price and info_price <= max_price"
            # c3 = "info['S5G'] == self.S5G.get()"
            if info['RAM'] == self.ram.get() and (info_price >= min_price and info_price <= max_price) \
                                             and info['ROM'] == self.rom.get() and info['After_taken_pixel'] == self.atp.get() and info['resolution'] == self.resolution.get() \
                                             and info['CPU'] == self.CPU.get()  and info['S5G'] == self.S5G.get():
                self.tree_view.insert('', index + 1, values=(
                    info['name'], info['price'], info['inner_href'], info['RAM'], info['ROM'], info['After_taken_pixel'],
                    info['resolution'], info['CPU'], info['S5G']
                ))
                i = i + 1
        self.status.set(f'总共查找到{i}条数据')

    def onDBClick(self,event):
        item = self.tree_view.selection()[0]
        info = self.tree_view.item(item, "values")
        url = info[2]
        web.open_new(url)

    def show_data_frame(self):
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass
        jdphone = db.all()
        index = 0
        for info in jdphone:
            self.tree_view.insert('',index + 1,values=(
                info['name'],info['price'],info['inner_href'],info['RAM'],info['ROM'],info['After_taken_pixel'],info['resolution'],info['CPU'],info['S5G']
            ))



#年轻不懂事的结果

# rom1 = tk.Radiobutton(self, value='16GB',text='16GB', variable=self.rom).grid(row = 2, column = 1, sticky = "W", pady = 2)
# rom2 = tk.Radiobutton(self, value='32GB', text='32GB', variable=self.rom).grid(row=2, column=2, sticky="W",pady=2)
# rom3 = tk.Radiobutton(self, value='64GB', text='64GB', variable=self.rom).grid(row=2, column=3, sticky="W",pady=2)
# rom4 = tk.Radiobutton(self, value='128GB', text='128GB', variable=self.rom).grid(row=2, column=4, sticky="W",pady=2)
# rom5 = tk.Radiobutton(self, value='256GB', text='256GB', variable=self.rom).grid(row=2, column=5, sticky="W",pady=2)
# rom6 = tk.Radiobutton(self, value='其他', text='其他', variable=self.rom).grid(row=2, column=6, sticky="W",pady=2)
# rom7 = tk.Radiobutton(self, value='未知运行内存', text='未知运行内存', variable=self.rom).grid(row=2, column=7, sticky="W",pady=2)

# ram1 = tk.Radiobutton(self, value='4GB',text="4GB", variable=self.ram).grid(row = 1, column = 1, sticky = "W", pady = 2)
# ram2 = tk.Radiobutton(self, value='6GB',text="6GB", variable=self.ram).grid(row = 1, column = 2, sticky = "W", pady = 2)
# ram3 = tk.Radiobutton(self, value='8GB',text="8GB", variable=self.ram).grid(row = 1, column = 3, sticky = "W", pady = 2)
# ram4 = tk.Radiobutton(self, value='12GB', text="12GB", variable=self.ram).grid(row = 1, column = 4, sticky = "W", pady = 2)
# ram5 = tk.Radiobutton(self, value='其他', text="其他", variable=self.ram).grid(row = 1, column = 5, sticky = "W", pady = 2)
# ram6 = tk.Radiobutton(self, value='未知运行内存', text="未知运行内存", variable=self.ram).grid(row = 1, column = 6, sticky = "W", pady = 2)
#

# self.tree_view.heading('name', text='名称')
# self.tree_view.heading('price',text='价格')
# self.tree_view.heading('inner_href', text='商品链接')
# self.tree_view.heading('RAM', text='内存')
# self.tree_view.heading('ROM', text='储存')
# self.tree_view.heading('After_taken_pixel', text='后置像素')
# self.tree_view.heading('resolution', text='屏幕')
# self.tree_view.heading('CPU', text='CPU')
# self.tree_view.heading('S5G', text='5G支持')

# self.tree_view.column('name', width=180, anchor='center')
# self.tree_view.column('price',width=80,anchor='center')
# self.tree_view.column('inner_href', width=180, anchor='center')
# self.tree_view.column('RAM', width=80, anchor='center')
# self.tree_view.column('ROM', width=80, anchor='center')
# self.tree_view.column('After_taken_pixel', width=80, anchor='center')
# self.tree_view.column('resolution', width=80, anchor='center')
# self.tree_view.column('CPU', width=80, anchor='center')
# self.tree_view.column('S5G', width=80, anchor='center')

#if info['RAM'] == self.ram.get():
            #     flag1 = 1
            # else:
            #     flag1 = 0
            # if info_price >= min_price and info_price <= max_price:
            #     flag2 = 1
            # else:
            #     flag2 = 0
            # if info['S5G'] == self.S5G.get():
            #     flag3 = 1
            # else:
            #     flag3 = 0
            # test_data = []
            # con_data = []
            # test_data.extend([flag1,flag2,flag3])
            # print(test_data)
            # for i in range(1, len(test_data) + 1):
            #     iter1 = combinations(test_data, i)
            #     con_data.append(list(iter1))
            # print(con_data)
            # for i in con_data:
            #     for j in i:
            #         for k in j:
            #             if k:
            #                 self.tree_view.insert('', index + 1, values=(
            #                     info['name'], info['price'], info['inner_href'], info['RAM'], info['ROM'],
            #                     info['After_taken_pixel'],
            #                     info['resolution'], info['CPU'], info['S5G']
            #                 ))
            #                 i = i + 1


