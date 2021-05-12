
import os
from tkinter import *


class PhotoPreview:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Photo Preview')
        self.window_center(700, 700)
        
        self.labImage = Label(self.root, text='图片显示区')
        self.labImage.pack(pady=15)
        
        self.btnShow = Button(self.root, text='显示图片', command=self.preview)
        self.btnShow.pack(pady=10)
        
        self.listBox = Listbox(self.root, width=30, selectmode=SINGLE)
        self.listBox.pack(pady=10)
        
        self.__initListBox()
        
        self.root.mainloop()
    
    def __initListBox(self):
        self.images = {}
        os.makedirs('images', exist_ok=True)    # 如果images文件夹不存在，才会创建
        for i, image in enumerate(os.listdir('images')):
            self.images[f'1-{i+1}'] = f'images/{image}'
        
        for index in self.images.keys():
            self.listBox.insert(END, index)
    
    def window_center(self, width, height):
        '''通用型窗口居中'''
        win_width = self.root.winfo_screenwidth()
        win_height = self.root.winfo_screenheight()
        x = int((win_width - width) / 2)
        y = int((win_height - height) / 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def preview(self):
        curIndexs = self.listBox.curselection()
        for curIndex in curIndexs:
            i = self.listBox.get(curIndex)
            self.image = PhotoImage(file=self.images[i])
            self.labImage.config(image=self.image, compound='top')
            self.labImage.config(text=i, bg='yellow')


if __name__ == '__main__':
    PhotoPreview()